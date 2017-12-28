// ALL snakes are AI
// How to import javascript?
const MAX_TRACK_LENGTH = 50;
const MAX_QUADRANTS = 16;

var canvas = document.getElementById("backgroundCanvas");
canvas.width = 750;
canvas.height = 500;

if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
}

// SnakeGame - superclass
function SnakeGame(num_alive) {
    this.num_alive = num_alive;
    this.colour = "#000000";
    this.board_arr = new Array();
    for (i = 0; i < this.y_range; i++) {
        this.board_arr[i] = [];
        for (j = 0; j < this.x_range; j++) {
            this.board_arr[i][j] = 0;
        }
    }
}

// spacing of the coordinates on the screen
SnakeGame.prototype.unit_space = 7.5;
SnakeGame.prototype.x_range = Math.floor(canvas.width / (2 * SnakeGame.prototype.unit_space));
SnakeGame.prototype.y_range = Math.floor(canvas.height / (2 * SnakeGame.prototype.unit_space));
// colours of snakes
SnakeGame.prototype.colours = ["#53F527", "#9821F0", "#21F0EA", "#F0ED21", "#FF6F50", "#ffffff"];
// draw black board
SnakeGame.prototype.drawBoard = function () {
    ctx.fillStyle = this.colour;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
};
// print board values
SnakeGame.prototype.debugBoard = function () {
    ctx.fillStyle = "#FF6F50";
    ctx.font = "8px Arial";
    for (i = 0; i < this.y_range; i++) {
        for (j = 0; j < this.x_range; j++) {
            var txt = this.board_arr[i][j];
            ctx.fillText(txt, 2 * j * this.unit_space + this.unit_space, 2 * i * this.unit_space + this.unit_space);
        }
    }
}
// write start screen words
SnakeGame.prototype.drawStartWords = function () {
    ctx.fillStyle = "#ffffff";
    ctx.font = "50px Arial";
    var txt = "Click to begin, again to pause!"
    ctx.fillText(txt, canvas.width / 2 - ctx.measureText(txt).width / 2, canvas.height / 2);
}
// writes end screen words
SnakeGame.prototype.drawEndWords = function () {
    ctx.fillStyle = "#ffffff";
    ctx.font = "50px Arial";
    var txt = "Game Over! Press 'r' to restart!"
    ctx.fillText(txt, canvas.width / 2 - ctx.measureText(txt).width / 2, canvas.height / 2);
}

function GameObject() {
    this.posx;
    this.posy;
    this.colour;
}

GameObject.prototype = Object.create(SnakeGame.prototype);
GameObject.prototype.constructor = GameObject;

GameObject.prototype.hitObject = function (board, type = 'both', posx = this.posx, posy = this.posy) {
    var hit = false;
    switch (type) {
        case 'snake':
            hit = board.board_arr[posy][posx] == 2 ? true : false;
            break;
        case 'food':
            hit = board.board_arr[posy][posx] == 1 ? true : false;
            break;
        case 'wall':
            if (posx < 0 || posx >= this.x_range) {
                hit = true;
            }
            else if (posy < 0 || posy >= this.y_range) {
                hit = true;
            }
            else {
                hit = false;
            }
            break;
        case 'both':
            hit = (board.board_arr[posy][posx] != 0) ? true : false;
            break;
        default:
            alert("put in wrong value for a SnakeGame.prototype.hit function");
            hit = (board.board_arr[posy][posx] != 0) ? true : false;
            break;
    }
    return hit;
}

// determins the manhattan distance between x and the GameObject
GameObject.prototype.manhattanDistance = function (x){
    return Math.abs((this.posx - x.posx) + (this.posy - x.posy));
}

// determines the euclidian distance between x and the GameObject
GameObject.prototype.euclidianDistance = function (x){
    return Math.sqrt(Math.pow((this.posx - x.posx), 2) + Math.pow((this.posy - x.posy),2));
}

// gets direction vector between the instance and x
// vector originates from the instance
GameObject.prototype.getVector = function (x){
    return [x.posx - this.posx, x.posy - this.posy];
}

// gets unit direction vector originating from GameObject instance and ending at x
GameObject.prototype.getUnitVector = function (x){
    var vector = this.getVector(x);
    var dist = this.euclidianDistance(x);
    return vector.map(x => x/dist);
}

// gets the direction quadrant of x relative to the GameObject
GameObject.prototype.getDirection = function (x){
    var unit_vector = this.getUnitVector(x);
}

function State(snake, food, board){
    this.food_dir;
    this.food_dist = snake.head.manhattanDistance(food);
    this.sn_length = snake.length;
    this.tail_dir;
    this.valid_movements;
}

