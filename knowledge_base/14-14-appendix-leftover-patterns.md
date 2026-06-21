# 14: appendix: Leftover Patterns

_Extracted from PDF pages 635-654. Text only; images and diagrams are not embedded._


---

## PDF page 635

Appendix14
  LeftoverPatterns


     Not everyone can be the most popular. A lot has changed
          in the last 25+ years. Since Design Patterns: Elements of Reusable Object-
        Oriented Software first came out, developers have applied these patterns
       thousands of times. The patterns we summarize in this appendix are full-
         fledged, card-carrying, official GoF patterns, but aren’t used as often as the
        patterns we’ve explored so far. But these patterns are awesome in their own
          right, and if your situation calls for them, you should apply them with your
       head held high. Our goal in this appendix is to give you a high-level idea of
       what these patterns are all about.


                                                                          this is a new chapter      597


---

## PDF page 636

bridge pattern

Bridge
Use the Bridge Pattern to vary not only your
implementations, but also your abstractions.                                                                   This is an abstraction. It could be                                                              an interface or an abstract class.A scenario
Imagine you’re writing the code for a new
ergonomic and user-friendly remote control for
TVs. You already know that you’ve got to use
good object-oriented techniques because while
the remote is based on the same abstraction, there
                                                                                                              RemoteControl
will be lots of implementations—one for each model     Every remote has the                on()
of TV.                                          same abstraction.                              off()
                                                                                                                                         setChannel()
                                                                                                                                                                                                                                            // more methods


                                                                                                RCAControl                SonyControl
                                      Lots of                                      on()                                on()
                                                                                                                                                                    off()                                         off()                                               implementations,
                                                                                                                         setChannel()                      setChannel()                                           one for each TV.                                                                                                                                                                                                               // more methods                                // more methods


                                                                               {
                                                                                   tuneChannel(channel);
Your dilemma                                                                }

You know that the remote’s user interface won’t be right the
first time. In fact, you expect that the product will be refined
many times as usability data is collected on the remote
control.                                                                    Using this design we can vary                                                                                           notSo your dilemma is that the remotes are going to change and                                                                                 only the TV implementation,
the TVs are going to change. You’ve already abstracted the user                                                                   the user interface.
interface so that you can vary the implementation over the many
TVs your customers will own. But you are also going to need
to vary the abstraction because it is going to change over time as
the remote is improved based on the user feedback.

So how are you going to create an object-oriented design that
allows you to vary the implementation and the abstraction?


598      Appendix


---

## PDF page 637

leftover patterns

Why use the Bridge Pattern?

The Bridge Pattern allows you to vary the implementation and
the abstraction by placing the two in separate class hierarchies.
                                                                               Implementation class hierarchy.                                    The relationship between    Abstraction                                          the two is referred to as     class hierarchy.                                          the “bridge.”

                   RemoteControl                          Has-A                                        TV
                    implementor
                       on()                                                                                                                                  on()
                            off()                                                                                                                                                                     off()
                    setChannel()                    implementor.tuneChannel(channel);               tuneChannel()
                                    // more methods                                                                                                                                                                                            // more methods

                                            All methods in the abstraction
                                      are implemented in terms of                 RCA                    Sony                  ConcreteRemote             the implementation.                      currentStation                                                                                                       on()                                on()
                                                                                                                                                                               off()                                         off()
                       on()                                                                                                                       tuneChannel()                  tuneChannel()
                            off()
                     setChannel()               setChannel(currentStation + 1);                      // more methods                                // more methods
                    nextChannel()
                     previousChannel()
                                    // more methods                                                         Concrete subclasses are implemented in terms of the
                                                                 abstraction, not the implementation.


Now you have two hierarchies, one for the remotes and a separate one for platformspecific TV implementations. The bridge allows you to vary either side of the two
hierarchies independently.


 Bridge Benefits                                  Bridge Uses and Drawbacks
   Decouples an implementation so that it is not bound             Useful in graphics and windowing systems that need
     permanently to an interface.                                             to run over multiple platforms.
    Abstraction and implementation can be extended               Useful any time you need to vary an interface and an
      independently.                                                   implementation in different ways.
   Changes to the concrete abstraction classes don’t              Increases complexity.
       affect the client.


                                                                       you are here 4      599


---

## PDF page 638

builder pattern

