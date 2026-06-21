# 10: the State Pattern: The State of Things

_Extracted from PDF pages 419-462. Text only; images and diagrams are not embedded._


---

## PDF page 419

10 the State Pattern
   TheStateof Things


                                                     I thought things in Objectville were
                                                             going to be so easy, but now every time I
                                                          turn around there’s another change request
                                                       coming in. I’m at the breaking point! Oh,
                                                 maybe I should have been going to Betty’s
                                                 Wednesday night patterns group all along.
                                                          I’m in such a state!


  A little-known fact: the Strategy and State Patterns
  are twins separated at birth. You’d think they’d live similar lives,
   but the Strategy Pattern went on to create a wildly successful business around
   interchangeable algorithms, while State took the perhaps more noble path of helping
   objects to control their behavior by changing their internal state. As different as their
   paths became, however, underneath you’ll find almost precisely the same design. How
   can that be? As you’ll see, Strategy and State have very different intents. First, let’s
   dig in and see what the State Pattern is all about, and then we’ll return to explore their
   relationship at the end of the chapter.

                                                                          this is a new chapter      381


---

## PDF page 420

meet mighty gumball
  va
Jaw Breakers

Gumball machines have gone high tech. That’s right, the
major manufacturers have found that by putting CPUs
into their candy machines, they can increase sales, monitor
inventory over the network, and measure customer satisfaction
more accurately.                                                           story—                                                                            their                                                                        that’s                                          At leastBut these manufacturers are gumball machine experts, not                                                              they just got                                              we think          1800s                                                                               circa                                                                   tosoftware developers, and they’ve asked for your help:             bored with the                                                            and needed                                                                technology         their                                                                make                                                           find a way to                                                                                  exciting.                                                                jobs more

                                                                               to                                                                                  needs                                                                               controller                                                                machine                                                              gumball                                                 the                                                  think                                     we                                   way                                                                        may                                  the                                                                 We                                                                                                  us!                                  Here’s                                                                        for                                                                    Java                                                                                  in                                                                        this                                                        implement                                               you can                                             hoping                                                                              the                                      We’re                                                                               keep                                work.                                                                       to                                                                     need                                                                    you                                                                     so                                                                future,                                                   the                                                                in                                                behavior                                     more                             be adding                                  design as flexible and maintainable as possible!  Mighty Gumball, Inc.
                   Machine          the Gumball   Where                        - Mighty Gumball Engineers                 Half Empty           is Never

               of             Out                   Gumballs                                     Has          turn                                        Quarter                                               quarter                      crank
                                          insert                         quarter
                         No            eject
                                    Quarter
                                                           Gumball                                                        dispense                                                     gumball     Sold                                                      gumballs
                0                                         gumballs=0  >


382      Chapter 10


---

## PDF page 421

the state pattern

                                                 Cubicle Conversation
                                         Let’s take a look at this
                                  diagram and see what the
                                Mighty Gumball guys want...


                                 Judy: This diagram looks like a state diagram.
                                   Joe: Right, each of those circles is a state...
                               Judy: ...and each of the arrows is a state transition.
                             Frank: Slow down, you two, it’s been too long since I studied state diagrams.
                          Can you remind me what they’re all about?
                               Judy: Sure, Frank. Look at the circles; those are states. “No Quarter” is
                                 probably the starting state for the gumball machine because it’s just sitting there
                                   waiting for you to put your quarter in. All states are just different configurations
           Judy                                    of the machine that behave in a certain way and need some action to take them toFrank            Joe                           another state.
Joe: Right. See, to go to another state, you need to do something like put a quarter in the machine. See the arrow
from “No Quarter” to “Has Quarter”?
Frank: Yes...
Joe: That just means that if the gumball machine is in the “No Quarter” state and you put a quarter in, it will
change to the “Has Quarter” state. That’s the state transition.
Frank: Oh, I see! And if I’m in the “Has Quarter” state, I can turn the crank and change to the “Gumball Sold”
state, or eject the quarter and change back to the “No Quarter” state.
Judy: You got it!
Frank: This doesn’t look too bad then. We’ve obviously got four states, and I think we also have four actions: “insert
quarter,” “eject quarter,” “turn crank,” and “dispense.” But...when we dispense, we test for zero or more gumballs
in the “Gumball Sold” state, and then either go to the “Out of Gumballs” state or the “No Quarter” state. So we
actually have five transitions from one state to another.
Judy: That test for zero or more gumballs also implies we’ve got to keep track of the number of gumballs too. Any
time the machine gives you a gumball, it might be the last one, and if it is, we need to transition to the “Out of
Gumballs” state.
Joe: Also, don’t forget that you could do nonsensical things, like try to eject the quarter when the gumball machine is
in the “No Quarter” state, or insert two quarters.
Frank: Oh, I didn’t think of that; we’ll have to take care of those too.
Joe: For every possible action we’ll just have to check to see which state we’re in and act appropriately. We can do
this! Let’s start mapping the state diagram to code...

                                                                     you are here 4      383


---

## PDF page 422

review of state machines

State machines 101

How are we going to get from that state diagram to actual code? Here’s a quick
introduction to implementing state machines:

 1    First, gather up your states:
                          Has             Gumball
                            Quarter            Sold    Here are the states — four in total.             No
                             Outof                  Quarter                                          Gumballs


 2   Next, create an instance variable to hold the current state, and define values for each of the states:
    Let’s just call “Out of Gumballs”
    “Sold Out” for short.
         final static int SOLD_OUT = 0;               Here’s each state represented                                                                as a unique integer...         final static int NO_QUARTER = 1;
         final static int HAS_QUARTER = 2;
         final static int SOLD = 3;
                                                                           ...and here’s an instance variable that holds the
                                                             current state. We’ll go ahead and set it to “Sold         int state = SOLD_OUT;                                                       Out” since the machine will be unfilled when it’s
                                                                   first taken out of its box and turned on.

 3  Now we gather up all the actions that can happen in the system:
                                                    These actions are
                                                    the gumball machine’s             insert quarter      turn crank                                                             interface — the things
                      eject quarter                     you can do with it.
                                         dispense

                                                          Dispense is more of an internal
                                                           action the machine invokes on itself.      Looking at the diagram, invoking any of       these actions causes a state transition.


384      Chapter 10


---

## PDF page 423

the state pattern

 4  Now we create a class that acts as the state machine. For each action,
    we create a method that uses conditional statements to determine
     what behavior is appropriate in each state. For instance, for the
     “insert quarter” action, we might write a method like this:

     public void insertQuarter() {                                          Each possible
                                                                                            state is checked
                                                                                        with a conditional        if (state == HAS_QUARTER) {                                                                                                   statement...
            System.out.println("You can't insert another quarter");
                                                                   the appropriate                                                                            exhibits                                                                                                             state...        } else if (state == NO_QUARTER) {                ...and                                                                                                 possible                                                                  for each                                                                    behavior
            state = HAS_QUARTER;
            System.out.println("You inserted a quarter");
                                                                                          ...but can also transition to other states,
        } else if (state == SOLD_OUT) {                        just as depicted in the diagram.

            System.out.println("You can't insert a quarter, the machine is sold out");

        } else if (state == SOLD) {

            System.out.println("Please wait, we're already giving you a gumball");

        }
    }
                                             Here we’re talking
                                                 about a common technique:
                                                  modeling state within an object
                                           by creating an instance variable to hold
                                              the state values and writing conditional
                                             code within our methods to handle
                                                the various states.


With that quick review, let’s go implement the Gumball Machine!


                                                                       you are here 4      385


---

## PDF page 424

implement the gumball machine

Writing the code

It’s time to implement the Gumball Machine. We know we’re going to have an instance
variable that holds the current state. From there, we just need to handle all the actions,
behaviors, and state transitions that can happen. For actions, we need to implement
inserting a quarter, removing a quarter, turning the crank, and dispensing a gumball; we
also have the empty Gumball Machine condition to implement.
                                                   Here are the four states; theystatematchdiagram.the                                                                              Gumball’s                                                         Mighty                                                          states in