function Action(){

}

function StateActionPair(s, a){
    this.state = s;
    this.action = a;
}

var key = function(state_action){
    var k = state_action.toString();
}

// Reinforcement learning stuff
// A state is composed of:
// Direction of food (quadrant), distance of food, snake length (capped at MAX_TRACK_LENGTH), direction of tail
// Whether the snake is able to go in each of the 3 directions possible
function Environment(){

}


// Board - subclass
// 0 in board_arr means empty, 1 means food, 2 means snake
function Board(){
    this.colour = "#00000";
    this.board_arr = new Array();
    for (i = 0; i < this.y_range; i++){
        this.board_arr[i] = [];
        for (j = 0; j < this.x_range; j++){
            this.board_arr[i][j] = 0;
        }
    }
}

// set up Board so it inherits from SnakeGame
Board.prototype = Object.create(GameObject.prototype);
Board.prototype.constructor = Board;

Board.prototype.draw = function () {
    ctx.fillStyle = this.colour;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
};

Board.prototype.debugArr = function () {
    ctx.fillStyle = "#FF6F50";
    ctx.font = "8px Arial";
    for (i = 0; i < this.y_range; i++) {
        for (j = 0; j < this.x_range; j++) {
            var txt = this.board_arr[i][j];

            ctx.fillText(txt, 2 * j * this.unit_space + this.unit_space, 2 * i * this.unit_space + this.unit_space);
        }
    }
}

// Food - subclass - new Food also updates board array
function Food(board) {
    this.colour = this.colours[5];
    this.size = 5;

    // randomly puts food, then checks for overlap
    // in case of overlap, tries for a new position
    var overlap = true;
    while (overlap) {
        this.posx = Math.floor(Math.random() * this.x_range);
        this.posy = Math.floor(Math.random() * this.y_range);

        overlap = this.hitObject(board);
    }
    board.board_arr[this.posy][this.posx] = 1;
};

// set of Food so it inherits form SnakeGame
Food.prototype = Object.create(GameObject.prototype);
Food.prototype.constructor = Food;