Builder
Use the Builder Pattern to encapsulate the construction of
a product and allow it to be constructed in steps.
A scenario
You’ve just been asked to build a vacation planner for Patternsland, a new theme
park just outside of Objectville. Park guests can choose a hotel and various types of
admission tickets, make restaurant reservations, and even book special events. To create
a vacation planner, you need to be able to create structures like this:
                                                                 Each vacation is planned
                                                                            over some number of days.


                           Vacation


                                               ee        DayOne               DayTwo               DayThr


                          t                                               t
                              kTickets SpecialEven                                     Dining     ParkTickets  Hotel  SpecialEven   Hotel ParkTickets Dining      Hotel Par


                                                                                            nsr
                            Ice                                                             atte                          Patternson                                               CirqueDuP                                               Dinner                  Dinner
                                                  Each day can have any combination                                                of hotel reservations, tickets,
                                                                  meals, and special events.


You need a flexible design
Each guest’s planner can vary in the number of days and types of activities it includes.
For instance, a local resident might not need a hotel, but wants to make dinner and
special event reservations. Another guest might be flying into Objectville and needs a
hotel, dinner reservations, and admission tickets.

So, you need a flexible data structure that can represent guest planners and all their
variations; you also need to follow a sequence of potentially complex steps to create the
planner. How can you provide a way to create the complex structure without mixing it
with the steps for creating it?

600      Appendix


---

## PDF page 639

leftover patterns

Why use the Builder Pattern?

Remember Iterator? We encapsulated the iteration into a separate
object and hid the internal representation of the collection from the
client. It’s the same idea here: we encapsulate the creation of the
trip planner in an object (let’s call it a builder), and have our client
ask the builder to construct the trip planner structure for it.                  The client uses an
                                                                               abstract interface to
                                                                                           build the planner.


                                                     builder
                                                                   AbstractBuilder    The Client directs    Client
                              constructPlanner()                        buildDay()     the builder to
                                                                        addHotel()      construct the
      planner.                                                       addReservation()                                                                      addSpecialEvent()
                                                                         addTickets()
                                                                        getVacationPlanner()
                                                                     The concrete builder          builder.buildDay(date);          builder.addHotel(date, "Grand Facadian");                                           creates real products          builder.addTickets("Patterns on Ice");                                       and stores them in                                                                                                       composite                                                                               the vacation
           // plan rest of vacation                              VacationBuilder                   structure.                                                                        vacation
          Planner yourPlanner =
                  builder.getVacationPlanner();                     buildDay()
                                                                        addHotel()
                                                                      addReservation()
                                                                      addSpecialEvent()
                                                                          addTickets()                                   create                            to                   the builder                                                                        getVacationPlanner()         Client directs   The                              and                      of steps                  in a number    the planner                   getVacationPlanner()             the            calls     then                     the complete object.                 retrieve           to     method

 Builder Benefits                                   Builder Uses and Drawbacks
    Encapsulates the way a complex object is                   Often used for building composite structures.
      constructed.                                       Constructing objects requires more domain
    Allows objects to be constructed in a multistep and                 knowledge of the client than when using a Factory.
      varying process (as opposed to one-step factories).
    Hides the internal representation of the product from
      the client.
    Product implementations can be swapped in and out
     because the client only sees an abstract interface.


                                                                       you are here 4      601


---

## PDF page 640

chain of responsibility pattern

Chain of Responsibility

Use the Chain of Responsibility Pattern when you want to
give more than one object a chance to handle a request.

A scenario
Mighty Gumball has been getting more email
than they can handle since the release of the
Java-powered Gumball Machine. From their
own analysis they get four kinds of email: fan
mail from customers that love the new 1-in-10
game, complaints from parents whose kids are
addicted to the game, requests to put machines
in new locations, and a fair amount of spam.

All fan mail should go straight to the CEO, all
complaints should go to the legal department,
and all requests for new machines should go to
business development. Spam should be deleted.


Your task                                                                You’ve got to help us
                                                                       deal with the flood of email we’reMighty Gumball has already written some AI
                                                                      getting since the release of thedetectors that can tell if an email is spam, fan
                                                              Java Gumball Machine.mail, a complaint, or a request, but they need
you to create a design that can use the detectors
to handle incoming email.


602      Appendix


---

## PDF page 641

leftover patterns

How to use the Chain of Responsibility Pattern

