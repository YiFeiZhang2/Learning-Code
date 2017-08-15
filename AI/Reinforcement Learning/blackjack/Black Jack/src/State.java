
// An Ace is 1, but can be 11 if that does not make the hand bust
// State S is a specific state of the dealer's shown card, player's value, and whether they have a usable ace
// Action A is either True (hit) or False (stay)
class State {
	/* card is the dealer's shown card
	 * val is the total value of the player's hand
	 * usable is whether the player has a usable ace
	 */
	int card;
	int val;
	boolean usable;
	
	State (int card, int val, boolean usable){
		this.card = card;
		this.val = val;
		this.usable = usable;
	}
	
	@Override
	public boolean equals(Object o) {
		if (!(o instanceof State)) {
			return false;
		}
		State s = (State) o;
		return (this.card == s.card && this.val == s.val && this.usable == s.usable);
	}
	
	@Override
	public int hashCode() {
		String x = Integer.toString(this.card) + Integer.toString(this.val) 
				+ Boolean.toString(this.usable);
		return x.hashCode();
	}
	
	State (Hand playerHand, Hand dealerHand){
		this.card = dealerHand.total;
		this.val = playerHand.value();
		this.usable = playerHand.hasUsableAce();
	}
	
	// True is the player, False is the dealer
	// Return the hand for the player or dealer consistent with the current state
	// The dealer's hidden card is just assumed to have not been dealt
	public Hand getHand (boolean player){
		Hand hand;
		if (player) {
			int total = this.val;
			if (usable) {
				total = this.val - 10;
			}
			hand = new Hand(total, usable);
		} else {
			hand = new Hand(card, (card == 1));
		}
		return hand;
	}
}

// Hand represents either player's hand
class Hand {
	/* cards is a list of cards in hand
	 * total is the sum of cards (Ace is 1)
	 * ace represents whether the hand has an ace or not
	 */
	int total;
	boolean ace;
	
	Hand (){
		this.total = 0;
		this.ace = false;
	}
	
	Hand (int total, boolean hasAce){
		this.total = total;
		this.ace = hasAce;
	}
	
	public void printH() {
		if (ace)
			System.out.println("The total is " + this.total + " and a usable ace");
		else
			System.out.println("The total is " + this.total + " and no usable ace");
	}
	
	public void addCard (int card){
		this.total += card;
		if (card == 1){
			this.ace = true;
		}
	}
	
	public boolean hasUsableAce (){
		return (this.ace && (this.total + 10 <= 21));
	}
	
	public int value (){
		if (this.hasUsableAce()){
			return (this.total+10);
		} else {
			return this.total;
		}
	}
}

class StateActionPair {
	State state;
	boolean action;
	
	StateActionPair(State state, boolean action) {
		this.state = state;
		this.action = action;
	}
	
	public void printSAP() {
		System.out.println(state.card + " " + state.val + " " + state.usable + " " + this.action); 
	}
	
	@Override
	public int hashCode() {
	    String x = Integer.toString(this.state.card) + Integer.toString(this.state.val) 
	    			+ Boolean.toString(this.state.usable) + Boolean.toString(this.action);
	    return x.hashCode();
	}
	
	@Override
	public boolean equals(Object o) {
		if (!(o instanceof StateActionPair)) {
			return false;
		}
		StateActionPair sap = (StateActionPair) o;
		return (this.action == sap.action && this.state.equals(sap.state));
	}
}