Food.prototype.draw = function () {
    ctx.fillStyle = this.colour;
    ctx.beginPath();
    var pixel_x = this.posx * (2 * this.unit_space) + this.unit_space;
    var pixel_y = this.posy * (2 * this.unit_space) + this.unit_space;
    ctx.arc(pixel_x, pixel_y, this.size, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();
};


function BodySegment(x, y, prev_seg, next_seg) {       // the x and y are coordinates of the board - from 0 to board's x_range and y_range\
    this.posx = x; //* (2 * this.unit_space) + 7.5; for drawing
    this.posy = y;
    this.prev = prev_seg;
    this.next = next_seg;
    this.size = this.unit_space;
};

BodySegment.prototype = Object.create(GameObject.prototype);
BodySegment.prototype.constructor = BodySegment;

// new Snake also updates board array
function Snake(colour_ind, board) {
    var self = this;
    this.colour = this.colours[colour_ind];
    this.is_alive = true;
    this.length = 1;
    this.head = this.createHead(board);
    this.tail = this.head;
    this.hit = 'unhit';
};

Snake.prototype = Object.create(GameObject.prototype);
Snake.prototype.constructor = Snake;

Snake.prototype.logBody = function () {
    var arr = []
    var seg = this.head;

    while (seg != null) {
        arr.push([seg.posx + " " + seg.posy]);
        seg = seg.next;
    }
    console.log(arr);
}

// creates the head of the snake and updates the board array
Snake.prototype.createHead = function (board) {
    var overlap = true;

    while (overlap) {
        var h_x = Math.floor(Math.random() * this.x_range/2 + this.x_range/4);
        var h_y = Math.floor(Math.random() * this.y_range/2 + this.x_range/4);

        var head = new BodySegment(h_x, h_y, null, null);
        overlap = head.hitObject(board);
    }

    board.board_arr[head.posy][head.posx] = 2;
    this.length += 1;
    return head;
};

// adds a segment to the end of the snake with specified posx and posy
// also updates the board array to reflect that
Snake.prototype.addTail = function (posx, posy, board) {
    var body = new BodySegment(posx, posy, null, null);
    //alert('initial');
    if (this.length == 1) {
        this.head.next = body;
        this.tail = body;
        body.prev = this.head;
    }
    else {
        body.prev = this.tail;
        this.tail.next = body;
        this.tail = body;

    }
    //alert('middle');
    board.board_arr[posy][posx] = 2;
    this.length += 1;
    //alert('end');
}

// moves snake and updates board
Snake.prototype.move = function (board) {

}

Snake.prototype.draw = function () {
    ctx.fillStyle = this.colour;
    
    var cur_seg = this.head;
    ctx.fillStyle = "#F0ED21";

    while (cur_seg != null) {
        ctx.beginPath();
        var pixel_x = cur_seg.posx * (2 * this.unit_space) + this.unit_space;
        var pixel_y = cur_seg.posy * (2 * this.unit_space) + this.unit_space;
        ctx.arc(pixel_x, pixel_y, cur_seg.size, 0, 2 * Math.PI);
        ctx.closePath();
        ctx.fill();

        cur_seg = cur_seg.next;
        ctx.fillStyle = this.colour;
    }
};

Snake.prototype.resolveHit = function(self, board, food_arr){

}

Snake.prototype.anyHit = function(next_x, next_y, board){
    // Wall detection
    if (this.hitObject(board, 'wall', next_x, next_y)) {
        this.hit = 'wall';
    }
    // Food detection:
    // If the snake's movement brings it into a 'Food', 
    // instead of moving the snake, add a new snake body ontop of the Food, and make a new Food.
    else if (this.hitObject(board, 'food', next_x, next_y)) {
        this.hit = 'food';
    }
    // Only move if the snake's movement will not cause any collisions
    else if (this.hitObject(board, 'snake', next_x, next_y)) {
        this.hit = 'snake';
    } else {
        this.hit = 'unhit';
    }
}

Snake.prototype.printScore = function (ind) {
    ctx.fillStyle = "#ffffff";
    ctx.font = "20px Arial";
    ctx.fillText("Score", canvas.width - 100, canvas.height - 120);
    ctx.font = "10px Arial";

    var txt = "Player " + String(ind + 1) + ": " + String(this.length);
    ctx.fillText(txt, canvas.width - 100, canvas.height - (100 - 20 * (ind)));
};

SnakeGame.prototype.createType = function (num, board, type) {
    var type_arr = new Array(num);
    for (i = 0; i < num; i++) {
        switch (type){
            case ('snake'):
                o = new Snake(i % 5, board, true);
                break;
            case ('food'):
                o = new Food(board);
                break;
            default:
                console.log('Wrong type input to createType');
                break;
        }
        type_arr[i] = o;
    }
    return type_arr;
}

SnakeGame.prototype.runFrame = function (board, snake_arr, food_arr, self){
    board.draw();
    if (self.alive_hum == 0) {
        self.drawEndWords();
        console.log("game over");
        clearInterval(canvas.interval);
        canvas.interval = null;
        canvas.removeEventListener("click", start);
        return;
    }

    //take player input and move player snakes
    //calculate the ai's movements
    //update the snake's positions according to movements - include growing and removing food
    //draw everything
    //write the score
    for (var i = 0; i < snake_arr.length; i++) {
        cur_snake = snake_arr[i];
        var a_output;
        if (cur_snake.is_alive) { 

            // MOVE?

            // The coordinate of the snake's head after the snake's movement
            var next_x = cur_snake.head.posx + cur_snake.dir[0];
            var next_y = cur_snake.head.posy + cur_snake.dir[1];
            // Check whether snake head's position after movement is within bounds first
            // then check for food collision
            cur_snake.anyHit(next_x, next_y, board, food_arr, self);
            cur_snake.resolveHit(self, board, food_arr);
        }
        cur_snake.printScore(i);
        cur_snake.draw();
    }
    for (i = 0; i < food_arr.length; i++) {
        food_arr[i].draw();
    }
    //board.debugArr();
}

SnakeGame.prototype.startGame = function (num_snake, num_food) {
    var self = this;
    var board = new Board();
    var snake_arr = this.createType(num_snake, board, 'snake');
    var food_arr = this.createType(num_food, board, 'food');
    board.draw();
    this.drawStartWords();

    canvas.addEventListener("click", start = function (event) {
        if (canvas.interval != null) {
            console.log('paused');
            clearInterval(canvas.interval);
            canvas.interval = null;
        } else {
            console.log('resume');
            canvas.interval = setInterval(function() {SnakeGame.prototype.runFrame(board, snake_arr, food_arr, self)}, 1000 / 10);
        }
    });
};

var num_snakes = 1;

var sg = new SnakeGame(num_snakes);
sg.startGame(num_snakes, 10);

canvas.addEventListener('keydown', function (event) {
    if (event.keyCode == 82){
        clearInterval(canvas.interval);
        canvas.interval = null;
        canvas.removeEventListener("click", start);
        var sg = new SnakeGame(num_snakes);
        sg.startGame(num_snakes, 10);
    }
})