With the Chain of Responsibility Pattern, you create a chain of objects
to examine requests. Each object in turn examines a request and either
handles it or passes it on to the next object in the chain.


                                                                                   Handler

                                                                                   successor
Each object in the chain                                                           handleRequest() acts as a handler and has            object. If it a successor can handle the request,
 it does; otherwise, it         the request to forwards
                              SpamHandler          FanHandler             ComplaintHandler       NewLocHandler  its successor.
                                  handleRequest()       handleRequest()         handleRequest()         handleRequest()


As email is received, it is passed to the first handler:
SpamHandler. If the SpamHandler can’t handle the request, it                          Email is not handled if it
is passed on to the FanHandler. And so on...                                                       falls off the end of the
                                                                                            chain — although you can always  Each email is passed to                                                              implement a catch-all handler.  the first handler.


                 Spam                 Fan             Complaint           NewLoc
                    Handler               Handler             Handler               Handler


    Chain of Responsibility Benefits               Chain of Responsibility Uses and Drawbacks

     Decouples the sender of the request and its                Commonly used in Windows systems to handle
         receivers.                                                      events like mouse clicks and keyboard events.
      Simplifies your object because it doesn’t have                Execution of the request isn’t guaranteed; it may
          to know the chain’s structure and keep direct                                   fall off the end of the chain if no object handles it
         references to its members.                                                  (this can be an advantage or a disadvantage).
      Allows you to add or remove responsibilities                Can be hard to observe and debug at runtime.
         dynamically by changing the members or order of
         the chain.


                                                                       you are here 4      603


---

## PDF page 642

flyweight pattern

Flyweight
Use the Flyweight Pattern when one instance of a class
can be used to provide many virtual instances.
A scenario
You want to add trees as objects in your new landscape design application. In your
application, trees don’t really do very much; they have an X-Y location, and they can
draw themselves dynamically, depending on how old they are. The thing is, a user
might want to have lots and lots of trees in one of their home landscape designs. It
might look something like this:


                 Tree
     Tree                                           Tree

                                Tree

                                                                         Each                                                                                  Tree                                                                                                         instance
                                                     Tree                                                                                            maintains its own                                                                                                              state.

                         House                                 Tree
      Tree
                                                                               xCoord
                                                  Tree
                                                                               yCoord
                                                                            age

                                                                       display()  {
                                                                        // use X-Y coords
                                                                        // & complex age
                                                                        // related calcs
                                                                      }
Your big client’s dilemma

You have a key client you’ve been pitching for months.
They’re going to buy 1,000 seats of your application, and
they’re using your software to do the landscape design for
huge planned communities. After using your software for a
week, your client is complaining that when they create large
groves of trees, the app starts getting sluggish...


604      Appendix


---

## PDF page 643

leftover patterns

Why use the Flyweight Pattern?

What if, instead of having thousands of Tree objects, you
could redesign your system so that you’ve got only one
instance of Tree, and a client object that maintains the state
of ALL your trees? That’s the Flyweight!


  All the state, for ALL                                                          One,                                                                                                                single,                                                                                             state-free  of your virtual Tree                                                        Tree                                                                                               object.   objects, is stored in this
  2D array.
                   TreeManager                  Tree
                              treeArray                          display(x, y, age) {
                                                         // use X-Y coords
                                                         // & complex age                       displayTrees() {
                                                         // related calcs                         // for all trees {
                                                       }                           // get array row
                           display(x, y, age);
                         }
                      }


  Flyweight Benefits                               Flyweight Uses and Drawbacks

   Reduces the number of object instances at runtime,           The Flyweight is used when a class has many
      saving memory.                                                      instances, and they can all be controlled identically.
    Centralizes state for many “virtual” objects into a              A drawback of the Flyweight Pattern is that once
       single location.                                                   you’ve implemented it, single, logical instances of the
                                                                           class will not be able to behave independently from
                                                                         the other instances.


                                                                       you are here 4      605


---

## PDF page 644

interpreter pattern

Interpreter
                                                          The Interpreter
Use the Interpreter Pattern to build an                                                                        Pattern requires
interpreter for a language.                                  some knowledge of
                                                                   formal grammars.A scenario
