// ALL snakes are AI
// How to import javascript?
const MAX_QUADRANTS = 4;
// up left down right
const DIRECTIONS = [[0, 1], [-1, 0], [0, -1], [1, 0]];
const SNAKE_LENGTH_ROUNDING = 4;
const CANVAS_WIDTH = 750;
const CANVAS_HEIGHT = 500;

var canvas = document.getElementById("backgroundCanvas");
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;

// spacing of the coordinates on the screen
const UNIT_SPACE = 15;
const X_RANGE = Math.floor(CANVAS_WIDTH / (2 * UNIT_SPACE)); // 25
const Y_RANGE = Math.floor(CANVAS_HEIGHT / (2 * UNIT_SPACE)); // 16

// set up board
var board_arr = new Array();
for (i = 0; i < SnakeGame.prototype.y_range; i++) {
    board_arr[i] = [];
    for (j = 0; j < SnakeGame.prototype.x_range; j++) {
        board_arr[i][j] = 0;
    }
}

var resetBoard = function(){
    board_arr.forEach(function(item, i){
        item.forEach(function(ele, j){
            ele = 0;
        })
    });
}

if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
}

// SnakeGame - superclass
function SnakeGame(num_alive) {
    this.num_alive = num_alive;
    this.colour = "#000000";
}

SnakeGame.num_squares = X_RANGE * Y_RANGE;
// colours of snakes
SnakeGame.prototype.colours = ["#53F527", "#9821F0", "#21F0EA", "#F0ED21", "#FF6F50", "#ffffff"];
// draw black board
SnakeGame.prototype.drawBoard = function() {
    ctx.fillStyle = this.colour;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
};
// print board values
SnakeGame.prototype.debugBoard = function() {
    ctx.fillStyle = "#FF6F50";
    ctx.font = "8px Arial";
    for (i = 0; i < Y_RANGE; i++) {
        for (j = 0; j < X_RANGE; j++) {
            var txt = board_arr[i][j];
            ctx.fillText(txt, 2 * j * UNIT_SPACE + UNIT_SPACE, 2 * i * UNIT_SPACE + UNIT_SPACE);
        }
    }
}

// generated quadrants are in terms of angles from the y-axis
// counting counterclockwise, starting from 0 at the positive y-axis
SnakeGame.generateQuadrants = function() {
    var quadrants = [];
    for (i = 0; i < MAX_QUADRANTS; i++) {
        // angle from the forward y-axis, counting counterclockwise
        var angle = i * (2*Math.PI/MAX_QUADRANTS);
        quadrants[0] = angle;
    }
    return quadrants;
}

// Converts a vector from cartesian plane to form of polar coordinates
// Angle 0 starts at the positive y axis, and increases clockwise
// Used to decide which quadrant a vector is in
SnakeGame.convertAxis = function(angle) {
    return Math.tan(angle[1]/angle[0]);
}