public class GumballMachine {                                       Here’s the instance variable that is going                                                                 to keep track of the current state we’re    final static int SOLD_OUT = 0;                                         in. We start in the SOLD_OUT state.
    final static int NO_QUARTER = 1;
    final static int HAS_QUARTER = 2;                    We have a second instance variable that
    final static int SOLD = 3;                                   keeps track of the number of gumballs                                                                                       in the machine.
    int state = SOLD_OUT;
    int count = 0;                                    The constructor takes an initial inventory
                                                          of gumballs. If the inventory isn’t zero,
    public GumballMachine(int count) {                   the machine enters state NO_QUARTER,
        this.count = count;                                  meaning it is waiting for someone to
        if (count > 0) {                                         insert a quarter; otherwise, it stays in                                                              the SOLD_OUT state.            state = NO_QUARTER;
        }                                     implementing                 Now we start    }                                         methods....                    the actions as
                                                       When a quarter is inserted...
                                                                                                                                   ...if a quarter is already    public void insertQuarter() {                                                                                                 inserted, we tell the        if (state == HAS_QUARTER) {                                                                                                     customer...            System.out.println("You can't insert another quarter");
        } else if (state == NO_QUARTER) {                                           ...otherwise, we accept the
            state = HAS_QUARTER;                                              quarter and transition to
            System.out.println("You inserted a quarter");               the HAS_QUARTER state.
        } else if (state == SOLD_OUT) {
            System.out.println("You can't insert a quarter, the machine is sold out");
        } else if (state == SOLD) {
            System.out.println("Please wait, we're already giving you a gumball");
        }                                If the customer just bought a                  And if the machine is sold    }                                    gumball, he needs to wait until the                    out, we reject the quarter.
                                 transaction is complete before
                                    inserting another quarter.

386      Chapter 10


---

## PDF page 425

the state pattern
    public void ejectQuarter() {        Now, if the customer tries to remove the quarter...        if (state == HAS_QUARTER) {                                                                                                                      ...if there is a quarter, we            System.out.println("Quarter returned");                 return it and go back to the
            state = NO_QUARTER;                              NO_QUARTER state...        } else if (state == NO_QUARTER) {
            System.out.println("You haven't inserted a quarter");        ...otherwise, if there isn’t
        } else if (state == SOLD) {                                             one we can’t give it back.
            System.out.println("Sorry, you already turned the crank");
        } else if (state == SOLD_OUT) {
            System.out.println("You can't eject, you haven't inserted a quarter yet");
        }
    }                                You can’t eject if the machine is sold             If the customer just
                                            out, it doesn’t accept quarters!                 turned the crank, we
                                                                                             can’t give a refund; he
                       The customer tries to turn the crank...                       already has the gumball!
    public void turnCrank() {
        if (state == SOLD) {                            Someone’s trying to cheat the machine.
            System.out.println("Turning twice doesn't get you another gumball!");
        } else if (state == NO_QUARTER) {                                                                                 We need a            System.out.println("You turned but there's no quarter");                                                                                                 quarter first.        } else if (state == SOLD_OUT) {
            System.out.println("You turned, but there are no gumballs");                                                                      We can’t deliver        } else if (state == HAS_QUARTER) {            System.out.println("You turned...");                                      gumballs; there
            state = SOLD;                                                           are none.
            dispense();                                                                             Success! They get a gumball. Change        }                                                                 the state to SOLD and call the    }                                 Called to dispense a gumball.              machine’s dispense() method.
    public void dispense() {                                                                                             We’re in the        if (state == SOLD) {                                                                                                            state; give            System.out.println("A gumball comes rolling out the slot");    SOLD                                                                                                             gumball!            count = count - 1;                                                     ’em a
            if (count == 0) {                                                                                           Here’s where we handle the                System.out.println("Oops, out of gumballs!");                                                                                “out of gumballs” condition:                state = SOLD_OUT;            } else {                                                          If this was the last one, we                state = NO_QUARTER;                                        set the machine’s state to            }                                                  SOLD_OUT; otherwise, we’re        } else if (state == NO_QUARTER) {                               back to not having a quarter.
            System.out.println("You need to pay first");
        } else if (state == SOLD_OUT) {                               None of these should ever
            System.out.println("No gumball dispensed");                happen, but if they do,        } else if (state == HAS_QUARTER) {                                                                        we give ’em an error, not            System.out.println("You need to turn the crank");                                                                             a gumball.        }
    }
    // other methods here like toString() and refill()
}

                                                                       you are here 4      387


---

## PDF page 426

test the gumball machine

In-house testing

That feels like a nice solid design using a well-thought-out methodology, doesn’t
it? Let’s do a little in-house testing before we hand it off to Mighty Gumball to
be loaded into their actual gumball machines. Here’s our test harness:

 public class GumballMachineTestDrive {                          Load it up with five
                                                                                         gumballs total.
     public static void main(String[] args) {
         GumballMachine gumballMachine = new GumballMachine(5);
                                                                       Print out the state of the machine.         System.out.println(gumballMachine);
                                                         Throw a quarter in...         gumballMachine.insertQuarter();
                                                                  Turn the crank; we should get our gumball.         gumballMachine.turnCrank();
         System.out.println(gumballMachine);              Print out the state of the machine again.
         gumballMachine.insertQuarter();              Throw a quarter in...
         gumballMachine.ejectQuarter();                 Ask for it back.
         gumballMachine.turnCrank();                    Turn the crank; we shouldn’t get our gumball.
         System.out.println(gumballMachine);           Print out the state of the machine again.
                                                       Throw a quarter in...         gumballMachine.insertQuarter();
         gumballMachine.turnCrank();                   Turn the crank; we should get our gumball.
         gumballMachine.insertQuarter();             Throw a quarter in...
                                                               Turn the crank; we should get our gumball.         gumballMachine.turnCrank();
         gumballMachine.ejectQuarter();                Ask for a quarter back we didn’t put in.
                                                                   Print out the state of the machine again.         System.out.println(gumballMachine);
         gumballMachine.insertQuarter();             Throw TWO quarters in...
         gumballMachine.insertQuarter();                                                               Turn the crank; we should get our gumball.
         gumballMachine.turnCrank();
         gumballMachine.insertQuarter();                                                    Now for the stress testing...         gumballMachine.turnCrank();
         gumballMachine.insertQuarter();
         gumballMachine.turnCrank();
         System.out.println(gumballMachine);          Print that machine state one more time.
     }
 }

388      Chapter 10


---

## PDF page 427

the state pattern


File Edit  Window Help mightygumball.com
%java GumballMachineTestDrive
Mighty Gumball, Inc.
Java-enabled Standing Gumball Model #2004
Inventory: 5 gumballs
Machine is waiting for quarter
You inserted a quarter
You turned...
A gumball comes rolling out the slot
Mighty Gumball, Inc.
Java-enabled Standing Gumball Model #2004
Inventory: 4 gumballs
Machine is waiting for quarter
You inserted a quarter
Quarter returned
You turned but there's no quarter
Mighty Gumball, Inc.
Java-enabled Standing Gumball Model #2004
Inventory: 4 gumballs
Machine is waiting for quarter
You inserted a quarter
You turned...
A gumball comes rolling out the slot
You inserted a quarter
You turned...
A gumball comes rolling out the slot
You haven't inserted a quarter
Mighty Gumball, Inc.
Java-enabled Standing Gumball Model #2004
Inventory: 2 gumballs
Machine is waiting for quarter
You inserted a quarter
You can't insert another quarter
You turned...
A gumball comes rolling out the slot
You inserted a quarter
You turned...
A gumball comes rolling out the slot
Oops, out of gumballs!
You can't insert a quarter, the machine is sold out
You turned, but there are no gumballs
Mighty Gumball, Inc.
Java-enabled Standing Gumball Model #2004
Inventory: 0 gumballs
Machine is sold out


                                                        you are here 4      389


---

## PDF page 428

gumball buying game

You knew it was coming...a change request!
Mighty Gumball, Inc., has loaded your code into their
newest machine and their quality assurance experts are
putting it through its paces. So far, everything’s looking
great from their perspective.
In fact, things have gone so smoothly they’d like to take
things to the next level...


                       We think that by turning
                                   “gumball buying” into a game we
                                  can significantly increase our
                                         sales. We’re going to put one of
                                these stickers on every machine.
                                We’re so glad we’ve got Java
                                           in the machines because this is
                                       going to be easy, right?


                                          10% of the time,  CEO, Mighty                                      when the crank
   Gumball, Inc.                                                     is turned, the                                                                 gets            or                                          customer   JawBreaker                                                two gumballs   Gumdrop?                             Gumballs                         instead of one.


390      Chapter 10


---

## PDF page 429

the state pattern

      Design Puzzle
             Draw a state diagram for a Gumball Machine that handles the 1 in 10
                contest. In this contest, 10% of the time the Sold state leads to two
                  balls being released, not one. Check your answer with ours (at the
             end of the chapter) to make sure we agree before you go further...