Remember the Duck Simulator? You have a hunch it would also            If you’ve never studied formal grammars,
make a great educational tool for children to learn programming.        go ahead and read through the pattern;
Using the simulator, each child gets to control one duck with a              you’ll still get the gist of it.
simple language. Here’s an example of the language:
                                                            right.                                    Turn the duck
   right;                                 Fly all day...
   while (daylight) fly;
   quack;                                            ...and then quack.


Now,     remembering              how to create                           grammars                                      from                                         one
                                                         of your old                                     consistingintroductory           programming                                classes,                             you write                                          out the                                          grammar:                                                                                          is an expression                                     A program            and                                                             of commands                                                     of sequences       statements).                                                                                         (“while”                                                                              repetitions                                                                A sequence is a set of
                                                                                                        expressions separated
   expression ::=  <command> | <sequence> | <repetition>              by semicolons.
   sequence ::= <expression> ';' <expression>
   command ::= right | quack | fly                               We have three
                                                                                  commands: right,   repetition ::= while '(' <variable> ')'<expression>                                                                                            quack, and fly.   variable ::= [A-Z,a-z]+
                                  A while statement is just                                           a conditional variable and                                                 an expression.
Now what?

You’ve got a grammar; now all you need is a way to represent and
interpret sentences in the grammar so that the students can see the
effects of their programming on the simulated ducks.


606      Appendix


---

## PDF page 645

leftover patterns

How to implement an interpreter

When you need to implement a simple language, the
Interpreter Pattern defines a class-based representation for its
grammar along with an interpreter to interpret its sentences.
To represent the language, you use a class to represent each
rule in the language. Here’s the duck language translated into
classes. Notice the direct mapping to the grammar.
                                                                 Expression
                                                                                 interpret(context)


                                                        Repetition                    Sequence
                                                                      variable                              expression1
                                                               expression                            expression2
                                                                interpret(context)                     interpret(context)


                              Variable            QuackCommand      RightCommand       FlyCommand
                                  interpret(context)         interpret(context)         interpret(context)          interpret(context)


To interpret the language, call the interpret() method on each
expression type. This method is passed a context—which
contains the input stream of the program we’re parsing—and
matches the input and evaluates it.


  Interpreter Benefits                                Interpreter Uses and Drawbacks
     Representing each grammar rule in a class makes             Use Interpreter when you need to implement a
       the language easy to implement.                                   simple language.
    Because the grammar is represented by classes, you            Appropriate when you have a simple grammar and
      can easily change or extend the language.                               simplicity is more important than efficiency.
    By adding methods to the class structure, you can             Used for scripting and programming languages.
     add new behaviors beyond interpretation, like pretty             This pattern can become cumbersome when
       printing and more sophisticated program validation.                   the number of grammar rules is large. In these
                                                                  cases a parser/compiler generator may be more
                                                                             appropriate.


                                                                       you are here 4      607


---

## PDF page 646

mediator pattern

Mediator
Use the Mediator Pattern to centralize complex
communications and control between related objects.
A scenario
Bob has an automated home, thanks to the good folks at HouseOfTheFuture. All of
his appliances are designed to make his life easier. When Bob stops hitting the snooze
button, his alarm clock tells the coffee maker to start brewing. Even though life is good
for Bob, he and other customers are always asking for lots of new features: No coffee
on the weekends... Turn off the sprinkler 15 minutes before a shower is scheduled...
Set the alarm early on trash days...


       Alarm                                                                CoffeePot
       onEvent() {                    Alarm                              onEvent() {
         checkCalendar()                                                     checkCalendar()
         checkSprinkler()                                   CoffeePot       checkAlarm()
         startCoffee()                                                       // do more stuff
         // do more stuff                                                 }
       }


       Calendar                                                                   Sprinkler
                               Calendar                     Sprinkler       onEvent() {                                                         onEvent() {
         checkDayOfWeek()                                                    checkCalendar()
         doSprinkler()                                                       checkShower()
         doCoffee()                                                          checkTemp()
         doAlarm()                                                           checkWeather()
         // do more stuff                                                    // do more stuff
       }                                                                  }


HouseOfTheFuture’s dilemma
It’s getting really hard to keep track of which rules reside in which objects, and how
the various objects should relate to each other.

608      Appendix


---

## PDF page 647

leftover patterns

Mediator in action...                                                                 It’s such a relief,
                                                                                     not having to figure
With a Mediator added to the system, all                                                                                     out that Alarm clock’s
of the appliance objects can be greatly                                                                                          picky rules!
simplified:

  They tell the Mediator when their state
   changes.                                                                 CoffeePot                                        Alarm
  They respond to requests from the
   Mediator.
Before we added the Mediator, all of the                                              Mediator
appliance objects needed to know about each                                         if(alarmEvent){other; that is, they were all tightly coupled.
                                                                                checkCalendar()With the Mediator in place, the appliance
objects are all completely decoupled from              Mediator                  checkShower()
each other.                                                                       checkTemp()
                                                                              }The Mediator contains all of the control
                                                                               if(weekend) {logic for the entire system. When an existing
appliance needs a new rule, or a new                                                 checkWeather()
appliance is added to the system, you’ll know                                          // do more stuff
that all of the necessary logic will be added to                                        }
                                                                      Sprinklerthe Mediator.                                  Calendar                        if(trashDay) {
                                                                                resetAlarm()
                                                                                // do more stuff
                                                                              }


  Mediator Benefits                             Mediator Uses and Drawbacks

     Increases the reusability of the objects supported by           The Mediator is commonly used to coordinate
       the Mediator by decoupling them from the system.                    related GUI components.
     Simplifies maintenance of the system by centralizing           A drawback of the Mediator Pattern is that without
       control logic.                                                     proper design, the Mediator object itself can become
     Simplifies and reduces the variety of messages sent                  overly complex.
      between objects in the system.


                                                                       you are here 4      609


---

## PDF page 648

memento pattern

Memento
Use the Memento Pattern when you need
 to be able to return an object to one of its
 previous states; for instance, if your user
 requests an “undo.”

A scenario
 Your interactive role-playing game is hugely successful,
 and has created a legion of addicts, all trying to get
 to the fabled “level 13.” As users progress to more
 challenging game levels, the odds of encountering
 a game-ending situation increase. Fans who have
 spent days progressing to an advanced level are
 understandably miffed when their character gets snuffed,
 and they have to start all over. The cry goes out for a
“save progress” command, so that players can store their
 game progress and at least recover most of their efforts                                                                 Just be careful how you go about
 when their character is unfairly extinguished. The                                                                           saving the game state. It’s pretty
“save progress” function needs to be designed to return                   complicated, and I don’t want anyone
 a resurrected player to the last level she completed                        else with access to it mucking it up and
 successfully.                                                         breaking my code.


 610      Appendix


---

## PDF page 649

leftover patterns

The Memento at work

The Memento has two goals:

    Saving the important state of a system’s key object

    Maintaining the key object’s encapsulation

Keeping the Single Responsibility Principle in mind, it’s also
a good idea to keep the state that you’re saving separate from                                                        GameMemento
the key object. This separate object that holds the state is
known as the Memento object.                                         savedGameState


                             Client                                MasterGameObject
                         // when new level is reached           gameState
                         Object saved =                                                                Object getCurrentState() {                           (Object) mgo.getCurrentState();                                                                 // gather state
                                                                  return(gameState);                         // when a restore is required
 While this isn’t            mgo.restoreState(saved);              }
 a terribly fancy
                                                                restoreState(Object savedState) { implementation, notice
 that the Client has                                                // restore state
  no access to the                                                }
  Memento’s data.
                                                               // do other game stuff


  Memento Benefits                         Memento Uses and Drawbacks

    Keeping the saved state external from the key               The Memento is used to save state.
       object helps to maintain cohesion.                       A drawback to using Memento is that saving and
    Keeps the key object’s data encapsulated.                            restoring state can be time-consuming.
     Provides easy-to-implement recovery capability.               In Java systems, consider using Serialization to
                                                                 save a system’s state.


                                                                       you are here 4      611


---

## PDF page 650

prototype pattern

Prototype

Use the Prototype Pattern when creating an instance
of a given class is either expensive or complicated.

A scenario
Your interactive role-playing game has an insatiable appetite for monsters. As your
heroes make their journey through a dynamically created landscape, they encounter
an endless chain of foes that must be subdued. You’d like the monster’s characteristics
to evolve with the changing landscape. It doesn’t make a lot of sense for bird-like
monsters to follow your characters into underseas realms. Finally, you’d like to allow
advanced players to create their own custom monsters.


                                                                        Yikes! Just the act
                                                            of creating all of these different
                                                                kinds of monster instances is getting
                                                                           tricky... Putting all sorts of state detail in the
                                                            constructors doesn’t seem to be very cohesive. It
                                                         would be great if there was a single place where
                                                                                    all of the instantiation details could be
                   It would be a lot cleaner if                               encapsulated...
               we could decouple the code that
                  handles the details of creating the
                monsters from the code that actually
                   needs to create the instances on
                   the fly.


612      Appendix


---

## PDF page 651

leftover patterns

Prototype to the rescue

The Prototype Pattern allows you to make new instances by
copying existing instances. (In Java this typically means using               <<interface>>
the clone() method, or deserialization when you need deep                 Monster
copies.) A key aspect of this pattern is that the client code can
make new instances without knowing which specific class is
being instantiated.


                                         WellKnownMonster       DynamicPlayerGeneratedMonster


             MonsterMaker
                                                      The client needs a new monster             makeRandomMonster() {                                                                       appropriate to the current                Monster m =                                              situation. (The client won’t know                  MonsterRegistry.getMonster();               what kind of monster he gets.)
             }


                   MonsterRegistry
                  Monster getMonster() {
                    // find the correct monster
                                                          The registry finds the                    return correctMonster.clone();                                                                                                   appropriate
                  }                                                                            monster, makes a clone of it, and                                                                           returns the clone.


   Prototype Benefits                               Prototype Uses and Drawbacks

     Hides the complexities of making new instances               Prototype should be considered when a system
      from the client.                                             must create new objects of many types in a
     Provides the option for the client to generate                      complex class hierarchy.
       objects whose type is not known.                        A drawback to using Prototype is that making a
     In some circumstances, copying an object can be                  copy of an object can sometimes be complicated.
      more efficient than creating a new object.


                                                                       you are here 4      613


---

## PDF page 652

visitor pattern

Visitor
Use the Visitor Pattern when you want to
 add capabilities to a composite of objects
 and encapsulation is not important.

A scenario
 Customers who frequent the Objectville Diner and Objectville
 Pancake House have recently become more health conscious. They
 are asking for nutritional information before ordering their meals.
 Because both establishments are so willing to create special orders,
 some customers are even asking for nutritional information on a
 per-ingredient basis.

 Lou’s proposed solution:                                           Menu
                               // new methods
                                getHealthRating()
                                getCalories()
                                getProtein()
                                getCarbs()                                                           MenuItem         MenuItem

                         // new methods
                         getHealthRating()
                         getCalories()
                         getProtein()
                         getCarbs()                    Ingredient              Ingredient


 Mel’s concerns...
“Boy, it seems like we’re opening Pandora’s box. Who knows what
 new method we’re going to have to add next, and every time we
 add a new method we have to do it in two places. Plus, what if
 we want to enhance the base application with, say, a recipes class?
 Then we’ll have to make these changes in three different places...”


 614      Appendix


---

## PDF page 653

leftover patterns

The Visitor drops by

The Visitor works hand in hand with a Traverser. The Traverser
knows how to navigate to all of the objects in a Composite. The
Traverser guides the Visitor through the Composite so that the Visitor
can collect state as it goes. Once state has been gathered, the Client
can have the Visitor perform various operations on the state. When
new functionality is required, only the Visitor must be enhanced.                                   All these composite
                                                                                                             classes have to do is add
                                                                                      a getState() method
                                         The Visitor needs to be able to call    (and not worry about                                                                                                  exposing themselves).                                                    getState() across classes, and this isThe Client asks                                   where you can add new methods for
 the Visitor to get                                the client to use. information from the
                                                                   Menu Composite structure...
 New methods can be                                     getState()                      getHealthRating() added to the Visitor
                                                     Visitor          getState() without affecting the      getCalories() Composite.                getProtein()                         getCarbs()              getState()
                                                              MenuItem         MenuItem                                                    getState()
                        Client /
                    Traverser                                                            getState()


                                                                 Ingredient              Ingredient                         The Traverser knows how to
                                 guide the Visitor through
                             the Composite structure.


   Visitor Benefits                                        Visitor Drawbacks
     Allows you to add operations to a Composite                The Composite classes’ encapsulation is broken
        structure without changing the structure itself.                   when the Visitor is used.
    Adding new operations is relatively easy.                   Because the traversal function is involved,
    The code for operations performed by the Visitor is                changes to the Composite structure are more
        centralized.                                                                             difficult.


                                                                       you are here 4      615