// write start screen words
SnakeGame.prototype.drawStartWords = function() {
    ctx.fillStyle = "#ffffff";
    ctx.font = "50px Arial";
    var txt = "Click to begin, again to pause!"
    ctx.fillText(txt, canvas.width / 2 - ctx.measureText(txt).width / 2, canvas.height / 2);
}
// writes end screen words
SnakeGame.prototype.drawEndWords = function() {
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

GameObject.prototype.hitObject = function (type = 'both', posx = this.posx, posy = this.posy) {
    var hit = false;
    switch (type) {
        case 'snake':
            hit = board_arr[posy][posx] == 2 ? true : false;
            break;
        case 'food':
            hit = board_arr[posy][posx] == 1 ? true : false;
            break;
        case 'wall':
            if (posx < 0 || posx >= X_RANGE) {
                hit = true;
            }
            else if (posy < 0 || posy >= Y_RANGE) {
                hit = true;
            }
            else {
                hit = false;
            }
            break;
        case 'both':
            hit = (board_arr[posy][posx] != 0) ? true : false;
            break;
        default:
            alert("put in wrong value for a SnakeGame.prototype.hit function");
            hit = (board_arr[posy][posx] != 0) ? true : false;
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
// vector originates from the instance (this)
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
// Quadrant 0 to quadrant MAX_QUANDRANT - 1, quadrant 0 starts from
// straight ahead and goes clockwise
GameObject.prototype.getDirection = function (x){
    var unit_vector = this.getUnitVector(x);
    var quadrants = SnakeGame.generateQuadrants();
    var polar_vector = SnakeGame.convertAxis(unit_vector);
    quadrants.forEach(function(item, index, array){
        // Convert quadrants back to polar angles
        // Angles are counted from 0 and upwards
        // The first time the polar_vector is smaller than the quadrant angle
        // means that the polar_vector is between that quadrant line and the previous quadrant line
        // The quadrant to return will be the previous quadrant (ie between 0 and 1 would return 0)
        if (polar_vector < item * (Math.PI*2/MAX_QUADRANTS)) {
            return (index - 1);
        }
    });
    // If the polar_vector is between the last quadrant line and the 0 quadrant line, then the for
    // loop will not catch it. So put in this extra edge case
    return MAX_QUADRANTS - 1;
}

function State(food_dir, food_dist, tail_dir, sn_length, valid_movements){
    this.food_dir = food_dir;
    this.food_dist = food_dist;
    this.tail_dir = tail_dir;
    this.sn_length = sn_length;
    this.valid_movements = valid_movements;
}

var gameToState = function(snake, food, board) {
    var food_dir = snake.head.getDirection(food);
    var food_dist = Math.ceil(snake.head.manhattanDistance(food)/(X_RANGE + Y_RANGE))*10;
    var tail_dir = snake.head.getDirection(snake.tail);
    var sn_length = Math.ceil(snake.length/SnakeGame.num_squares)*10;
    var valid_movements = snake.getValidMovements;
    return (new State(food_dir, food_dist, tail_dir, sn_length, valid_movements));
}

State.prototype.toString = function(){
    //debugger;
    var str = '';
    Object.values(this).forEach(function(value, index){
        str += value;
    });
    
    return str;
    
}

// action a is one of the cardinal directions
// map to DIRECTIONS with action being the index in DIRECTIONS that matches with a
// if it isn't a cardinal direction, return -1
var directionToAction = function(a) {
    DIRECTIONS.forEach(function(item, index, array){
        if (item[0] == a[0] && item[1] == a[1]) {
            return index;
        }
    });
    return -1;
}

function StateActionPair(s, a){
    this.state = s;
    this.action = a;
}

StateActionPair.prototype.toDirection = function(){
    return DIRECTIONS[this.action];
}

StateActionPair.prototype.toString = function(){
    var state_action_string = "";
    state_action_string += this.state.toString();
    state_action_string += this.action.toString();
    return state_action_string;
}

var movementPermutations = function(){
    var move_perm = ['0', '1'];
    for (i = 1; i < 4; i++){
        var len = move_perm.length
        for (j = 0; j < len; j++){
            var perm = move_perm[j];
            move_perm.push(perm+'0');
            move_perm.push(perm+'1');
        };
        move_perm = move_perm.filter(x => x.length > i);
    }
    return move_perm;
}

// for all state and all actions, initialize to value
var initializeStateActionMap = function(value){
    var state_action_map = {};
    for (food_dir = 0; food_dir < 1 /*MAX_QUADRANTS*/; food_dir++){
        for (food_dist = 0; food_dist < 1/*10*/; food_dist++){
            for (sn_length = 1; sn_length < 2/*10*/; sn_length++){
                for (tail_dir = 0; tail_dir < MAX_QUADRANTS; tail_dir++){
                    movementPermutations().forEach(function(item, index, array){
                        for (action = 0; action < DIRECTIONS.length; action++){
                            var S = new State(food_dir, food_dist, tail_dir, sn_length, item);
                            var SAP = new StateActionPair(S, action);
                            state_action_map[SAP.toString()] = value;
                        }
                    });
                }
            }
        }   
    }
    return state_action_map;
}

var selectAction = function(cur_state, value_map){

}

var QLearning = function(num_iteration){
    var value_map = initializeStateActionMap(-1);
    var count_map = initializeStateActionMap(1);

    for (i = 0; i < num_iteration; i++){
        sn = new Snake(0);
        fd = new Food();

        resetBoard();
    }
}

// Food - subclass - new Food also updates board array
function Food() {
    this.colour = this.colours[5];
    this.size = 5;

    // randomly puts food, then checks for overlap
    // in case of overlap, tries for a new position
    var overlap = true;
    while (overlap) {
        this.posx = Math.floor(Math.random() * X_RANGE);
        this.posy = Math.floor(Math.random() * Y_RANGE);

        overlap = this.hitObject();
    }
    board_arr[this.posy][this.posx] = 1;
};

// set of Food so it inherits form SnakeGame
Food.prototype = Object.create(GameObject.prototype);
Food.prototype.constructor = Food;

Food.prototype.draw = function () {
    ctx.fillStyle = this.colour;
    ctx.beginPath();
    var pixel_x = this.posx * (2 * UNIT_SPACE) + UNIT_SPACE;
    var pixel_y = this.posy * (2 * UNIT_SPACE) + UNIT_SPACE;
    ctx.arc(pixel_x, pixel_y, this.size, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.fill();
};


function BodySegment(x, y, prev_seg, next_seg) {       // the x and y are coordinates of the board - from 0 to board's x_range and y_range\
    this.posx = x; //* (2 * UNIT_SPACE) + 7.5; for drawing
    this.posy = y;
    this.prev = prev_seg;
    this.next = next_seg;
    this.size = UNIT_SPACE;
};

BodySegment.prototype = Object.create(GameObject.prototype);
BodySegment.prototype.constructor = BodySegment;

// new Snake also updates board array
function Snake(colour_ind) {
    var self = this;
    this.colour = this.colours[colour_ind];
    this.is_alive = true;
    this.length = 1;
    this.head = this.createHead();
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
Snake.prototype.createHead = function () {
    var overlap = true;

    while (overlap) {
        var h_x = Math.floor(Math.random() * X_RANGE/2 + X_RANGE/4);
        var h_y = Math.floor(Math.random() * Y_RANGE/2 + X_RANGE/4);

        var head = new BodySegment(h_x, h_y, null, null);
        overlap = head.hitObject();
    }

    board_arr[head.posy][head.posx] = 2;
    this.length += 1;
    return head;
};

// adds a segment to the end of the snake with specified posx and posy
// also updates the board array to reflect that
Snake.prototype.addTail = function(posx, posy) {
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
    board_arr[posy][posx] = 2;
    this.length += 1;
    //alert('end');
}

Snake.prototype.getValidMovements = function() {
    var movements = "";
    DIRECTIONS.forEach(function(item, index, array){
        var new_x = this.head.posx + item[0];
        var new_y = this.head.posy + item[1];
        if (this.hitObject(board, 'wall', new_x, new_y)) {
            movements += '0';
        } else {
            movements += '1';
        }
    });
    return movements;
}

// moves snake and updates board
Snake.prototype.move = function() {
    // from the tail, change position to the previous segment's position thus moving snake
    var cur_seg = this.tail;
    if (cur_seg != null) {
        board_arr[cur_seg.posy][cur_seg.posx] = 0;
        while (cur_seg.prev != null) {
            cur_seg.posx = cur_seg.prev.posx;
            cur_seg.posy = cur_seg.prev.posy;
            cur_seg = cur_seg.prev;
        }
    } else {
        // if cur_seg is null, then the length of snake is 1, so would update the old head value to 0
        board_arr[this.head.posy][this.head.posx] = 0;
    }

    // move the head via the snake's dir
    // requires explicitly state cur_seg = this.head for when snake's length's is 1
    // and the tail's previous is null, so would be moving head instead of tail.
    cur_seg = this.head;
    cur_seg.posx += this.dir[0];
    cur_seg.posy += this.dir[1];
    // updates board array
    board_arr[this.head.posy][this.head.posx] = 2;    
}

Snake.prototype.draw = function() {
    ctx.fillStyle = this.colour;
    
    var cur_seg = this.head;
    ctx.fillStyle = "#F0ED21";

    while (cur_seg != null) {
        ctx.beginPath();
        var pixel_x = cur_seg.posx * (2 * UNIT_SPACE) + UNIT_SPACE;
        var pixel_y = cur_seg.posy * (2 * UNIT_SPACE) + UNIT_SPACE;
        ctx.arc(pixel_x, pixel_y, cur_seg.size, 0, 2 * Math.PI);
        ctx.closePath();
        ctx.fill();

        cur_seg = cur_seg.next;
        ctx.fillStyle = this.colour;
    }
};

Snake.prototype.resolveHit = function(self, board){

}

Snake.prototype.anyHit = function(next_x, next_y){
    // Wall detection
    if (this.hitObject('wall', next_x, next_y)) {
        this.hit = 'wall';
    }
    // Food detection:
    // If the snake's movement brings it into a 'Food', 
    // instead of moving the snake, add a new snake body ontop of the Food, and make a new Food.
    else if (this.hitObject('food', next_x, next_y)) {
        this.hit = 'food';
    }
    // Only move if the snake's movement will not cause any collisions
    else if (this.hitObject('snake', next_x, next_y)) {
        this.hit = 'snake';
    } else {
        this.hit = 'unhit';
    }
}

Snake.prototype.printScore = function(ind) {
    ctx.fillStyle = "#ffffff";
    ctx.font = "20px Arial";
    ctx.fillText("Score", canvas.width - 100, canvas.height - 120);
    ctx.font = "10px Arial";

    var txt = "Player " + String(ind + 1) + ": " + String(this.length);
    ctx.fillText(txt, canvas.width - 100, canvas.height - (100 - 20 * (ind)));
};

SnakeGame.prototype.createType = function (num, type) {
    var type_arr = new Array(num);
    for (i = 0; i < num; i++) {
        switch (type){
            case ('snake'):
                o = new Snake(i % 5, true);
                break;
            case ('food'):
                o = new Food();
                break;
            default:
                console.log('Wrong type input to createType');
                break;
        }
        type_arr[i] = o;
    }
    return type_arr;
}

SnakeGame.prototype.runFrame = function (snake_arr, food_arr, self){
    board.draw();
    if (self.alive_hum == 0) {
        self.drawEndWords();
        console.log("game over");
        clearInterval(canvas.interval);
        canvas.interval = null;
        canvas.removeEventListener("click", start);
        return;
    }

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
            cur_snake.anyHit(next_x, next_y, food_arr, self);
            cur_snake.resolveHit(self, food_arr);
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
    var snake_arr = this.createType(num_snake, 'snake');
    var food_arr = this.createType(num_food, 'food');
    board.draw();
    this.drawStartWords();

    canvas.addEventListener("click", start = function (event) {
        if (canvas.interval != null) {
            console.log('paused');
            clearInterval(canvas.interval);
            canvas.interval = null;
        } else {
            console.log('resume');
            canvas.interval = setInterval(function() {SnakeGame.prototype.runFrame(snake_arr, food_arr, self)}, 1000 / 10);
        }
    });
};

/*
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
*/

console.log(4);

QLearning(2);

console.log(3);