Mighty Gumball, Inc.
Where the Gumball Machine
      is Never Half Empty


         Use Mighty Gumball’s stationery to draw your state diagram.


                                                                    you are here 4      391


---

## PDF page 430

things get messy

The messy STATE of things...

Just because you’ve written your gumball machine using a well-thought-out
methodology doesn’t mean it’s going to be easy to extend. In fact, when you go back
and look at your code and think about what you’ll have to do to modify it, well...
       final static int SOLD_OUT = 0;               First, you’d have to add a new WINNER state
       final static int NO_QUARTER = 1;            here. That isn’t too bad...
       final static int HAS_QUARTER = 2;
       final static int SOLD = 3;

       public void insertQuarter() {
           // insert quarter code here
       }
                                                                           ...but then, you’d have to add a new conditional       public void ejectQuarter() {                                                                         in every single method to handle the WINNER           // eject quarter code here                                                                   state; that’s a lot of code to modify.       }
       public void turnCrank() {
           // turn crank code here
       }                                             turnCrank() will get especially messy, because you’d
                                                         have to add code to check to see whether you’ve
       public void dispense() {                got a WINNER and then switch to either the                                          WINNER state or the SOLD state.           // dispense code here
       }


                                       Which of the following describe the state of our implementation?
                                          (Choose all that apply.)


     ❏  A. This code certainly isn’t adhering to the ❏  D. State transitions aren’t explicit; they
             Open Closed Principle.                          are buried in the middle of a bunch of
                                                                    conditional statements.     ❏  B. This code would make a FORTRAN
               programmer proud.          ❏  E. We haven’t encapsulated anything that
                                                                         varies here.     ❏  C. This design isn’t even very object-
                   oriented.               ❏   F.  Further additions are likely to cause bugs
                                                                        in working code.


392      Chapter 10


---

## PDF page 431

the state pattern


           Okay, this isn’t good. I think
       our first version was great, but it isn’t
     going to hold up over time as Mighty Gumball
   keeps asking for new behavior. The rate of bugs
     is just going to make us look bad, not to mention
      the CEO will drive us crazy.


Frank: You’re right about that! We need to refactor this code so that it’s easy
to maintain and modify.
Judy: We really should try to localize the behavior for each state so that if we
make changes to one state, we don’t run the risk of messing up the other code.
Frank: Right; in other words, follow that ol’ “encapsulate what varies”
principle.
Judy: Exactly.
Frank:: If we put each state’s behavior in its own class, then every state just
implements its own actions.
Judy: Right. And maybe the Gumball Machine can just delegate to the state
object that represents the current state.
Frank: Ah, you’re good: favor composition...more principles at work.
Judy: Cute. Well, I’m not 100% sure how this is going to work, but I think
we’re on to something.
Frank: I wonder if this will make it easier to add new states?
Judy: I think so... We’ll still have to change code, but the changes will be
much more limited in scope because adding a new state will mean we just
have to add a new class and maybe change a few transitions here and there.
Frank: I like the sound of that. Let’s start hashing out this new design!


                                              you are here 4      393


---

## PDF page 432

a new state design

The new design

It looks like we’ve got a new plan: instead of maintaining our existing code, we’re going to
rework it to encapsulate state objects in their own classes and then delegate to the current
state when an action occurs.
We’re following our design principles here, so we should end up with a design that is easier to
maintain down the road. Here’s how we’re going to do it:

    1   First, we’re going to define a State interface that
        contains a method for every action in the Gumball
        Machine.

    2  Then we’re going to implement a State class for
        every state of the machine. These classes will be
        responsible for the behavior of the machine when it
          is in the corresponding state.
    3   Finally, we’re going to get rid of all of our conditional
       code and instead delegate the work to the State class.


Not only are we following design principles, as you’ll see, we’re actually implementing the
State Pattern. But we’ll get to all the official State Pattern stuff after we rework our code...


                                            Now we’re going
                                                     to put all the behavior of a
                                                     state into one class. That way,
                                                     we’re localizing the behavior and
                                                 making things a lot easier to
                                                 change and understand.


394      Chapter 10


---

## PDF page 433

the state pattern

Defining the State interfaces and classes

First let’s create an interface for State, which all our states implement:

                                      Here’s the interface for all states. The methods map directly                                to actions that could happen to the Gumball Machine (these
                                   are the same methods as in the previous code).


Then take each state in our design and
encapsulate it in a class that implements                                           <<interface>>
the State interface.                                                                       State
                                                                                                           insertQuarter()
                                                                                                          ejectQuarter()
                                                                                                     turnCrank()
                                                                                                    dispense()

  To figure out what
   states we need, we look
   at our previous code...                   SoldState                SoldOutState             NoQuarterState            HasQuarterState                                                       insertQuarter()                   insertQuarter()                    insertQuarter()                      insertQuarter()
                                                      ejectQuarter()                    ejectQuarter()                    ejectQuarter()                       ejectQuarter()
                                                    turnCrank()                     turnCrank()                      turnCrank()                        turnCrank()
                                                   dispense()                       dispense()                       dispense()                          dispense()


                                                                                     ...and we map each state    public class GumballMachine {                                                                            directly to a class.
        final static int SOLD_OUT = 0;
        final static int NO_QUARTER = 1;
        final static int HAS_QUARTER = 2;                                                              Don’t forget, we need a new “winner” state
        final static int SOLD = 3;                       too that implements the State interface. We’ll
                                                            come back to this after we reimplement the
                                                                          first version of the Gumball Machine.        int state = SOLD_OUT;
        int count = 0;                                                                                     WinnerState
                                                                                                                                            insertQuarter()
                                                                                                                                          ejectQuarter()
                                                                                                                                    turnCrank()
                                                                                                                                      dispense()


                                                                       you are here 4      395


---

## PDF page 434

what are all the states


                                      To implement our states, we first need to specify the behavior of the
                                             classes when each action is called. Annotate the diagram below with the
                                        behavior of each action in each class; we’ve already filled in a few for you.

              Go to HasQuarterState.                                                                                                                 NoQuarterState
                                                                                                                                                  insertQuarter()                 Tell the customer, “You haven’t inserted a quarter.”
                                                                                                                                                ejectQuarter()
                                                                                                                                          turnCrank()
                                                                                                                                           dispense()


                                                                                                                 HasQuarterState
                                                                                                                                                  insertQuarter()
           Go to SoldState.                                                                                         ejectQuarter()turnCrank()
                                                                                                                                           dispense()

       Tell the customer, “Please wait, we’re already giving you a gumball.”
                                                                                                                       SoldState
                                                                                                                                                  insertQuarter()
                                                                                                                                                ejectQuarter()

                                                                                                                                       dispense()          Dispense one gumball. Check number of gumballs; if > 0,                                turnCrank()
         go to NoQuarterState; otherwise, go to SoldOutState.


                                                                                                                  SoldOutState
               Tell the customer, “There are no gumballs.”                                                  insertQuarter()ejectQuarter()
                                                                                                                                          turnCrank()
                                                                                                                                           dispense()


                                                                                                                   WinnerState
                                                                                                                                                  insertQuarter()
                                                                                                                                                ejectQuarter()
                                                                                                                                          turnCrank()
                                                                                                                                        dispense()
                                 Go ahead and fill this out even though we’re implementing it later.


396      Chapter 10


---

## PDF page 435

the state pattern

Implementing our State classes

Time to implement a state: we know what behaviors we want; we just need to get it down in code. We’re going to
closely follow the state machine code we wrote, but this time everything is broken out into different classes.
Let’s start with the NoQuarterState:
                                                        interface.           We get passed a reference to                                    the State                               implement                               the Gumball Machine through the                First we need to                                                                                constructor. We’re just going to
                                                                                stash this in an instance variable.
  public class NoQuarterState implements State {
     GumballMachine gumballMachine;
                                                                                   If someone inserts a quarter,     public NoQuarterState(GumballMachine gumballMachine) {                                                                    we print a message saying the         this.gumballMachine = gumballMachine;                                                                               quarter was accepted and then     }                                                                                change the machine’s state to
                                                                           the HasQuarterState.     public void insertQuarter() {
         System.out.println("You inserted a quarter");
         gumballMachine.setState(gumballMachine.getHasQuarterState());    You’ll see how these
     }                                                                           work in just a sec...
     public void ejectQuarter() {
         System.out.println("You haven't inserted a quarter");          You can’t get money
     }                                                                            back if you never gave
                                                                                                     it to us!
     public void turnCrank() {
         System.out.println("You turned, but there's no quarter");
      }                                                              And you can’t get a gumball
                                                                                             if you don’t pay us.
     public void dispense() {                                                              We can’t be dispensing         System.out.println("You need to pay first");                                                                                     gumballs without payment.     }
 }

                   What we’re doing is
                     implementing the behaviors that
                      are appropriate for the state
                    we’re in. In some cases, this behavior
                          includes moving the Gumball
                      Machine to a new state.


                                                                       you are here 4      397


---

## PDF page 436

state objects in the gumball machine

Reworking the Gumball Machine

Before we finish the State classes, we’re going to rework the Gumball
Machine—that way, you can see how it all fits together. We’ll start
with the state-related instance variables and switch the code from
using integers to using state objects:


      public class GumballMachine {

          final static int SOLD_OUT = 0;
          final static int NO_QUARTER = 1;                              we update the                                                                           GumballMachine,                                                              the                                                                       In                                                                                           than                                                                                          rather                                                                                                       classes          final                static                       int                           HAS_QUARTER                                      = 2;                                                                       new                                                                      the                                                                              use                                                                to                                                               code                                                                                                                         is quite                                                                                   code                                                                    The                                                                                         integers.          final                static                       int                           SOLD = 3;                                                                              static                                                             the                                                                                                  have                                                                              we                                                                                                              class                                                                                                 in one                                                                          that                                                                        except                                                                                      similar,                                                                                                                  objects...                                                                           integers and in the other          int state = SOLD_OUT;
          int count = 0;


     Old code                                    public class GumballMachine {

                                                   State soldOutState;
                                                   State noQuarterState;
                                                   State hasQuarterState;
                                                   State soldState;
                             New code
                                                   State state = soldOutState;
                                                  int count = 0;


                                                              All the State objects are created
                                               and assigned in the constructor.                                                                                   This now holds a
                                                                               State object, not
                                                                            an integer.


398      Chapter 10


---

## PDF page 437

the state pattern

Now, let’s look at the complete GumballMachine class...
 public class GumballMachine {                                                      Here are all the States again...
     State soldOutState;                                                                               ...and the State instance variable.     State noQuarterState;
     State hasQuarterState;                                                       The count instance variable holds the count     State soldState;                                                           of gumballs — initially the machine is empty.
     State state;
     int count = 0;                                                                  Our constructor takes the initial
                                                                      number of gumballs and stores it     public GumballMachine(int numberGumballs) {                                                                                             in an instance variable.         soldOutState = new SoldOutState(this);
         noQuarterState = new NoQuarterState(this);                                                                                 It also creates the State         hasQuarterState = new HasQuarterState(this);                                                                                         instances, one of each.         soldState = new SoldState(this);
         this.count = numberGumballs;                          If there are more than 0 gumballs we
         if (numberGumballs > 0) {                             set the state to the NoQuarterState;
             state = noQuarterState;                           otherwise, we start in the SoldOutState.
         } else {
             state = soldOutState;                    Now for the actions. These are         }                                               VERY EASY to implement now. We     }                                                                            just delegate to the current state.
     public void insertQuarter() {
         state.insertQuarter();                                                               Note that we don’t need an     }                                                                              action method for dispense() in     public void ejectQuarter() {                                                                      GumballMachine because it’s just an         state.ejectQuarter();                                                                                 internal action; a user can’t ask the     }
     public void turnCrank() {                                   machine to dispense directly. But we
         state.turnCrank();                                  do call dispense() on the State object
         state.dispense();                                   from the turnCrank() method.
     }
                                                                 This method allows other objects (like
     void setState(State state) {                                                                 our State objects) to transition the         this.state = state;                                                                 machine to a different state.     }
     void releaseBall() {
         System.out.println("A gumball comes rolling out the slot...");
         if (count > 0) {                                                     The machine supports a releaseBall()             count = count - 1;                                                                       helper method that releases the ball and         }                                                              decrements the count instance variable.     }
     // More methods here including getters for each State...
 }                                   This includes methods like getNoQuarterState() for getting each
                                     state object, and getCount() for getting the gumball count.

                                                                       you are here 4      399


---

## PDF page 438

more states for the gumball machine

Implementing more states

Now that you’re starting to get a feel for how the Gumball Machine and the states
fit together, let’s implement the HasQuarterState and the SoldState classes...                                                                                                    instantiated                                                              When the state is                                                                                to the                                                                                           reference                                                          we pass it a                                                                                       This is used  public class HasQuarterState implements State {                                                                               GumballMachine.       to a                                                                                            machine      GumballMachine gumballMachine;                                                                to transition the                                                                                              state.                                                                                different
      public HasQuarterState(GumballMachine gumballMachine) {
          this.gumballMachine = gumballMachine;
      }                                                              An inappropriate                                                                                  for this                                                                                          action
      public void insertQuarter() {                                                state.
          System.out.println("You can't insert another quarter");
      }
                                                                                    Return the customer’s      public void ejectQuarter() {                                                                                        quarter and          System.out.println("Quarter returned");                                                                                                    transition back to the
          gumballMachine.setState(gumballMachine.getNoQuarterState());    NoQuarterState.
      }
      public void turnCrank() {                                        When the crank is                                                                                  turned we transition          System.out.println("You turned...");                                                                               the machine to the
          gumballMachine.setState(gumballMachine.getSoldState());      SoldState state by
      }                                                                                                  calling its setState()
                                                                            method and passing it
                                                                               the SoldState object.      public void dispense() {                                                                      The SoldState object          System.out.println("No gumball dispensed");                                                                                                                        is retrieved by the
      }                                                                               getSoldState()
 }                                                                                 getter method
                                       Another                                    (there is one of these
                                               inappropriate                              getter methods for                                             action for this                            each state).
                                                state.


400      Chapter 10


---

## PDF page 439

the state pattern


Now, let’s check out the SoldState class...                                             Here are all the
  public class SoldState implements State {                                       inappropriate                                                                                    for this     //constructor and instance variables here                                  actions
                                                                                               state.
     public void insertQuarter() {
         System.out.println("Please wait, we're already giving you a gumball");
     }

     public void ejectQuarter() {
         System.out.println("Sorry, you already turned the crank");
     }

     public void turnCrank() {
         System.out.println("Turning twice doesn't get you another gumball!");
     }
 And here’s where the
  real work begins...                                                 We’re in the SoldState, which means the
                                                                 customer paid. So, we first need to ask     public void dispense() {                                                             the machine to release a gumball.         gumballMachine.releaseBall();
         if (gumballMachine.getCount() > 0) {
             gumballMachine.setState(gumballMachine.getNoQuarterState());
         } else {
             System.out.println("Oops, out of gumballs!");
             gumballMachine.setState(gumballMachine.getSoldOutState());
         }
     }                                                Then we ask the machine what the gumball }                                                            count is, and either transition to the                                                                           or the SoldOutState.                                                           NoQuarterState


      Look back at the GumballMachine implementation. If the crank is turned and
       not successful (say the customer didn’t insert a quarter first), we call dispense()
      anyway, even though it’s unnecessary. How might you fix this?


                                                                       you are here 4      401


---

## PDF page 440

your turn to implement a state


                            We have one remaining class we haven’t implemented: SoldOutState.
                              Why don’t you implement it? To do this, carefully think through how the
                                    Gumball Machine should behave in each situation. Check your answer
                                        before moving on...

     public class SoldOutState implements _______________  {
        GumballMachine gumballMachine;

        public SoldOutState(GumballMachine gumballMachine) {

        }

        public void insertQuarter() {


        }

        public void ejectQuarter() {


        }

        public void turnCrank() {


        }

        public void dispense() {


        }
    }


402      Chapter 10


---

## PDF page 441

the state pattern

Let’s take a look at what we’ve done so far...

For starters, you now have a Gumball Machine implementation that is structurally quite
different from your first version, and yet functionally it is exactly the same. By structurally
changing the implemention, you’ve:
     Localized the behavior of each state into its own class.
    Removed all the troublesome if statements that would have been difficult to maintain.
     Closed each state for modification, and yet left the Gumball Machine open to extension
     by adding new state classes (and we’ll do this in a second).
     Created a code base and class structure that maps much more closely to the Mighty
    Gumball diagram and is easier to read and understand.
Now let’s look a little more at the functional aspect of what we did:

                                   now holds an                                 Machine                  The Gumball             class.                                   State                                                        Gumball Machine States                           instance of each


                          NoQuarter


                                                            current state

                               er         e        HasQuart     G   n       u       m  chi         ballMa


                                    Sold
                      The current state of the
                            machine is always one of
                            these class instances.

                               SoldOut


                                                                       you are here 4      403


---

## PDF page 442

state transitions

                                              is                              called, it                               is             an action       When                                                              Gumball Machine States                                    state.                         current                to the        delegated

                                             turnCrank()
                            NoQuarter

            turnCrank()                                                                        current state
                             HasQuarter
       G   e               chin        umballMa


                                        Sold
      In this case, the turnCrank()
    method is being called when the
     machine is in the HasQuarter
                                                        ut     state, so as a result the machine               SoldO
     transitions to the Sold state.

                                        TRANSITION TO SOLD STATE

                          enters           The machine                        and a                       state             the Sold                          is dispensed...                       Gumball Machine                gumball                                                      States                   gumballs                                                                  More
                                                                                                                       ....and then the
                                            dispense()     NoQuarter                                                                                          machine will
                                                                                                either go to
                                                                                    the SoldOut
                                                                                        or NoQuarter
                                                               current                             HasQuarter                                                                                            state                                                                                                 depending          e                                                                state       G                                                                                        on                                                                                       the                                                                                          number of               chin        umballMa                                                                                                  gumballs remaining
                                                                                                                   in the machine.
                                        Sold                    Sold out


                                  SoldOut


404      Chapter 10


---

## PDF page 443

the state pattern

                                      Behind the Scenes:
                                        Self-Guided Tour

Trace the steps of the Gumball Machine starting with the NoQuarter state. Also annotate the diagram with actions
and output of the machine. For this exercise you can assume there are plenty of gumballs in the machine.

  1                                             2
                                    Gumball Machine States                                                                        Gumball Machine States


                  NoQuarter                                   NoQuarter


    e        HasQuarter              e        HasQuarter Gu  mballMachin                  G                            umballMachin


                         Sold                                                   Sold


                     SoldOut                                          SoldOut


  3                                              4
                                     Gumball Machine States                                                                      Gumball Machine States


                  NoQuarter                                   NoQuarter


    e        HasQuarter              e        HasQuarter Gu  mballMachin                  G                            umballMachin


                          Sold                                                   Sold


                      SoldOut                                          SoldOut


                                                                       you are here 4      405


---

## PDF page 444

state pattern defined

The State Pattern defined

Yes, it’s true, we just implemented the State Pattern! So now, let’s take a look at what it’s all about:

           The State Pattern allows an object to alter its behavior
             when its internal state changes. The object will appear to
               change its class.

The first part of this description makes a lot of sense, right? Because the pattern encapsulates
state into separate classes and delegates to the object representing the current state, we know
that behavior changes along with the internal state. The Gumball Machine provides a good
example: when the gumball machine is in the NoQuarterState and you insert a quarter, you get
different behavior (the machine accepts the quarter) than if you insert a quarter when it’s in the
HasQuarterState (the machine rejects the quarter).
What about the second part of the definition? What does it mean for an object to “appear to
change its class”? Think about it from the perspective of a client: if an object you’re using can
completely change its behavior, then it appears to you that the object is actually instantiated from
another class. In reality, however, you know that we are using composition to give the appearance
of a class change by simply referencing different state objects.
Okay, now it’s time to check out the State Pattern class diagram:
                                                        The State interface defines a common
    The Context is the class that                                        interface for all concrete states; the
     can have a number of internal                                        states all implement the same interface,      states. In our example, the                                          so they are interchangeable.
     GumballMachine is the Context.

                             Context                                               State
                                  request()                                                         handle()


                                  state.handle()                    ConcreteStateA      ConcreteStateB
                                                                        handle()                   handle()             Many concrete                                                                                          states are                                                                                                                         possible.       Whenever the request() is      made on the Context , it                                                                            from the                                                                           handle requests         is delegated                 to the state                           ConcreteStates                                                                                                                 its                                                                                              provides      to           handle.                                                         Context. Each ConcreteState                                                   own implementation for a request. In this                                                            way, when the Context changes state, its
                                                              behavior will change as well.

406      Chapter 10


---

## PDF page 445

the state pattern


  Wait a sec; from what
I remember of the Strategy
Pattern, this class diagram is
EXACTLY the same.


    You’ve got a good eye (or you read the beginning of the chapter)!
     Yes, the class diagrams are essentially the same, but the two patterns
      differ in their intent.
    With the State Pattern, we have a set of behaviors encapsulated in
      state objects; at any time the context is delegating to one of those
      states. Over time, the current state changes across the set of state
     objects to reflect the internal state of the context, so the context’s
     behavior changes over time as well. The client usually knows very
       little, if anything, about the state objects.
    With Strategy, the client usually specifies the strategy object that
     the context is composed with. Now, while the pattern provides the
      flexibility to change the strategy object at runtime, often there is
    a strategy object that is most appropriate for a context object. For
     instance, in Chapter 1, some of our ducks were configured to fly
     with typical flying behavior (like mallard ducks), while others were
     configured with a fly behavior that kept them grounded (like rubber
     ducks and decoy ducks).
     In general, think of the Strategy Pattern as a flexible alternative to
     subclassing; if you use inheritance to define the behavior of a class,
     then you’re stuck with that behavior even if you need to change it.
    With Strategy you can change the behavior by composing with a
     different object.
    Think of the State Pattern as an alternative to putting lots of
     conditionals in your context; by encapsulating the behaviors within
      state objects, you can simply change the state object in context to
    change its behavior.


                                                  you are here 4      407


---

## PDF page 446

q&a about the state pattern


                                                              To share your states, you’ll typically assign each state to a
                                                                                    static instance variable. If your state needs to make use of                In GumballMachine, the states decide what the   Q:                                                methods or instance variables in your Context, you’ll also        next state should be. Do the ConcreteStates always                                                             have to give it a reference to the Context in each handler()        decide what state to go to next?                                                               method.

             No, not always. The alternative is to let the Context   A:                                                                                                It seems like using the State Pattern always        decide on the flow of state transitions.         Q:                                                                increases the number of classes in our designs. Look
                                                  how many more classes our GumballMachine had than
       As a general guideline, when the state transitions are fixed     the original design!
         they are appropriate for putting in the Context; however,
       when the transitions are more dynamic, they are typically                                                                            You’re right; by encapsulating state behavior        placed in the state classes themselves (for instance, in   A:                                                                                 into separate state classes, you’ll always end up with        GumballMachine the choice of the transition to NoQuarter or                                                          more classes in your design. That’s often the price you        SoldOut depended on the runtime count of gumballs).                                                             pay for flexibility. Unless your code is some “one-off”
                                                                   implementation you’re going to throw away (yeah, right),
       The disadvantage of having state transitions in the state        consider building it with the additional classes and you’ll
         classes is that we create dependencies between the state      probably thank yourself down the road. Note that often what
         classes. In our implementation of GumballMachine we tried       is important is the number of classes that you expose to
          to minimize this by using getter methods on the Context,       your clients, and there are ways to hide these extra classes
         rather than hardcoding explicit concrete state classes.         from your clients (say, by declaring them package private).

         Notice that by making this decision, you are making a           Also, consider the alternative: if you have an application
         decision as to which classes are closed for modification—       that has a lot of state and you decide not to use separate
         the Context or the state classes—as the system evolves.        objects, you’ll instead end up with very large, monolithic
                                                                           conditional statements. This makes your code hard to
           Do clients ever interact directly with the states?      maintain and understand. By using objects, you make states   Q:
                                                                                     explicit and reduce the effort needed to understand and
                                                                     maintain your code.             No. The states are used by the Context to represent   A:            its internal state and behavior, so all requests to the states
       come from the Context. Clients don’t directly change the           The State Pattern class diagram shows that State                         Q:
         state of the Context. It is the Context’s job to oversee its         is an abstract class. But didn’t you use an interface in
          state, and you don’t usually want a client changing the state    the implementation of the gumball machine’s state?
          of a Context without that Context’s knowledge.
                                                                          Yes. Given we had no common functionality to put                          A:                       If I have lots of instances of the Context in my         into an abstract class, we went with an interface. In your   Q:
         application, is it possible to share the state objects       own implementation, you might want to consider an abstract
        across them?                                                    class. Doing so has the benefit of allowing you to add
                                                            methods to the abstract class later, without breaking the
                                                                    concrete state implementations.              Yes, absolutely, and in fact this is a very common   A:         scenario. The only requirement is that your state objects do
         not keep their own internal context; otherwise, you’d need a
        unique instance per context.


408      Chapter 10


---

## PDF page 447

the state pattern

We still need to finish the Gumball 1 in 10 game

Remember, we’re not done yet. We’ve got a game to implement, but now that we’ve got the State
Pattern implemented, it should be a breeze. First, we need to add a state to the GumballMachine class:
  public class GumballMachine {
      State soldOutState;
      State noQuarterState;                                                          All you need to add here is      State hasQuarterState;                                              the new WinnerState and
      State soldState;                              initialize it in the constructor.
      State winnerState;
      State state = soldOutState;            Don’t forget you also have
      int count = 0;                           to add a getter method for
      // methods here                           WinnerState too.
  }

Now let’s implement the WinnerState class; it’s remarkably similar to the SoldState class:
  public class WinnerState implements State {
                                                                               SoldState.      // instance variables and constructor                Just like
      // insertQuarter error message
      // ejectQuarter error message                                                                  Here we release two gumballs and then      // turnCrank error message                                                                          either go to the NoQuarterState or
                                                                the SoldOutState.      public void dispense() {
          gumballMachine.releaseBall();
          if (gumballMachine.getCount() == 0) {
              gumballMachine.setState(gumballMachine.getSoldOutState());
          } else {                                                                     If we have a second gumball, we release it.              gumballMachine.releaseBall();
              System.out.println("YOU'RE A WINNER! You got two gumballs for your quarter");
              if (gumballMachine.getCount() > 0) {                                                                                                    If we were able                  gumballMachine.setState(gumballMachine.getNoQuarterState());                                                                                           to release two             } else {                                                                                                                  gumballs, we let                  System.out.println("Oops, out of gumballs!");                                                                                           the user know                  gumballMachine.setState(gumballMachine.getSoldOutState());                                                                                            he was a winner.             }
          }
      }
  }

                                                                       you are here 4      409


---

## PDF page 448

implementing the 1 in 10 game

Finishing the game

We’ve got just one more change to make: we need to implement the random
chance game and add a transition to the WinnerState. We’re going to add both to
the HasQuarterState since that’s where the customer turns the crank:
                                                                                           First we add a   public class HasQuarterState implements State {                                                                              random number       Random randomWinner = new Random(System.currentTimeMillis());             to                                                                                         generator
       GumballMachine gumballMachine;                                            generate the 10%
                                                                                        chance of winning...
       public HasQuarterState(GumballMachine gumballMachine) {
           this.gumballMachine = gumballMachine;
       }

       public void insertQuarter() {
           System.out.println("You can't insert another quarter");
       }

       public void ejectQuarter() {
           System.out.println("Quarter returned");
           gumballMachine.setState(gumballMachine.getNoQuarterState());
                                                                                                                ...then we determine       }                                                                                                      if this customer won.
       public void turnCrank() {
           System.out.println("You turned...");
           int winner = randomWinner.nextInt(10);
           if ((winner == 0) && (gumballMachine.getCount() > 1)) {
               gumballMachine.setState(gumballMachine.getWinnerState());
          } else {
               gumballMachine.setState(gumballMachine.getSoldState());
          }                                                                            If they won, and there’s enough gumballs
       }                                                                 left for them to get two, we go to
                                                                         WinnerState; otherwise, we go to
       public void dispense() {                                 SoldState (just like we always did).
           System.out.println("No gumball dispensed");
       }
  }

Wow, that was pretty simple to implement! We just added a new state to the GumballMachine
and then implemented it. All we had to do from there was to implement our chance game and
transition to the correct state. It looks like our new code strategy is paying off...

410      Chapter 10


---

## PDF page 449

the state pattern

Demo for the CEO of Mighty Gumball, Inc.

The CEO of Mighty Gumball has dropped by for a demo of your new gumball game code. Let’s
hope those states are all in order! We’ll keep the demo short and sweet (the short attention span of
CEOs is well documented), but hopefully long enough so that we’ll win at least once.
                                        This code really hasn’t changed at all;                                  we just shortened it a bit.

   public class GumballMachineTestDrive {                      Once, again, start with a gumball
                                                                         machine with 5 gumballs.
       public static void main(String[] args) {
           GumballMachine gumballMachine = new GumballMachine(5);

           System.out.println(gumballMachine);

           gumballMachine.insertQuarter();                                                            We want to get a winning state,
           gumballMachine.turnCrank();                             so we just keep pumping in those
                                                                            quarters and turning the crank. We
                                                                                print out the state of the gumball           System.out.println(gumballMachine);                                                                           machine every so often...
           gumballMachine.insertQuarter();
           gumballMachine.turnCrank();
           gumballMachine.insertQuarter();
           gumballMachine.turnCrank();

           System.out.println(gumballMachine);
       }
   }

                                                  team is waiting                                                       engineering                               The whole                                                     room to see                                                    conference                                          outside the                                                      Pattern-based                                         if the new State                                           design is going to work!!


                                                                       you are here 4      411


---

## PDF page 450

testing the gumball machine


                                                                   File Edit  Window Help Whenisagumballajawbreaker?
           Yes! That rocks!         %java GumballMachineTestDrive
                              Mighty Gumball, Inc.
                              Java-enabled Standing Gumball Model #2004
                              Inventory: 5 gumballs
                              Machine is waiting for quarter
                              You inserted a quarter
                              You turned...
                              A gumball comes rolling out the slot...
                              A gumball comes rolling out the slot...
                              YOU'RE A WINNER! You got two gumballs for your quarter
                              Mighty Gumball, Inc.
                              Java-enabled Standing Gumball Model #2004
                              Inventory: 3 gumballs
                              Machine is waiting for quarter
                              You inserted a quarter
              Gee, did we get lucky  You turned...             or what? In our demo  A gumball comes rolling out the slot...
             to the CEO, we won   You inserted a quarter
              not once, but twice!   You turned...                              A gumball comes rolling out the slot...
                              A gumball comes rolling out the slot...
                              YOU'RE A WINNER! You got two gumballs for your quarter
                              Oops, out of gumballs!
                              Mighty Gumball, Inc.
                              Java-enabled Standing Gumball Model #2004
                              Inventory: 0 gumballs
                              Machine is sold out
                              %


    Why do we need the WinnerState? Couldn’t we just have the SoldState dispense two gumballs?Q:

      That’s a great question. SoldState and WinnerState are almost identical, except that WinnerState dispenses twoA:gumballs instead of one. You certainly could put the code to dispense two gumballs into SoldState. The downside is, of
course, that now you’ve got TWO states represented in one State class: the state in which you’re a winner, and the state
 in which you’re not. So you are sacrificing clarity in your State class to reduce code duplication. Another thing to consider
 is the principle you learned in the previous chapter: the Single Responsibility Principle. By putting the WinnerState
 responsibility into the SoldState, you’ve just given the SoldState TWO responsibilities. What happens when the
promotion ends? Or the stakes of the contest change? So, it’s a tradeoff and comes down to a design decision.


412      Chapter 10


---

## PDF page 451

the state pattern


                                                   Bravo! Great job,
                                                      gang. Our sales are already
                                                 going through the roof with the new
                                             game. You know, we also make soda
                                              machines, and I was thinking we could put
                                            one of those slot-machine arms on the
                                                side and make that a game too. We’ve got
                                                 four-year-olds gambling with the
                                              gumball machines; why stop there?


Sanity check...

Yes, the CEO of Mighty Gumball probably needs a sanity check, but that’s not what
we’re talking about here. Let’s think through some aspects of the GumballMachine
that we might want to shore up before we ship the gold version:

            We’ve got a lot of duplicate code in the Sold and Winning
             states and we might want to clean those up. How would we
         do it? We could make State into an abstract class and build
            in some default                         behavior                                        for                                       the methods;                                                           after all,                                                               error
           messages                           like, “You                              already                                        inserted                                         a quarter,”                                                               aren’t                                                            going         Dammit Jim,
            to be seen by the customer. So all “error response” behavior            I’m a gumball           could be generic and inherited from the abstract State class.            machine, not a                                                                             computer!
           The dispense() method always gets called, even if the crank is
           turned when there is no quarter. While the machine operates
            correctly and doesn’t dispense unless it’s in the right state, we
           could easily fix this by having turnCrank() return a boolean
           or by introducing exceptions. Which do you think is a better
            solution?
            All of the intelligence for the state transitions is in the State
              classes. What problems might this cause? Would we want to
         move that logic into the GumballMachine? What would be
           the advantages and disadvantages of that?
            Will you be instantiating a lot of GumballMachine objects?
               If so, you may want to move the state instances into static
            instance variables and share them. What changes would this
            require to the GumballMachine and the States?


                                                                       you are here 4      413


---

## PDF page 452

fireside chats: state and strategy


                                            Tonight’s talk: A Strategy and State Pattern Reunion.


Strategy:                                                 State:
Hey, bro. Did you hear I was in Chapter 1?
                                                            Yeah, word is definitely getting around.
I was just over giving the Template Method guys a
hand—they needed me to help them finish off their
chapter. So, anyway, what is my noble brother up to?

                                                Same as always—helping classes to exhibit different
                                                               behaviors in different states.I don’t know, you always sound like you’ve just
copied what I do and you’re using different words
to describe it. Think about it: I allow objects to
incorporate different behaviors or algorithms
through composition and delegation. You’re just
copying me.

                                                                             I admit that what we do is definitely related, but my
                                                                      intent is totally different than yours. And the way I
                                                               teach my clients to use composition and delegation
Oh yeah? How so? I don’t get it.                                                is totally different.


                                                                   Well, if you spent a little more time thinking about
                                                           something other than yourself, you might. Anyway,
                                                                  think about how you work: you have a class you’re
                                                                       instantiating and you usually give it a strategy object
                                                                     that implements some behavior. Like, in Chapter 1
                                                        you were handing out quack behaviors, right? Real
                                                            ducks got a real quack; rubber ducks got a quack
Yeah, that was some fine work...and I’m sure you can               that squeaked.
see how that’s more powerful than inheriting your
behavior, right?

                                                                     Yes, of course. Now, think about how I work; it’s
                                                                            totally different.Sorry, you’re going to have to explain that.


414      Chapter 10


---

## PDF page 453

the state pattern


Strategy:                                                 State:
                                                          Okay, when my Context objects get created, I may
                                                                                          tell them the state to start in, but then they change
                                                                        their own state over time.
Hey, come on, I can change behavior at runtime
too; that’s what composition is all about!
                                                          Sure you can, but the way I work is built around
                                                                       discrete states; my Context objects change state
                                                               over time according to some well-defined state
                                                                          transitions. In other words, changing behavior is
                                                                           built in to my scheme—it’s how I work!

Well, I admit, I don’t encourage my objects to have
a well-defined set of transitions between states. In
fact, I typically like to control what strategy my
objects are using.
                                                           Look, we’ve already said we’re alike in structure, but
                                                        what we do is quite different in intent. Face it, the
                                                            world has uses for both of us.

Yeah, yeah, keep living your pipe dreams, brother.
You act like you’re a big pattern like me, but check
it out: I’m in Chapter 1; they stuck you way out in
Chapter 10. I mean, how many people are actually
going to read this far?
                                                       Are you kidding? This is a Head First book and
                                                 Head First readers rock. Of course they’re going to
                                                                    get to Chapter 10!

That’s my brother, always the dreamer.


                                                                       you are here 4      415


---

## PDF page 454

refill exercise

We almost forgot!


                                                                                                         spec...we                                                                                                 original                                                                     the                                                                put in                                                             to                                                          forgot                                               we                                          one transition                                                                                                      gumballs!                                                                         of                                     There’s                                                                             out                                                                                                         it’s                                                                  when                                                                  machine                                                                gumball                                           to refill the                                                                                        did such                                                                               You                                   need a way                                                                                      us?                                                                           for                                                                                      it                                                                    implement                                                              you                                                    diagram — can                                         new                                       the                                         Here’s                                                         rest of the gumball machine we have no doubt                                           on the                                            job                              a good                         Inc.               Gumball,       Mighty                                    you can add this in a jiffy!                   Gumball Machine          Where the                     is Never Half Empty                 - The Mighty Gumball Engineers
                                                refill
                   of                  Out                          Gumballs                                          Has          turn                                             Quarter                                                        quarter                      crank
                                                  insert                          quarter
                             No            eject
                                         Quarter
                                                                 Gumball                                                               dispense                                                            gumball     Sold                                                               gumballs
                  0                                                   gumballs=0  >


416      Chapter 10


---

## PDF page 455

the state pattern


We need you to write the refill() method for the Gumball machine.  It has one
argument—the number of gumballs you’re adding to the machine—and
should update the gumball machine count and reset the machine’s state.


          You’ve done some amazing work!
           I’ve got some more ideas that
         are going to change the gumball
          industry and I need you to implement
         them. Shhhhh! I’ll let you in on these
          ideas in the next chapter.


                                         you are here 4      417


---

## PDF page 456

who does what?


                  Match each pattern with its description:

           Pattern              Description

                                                   Encapsulate interchangeable
                   State                                                   behaviors and use delegation to
                                                decide which behavior to use.

                                                   Subclasses decide how
                   Strategy                                                            to implement steps in an
                                                     algorithm.

                                                   Encapsulate state-based
                 Template Method                                                  behavior and delegate
                                                  behavior to the current state.


418      Chapter 10


---

## PDF page 457

the state pattern

        Tools for your Design Toolbox
                    It’s the end of another chapter; you’ve got enough
               patterns here to breeze through any job interview!               The State Pattern allows an
                                                                                                object to have many different
                                                                                        behaviors that are based on
                                                                                                                               its internal state.
                                                               Unlike a procedural state                Basics        OO
                             Abstraction                                             machine,representstheeachStatestatePatternas a     Principles OO                                                                                                     full-blown class.           what varies.           Encapsulation  Encapsulate
                                                              The                                                                                          Context gets                                                                                                                                                       its                                                                                                            behavior                          inheritance.   Polymorphism  Favor composition over                                                                                by delegating                                                                                                                     to the                                                                                                                    current
         to interfaces, not         Inheritance                                                   state object it is composed   Program    implementations.                                                                                     with.                              designs                     coupled                loosely     Strive for                 that interact.                                          By encapsulating each state             objects     between                               extension                                                                   into a class, we localize any               be open for             should                                                                               changes                                                                                                                that will need to be      Classes              for modification.                                                          this     but closed                                                                            made.                                                          principles                                                     you                  Do not          No new                                                              gives           on abstractions.                       That      Depend                               classes.                   chapter.                                                     them.            The State and Strategy                concrete       depend on                                     to sleep on                                      time                                     Patterns have the same class                           friends.                                                                                       diagram, but they differ in        Only talk to your
                                                                                                             intent.        Don’t call us, we’ll call you.                                  reason                                                              The Strategy Pattern typically                     have only one                 should     A class                                                             Here’s our new              configures Context classes        to change.                                                         pattern. If you’re           with a behavior or algorithm.                                                       managing state in
                                                              The State Pattern allows                                             a class, the State
                                                     Pattern gives you         a Context to change its
                                                                                         behavior                                                                                        as                                                                                                       the                                                                                                                  state                                                                                                                             of                                                                                                                   the                                   algorithms,   Patterns                     of                                                            technique for                                             aOO                       family             a                      one-to-many               a              defines      -                                                                                      Context                                                                                           changes.                defines         -                          them                                                              that                              an                           that                             additional                          so                                                              encapsulating Strategy                  and                              Provide                  -                 Attach                  one,           -                       makesobjects   Observer                               an            each                                    algorithm                                  dynamically.                                     its                              Define             between                          the                   -              Factory                                      all                           of                            lets                                         one  encapsulates                        object    Decorator                                                              state.                                       has                                                                                        state,                 an                                                                                           State                                                                                                             transitions                                                                                             can                                                                                             be                                 families    dependency               to                 Strategy                                        only                                  but                                              it.      Abstract             Method                   changes                                   use                                       class                     a                      creating                                    object,                           that                         an             object               for        Factory                            updated       responsibilities                         Ensure                             flexible   interchangeable.                                 without                            clients        one               -                                 of                                           request               a                          a                      and                         creating                from    when                                        point         interface                                                                                                  controlled                                                                                         by                                                                                                         the                                                                                                           State                            objects                                to                 for                 provide                                      global                                 extending                                        class                     a           Singleton              are                 -                  depedentnotified                         forEncapsulates            interface                                             request                            which             or                           a      Decoratorsindependently   vary                          provide                                      you                                       classes.                       decide                  and     dependents                       subclassing         related                                       letting                                                                                         classes                                                                                                        or                                                                                          by                                                                                                         the                                                                                                      Context              to                                         lets          Command                                Encapsulates                       concrete                  -               instance                 subclasses                           thereby                   their           let                         Method                                              requestyou       alternative                            a                        object,                                          letting                           it.                                         different             Adapter                      Factory      automatically                an           specifying                to               as                                                           its                                 the                                                                                              classes.                              thereby                                  Encapsulates               access                             towith                   -                                                   alter                                  clients                                           you                                      to              instantiate.                          object,                                            different        functionality.                                      and                 as                                             lettingobject                                   with               Facadean                           instantiation                               an                                          requests,                 parameterize                                     clients                 defer                                 thereby                                                          changes.                                  log                                 Allow                    -                         or                                        and                class                                               state        a                             object,                                               different                         queue                                                                             Statean                                                                                   Using                                                                                                  the                                                                                                     State                                                                                                            Pattern                                                                                                                                                         will                   as                                            requests,                    parameterize                                             internalwith                                     log                                        its                    requests,                           or                                        clients                                                          its                                      operations.                            when                                          and                            queue               subclasses.                                              change                                    to                          undoable                          behavior                                                requests,                       parameterize                       requests,                                                                                                            typically                                                                                                                  result                                                                                                                              in                                                                                          a                                                                                                                 greater                                        log                                      appear                                         operations.                  support                              or                                           will                              queue                            undoable                             object                   The                          requests,                     support                                                                           number                                                                                                               of                                                                                                   classes                                                                                                                                   in                                                                                                           your                                            operations.                               undoable                       supportclass.                                                             design.
                                                               State classes may be shared
                                                                     among Context instances.


                                                                     you are here 4      419


---

## PDF page 458

exercise solutions

         Design Puzzle Solution
                  Draw a state diagram for a Gumball Machine that handles the 1-in-10
                       contest. In this contest, 10% of the time the Sold state leads to two
                         balls being released, not one. Here’s our solution.


                                                  Winner            2
    Mighty Gumball, Inc.                                             dispense                                                      turn     Where the Gumball Machine                gumballs = 0                                               gumballs              is Never Half Empty                                        have                             acrank,                                            we
                0                >                         winner!
                      of                  gumballs                    Out                             Gumballs                                                Has        turn
                                                    Quarter           crank,                                                              quarter               no
                                                                            winner                                                        insert                                                                                           quarter
                                  No            eject
                                               Quarter
                                                                      Gumball                                                                    dispense                                                                 gumball     Sold                                                                       gumballs
                    0                                                          gumballs=0  >


420      Chapter 10


---

## PDF page 459

the state pattern


                              Which of the following describe the state of our implementation?
                                (Choose all that apply.) Here’s our solution.


  ❏  A. This code certainly isn’t adhering to the ❏  D. State transitions aren’t explicit; they
         Open Closed Principle.                          are buried in the middle of a bunch of
                                                              conditional statements.  ❏  B. This code would make a FORTRAN
          programmer proud.          ❏  E. We haven’t encapsulated anything that
                                                                   varies here.  ❏  C. This design isn’t even very object-
             oriented.               ❏   F.  Further additions are likely to cause bugs
                                                                  in working code.


                        We have one remaining class we haven’t implemented: SoldOutState. Why
                                    don’t you implement it? To do this, carefully think through how the Gumball
                               Machine should behave in each situation. Here’s our solution.
                                                                      we really                                                                                             state,                                                                       In the Sold Out                                                                                                    until someone                                                                                  anythingpublic class SoldOutState implements State {                  can’t do                                                                                         Machine.    GumballMachine gumballMachine;                               the Gumball                                                                                          refills
    public SoldOutState(GumballMachine gumballMachine) {
        this.gumballMachine = gumballMachine;
    }
    public void insertQuarter() {
        System.out.println("You can't insert a quarter, the machine is sold out");
    }
    public void ejectQuarter() {
        System.out.println("You can't eject, you haven't inserted a quarter yet");
    }
    public void turnCrank() {
        System.out.println("You turned, but there are no gumballs");
    }
    public void dispense() {
        System.out.println("No gumball dispensed");
    }
}


                                                                  you are here 4      421


---

## PDF page 460

exercise solutions


                                      To implement the states, we first need to define what the behavior will
                                  be when the corresponding action is called. Annotate the diagram below
                                       with the behavior of each action in each class; here’s our solution.
               Go to HasQuarterState.
                       Tell the customer, “You haven’t inserted a quarter.”                             NoQuarterState                                                                                                                                                  insertQuarter()
                      Tell the customer, “You turned, but there’s no quarter.”                            ejectQuarter()turnCrank()
                       Tell the customer, “You need to pay first.”                                             dispense()

                    Tell the customer, “You can’t insert another quarter.”
                                                                                                                 HasQuarterState
                 Give back quarter, go to NoQuarter state.                                                    insertQuarter()
             Go to SoldState.                                                                                           ejectQuarter()                                                                                                                                          turnCrank()
                    Tell the customer, “No gumball dispensed.”                                                    dispense()

            Tell the customer, “Please wait, we’re already giving you a gumball.”
             Tell the customer, “Sorry, you already turned the crank.”                                     SoldState                                                                                                                                                  insertQuarter()
                                                                                                                                                ejectQuarter()             Tell the customer, “Turning twice doesn’t get you another gumball.”                                                                                                                                          turnCrank()
                                                                                                                                        dispense()          Dispense one gumball. Check number of gumballs; if > 0, go
         to NoQuarter state; otherwise, go to SoldOut state.

              Tell the customer, “The machine is sold out.”
             Tell the customer, “You haven’t inserted a quarter yet.”                                   SoldOutState
                   Tell the customer, “There are no gumballs.”                                                      insertQuarter()ejectQuarter()
                                                                                                                                          turnCrank()
                     Tell the customer, “No gumball dispensed.”                                                  dispense()

             Tell the customer, “Please wait, we’re already giving you a gumball.”
             Tell the customer, “Sorry, you already turned the crank.”                                   WinnerState                                                                                                                                                  insertQuarter()
                                                                                                                                                ejectQuarter()             Tell the customer, “Turning twice doesn’t get you another gumball.”                                                                                                                                          turnCrank()
                                                                                                                                        dispense()          Dispense two gumballs. Check number of gumballs; if > 0,
          go to NoQuarter state; otherwise, go to SoldOutState.


422      Chapter 10


---

## PDF page 461

the state pattern

                                   Behind the Scenes:
                                     Self-Guided Tour
                  delegates to                    Solution
                 current state
      1                                        2
                              insertQuarter()                                                                            delegates                                              Gumball Machine States                                                                                                                              Gumball Machine States

                                                                                                                turnCrank()
                      NoQuarter                              NoQuarter                                  state
                              currentinsertQuarter()                                                                      turnCrank()                                                                                                                                    current state
       e        HasQuarter           e        HasQuarter   Gu    mballMachin               G                           umballMachin
                                                       machine actionmachine action
                               Sold                                            Sold


                          SoldOut                                     SoldOut
                                                                 transitions to
                                                       HasQuarter state
                                                                                                             transitions to
                                                                                                   Sold state


      3                                        4
                                               Gumball Machine States                                                           Gumball Machine States


                                                                               oQuarter                               dispense()     NoQuarter                              N                                                                                                                    state
                                                                                                                      current


                           er       ecurrent      HasQuart   Gu                     e        HasQuarter    mballMachin     state            G                           umballMachin

 Here the machine                 Sold                                            Sold
  gives out a gumball
 by calling the internal                          SoldOut                ...and then transitions             SoldO  dispense() action...                                                                                       ut
                                                       to NoQuarter.


                                                                     you are here 4      423


---

## PDF page 462

exercise solutions


                     SOlUTion

                    Match each pattern with its description:

           Pattern              Description

                                                   Encapsulate interchangeable
                   State                                                   behaviors and use delegation to
                                                decide which behavior to use.

                                                   Subclasses decide how
                   Strategy                                                            to implement steps in an
                                                     algorithm.

                                                   Encapsulate state-based
                 Template Method                                                  behavior and delegate
                                                  behavior to the current state.


                                      To refill the Gumball Machine, we add a refill() method to the State interface,
                                     which each State must implement. In every state except SoldOutState, the
                                 method does nothing. In SoldOutState, refill() transitions to NoQuarterState.
                             We also add a refill() method to GumballMachine that adds to the count of
                                         gumballs, and then calls the current state’s refill() method.
 public void refill() {                                                                      We add this method to     gumballMachine.setState(gumballMachine.getNoQuarterState());                                                                                the SoldOutState...
 }
                                                                  ...and add this method to void refill(int count) {                                                 the GumballMachine class.
     this.count += count;
      System.out.println("The gumball machine was just refilled; its new count is: " + this.count);
     state.refill();
 }


424      Chapter 10
