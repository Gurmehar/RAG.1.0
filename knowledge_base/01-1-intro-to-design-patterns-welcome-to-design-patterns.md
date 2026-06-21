# 1: intro to Design Patterns: Welcome to Design Patterns

_Extracted from PDF pages 39-74. Text only; images and diagrams are not embedded._


---

## PDF page 39

1 intro to Design Patterns
   Welcometo
       DesignPatterns
                                                 Now that we’re living
                                                                               in Objectville, we’ve just got to
                                                            get into Design Patterns...everyone
                                                                                is doing them. Soon we’ll be the hit
                                                           of Jim and Betty’s Wednesday night
                                                                        patterns group!


      Someone has already solved your problems. In this chapter,
             you’ll learn why (and how) you can exploit the wisdom and lessons learned by other
          developers who’ve been down the same design problem road and survived the trip.
          Before we’re done, we’ll look at the use and benefits of design patterns, look at some
         key object-oriented (OO) design principles, and walk through an example of how one
           pattern works. The best way to use patterns is to load your brain with them and then
          recognize places in your designs and existing applications where you can apply them.
          Instead of code reuse, with patterns you get experience reuse.

                                                                             this is a new chapter      1


---

## PDF page 40

SimUDuck

It started with a simple SimUDuck app

Joe works for a company that makes a highly successful duck pond
simulation game, SimUDuck. The game can show a large variety of
duck species swimming and making quacking sounds. The initial
designers of the system used standard OO techniques and created
one Duck superclass from which all other duck types inherit.


                                                      Duck
     All ducks quack and swim. The                       quack()
     superclass takes care of the
    implementation code.                                 swim()                        The display() method is
                                                                        display()                                abstract, since all duck
                                                                                                             // OTHER duck-like methods...              subtypes look different.


       duck subtype                                                                                            ducks                                                                     of  Each                                                                                     types                                                                          other                                                                                                                    class.                                  MallardDuck           RedheadDuck       Lots of   is responsible                                                                        Duck                                                                        the                                                                  from                                          display() {                       display() {                  inherit   for implementing            display()                                                                                                                   // looks like a redhead }    its own           for how it               // looks like a mallard }    behavior                 screen.        on the     looks


In the last year, the company has been under increasing pressure
from competitors. After a week-long off-site brainstorming
session over golf, the company executives think it’s time for a big
innovation. They need something really impressive to show at the
upcoming shareholders meeting in Maui next week.


2      Chapter 1


---

## PDF page 41

intro to design patterns

But now we need the ducks to FLY

 The executives decided that flying ducks is just what the
 simulator needs to blow away the competitors. And of course                  I just need to add a
 Joe’s manager told them it’ll be no problem for Joe to just                        fly() method in the Duck class
 whip something up in a week. “After all,” said Joe’s boss,                   and then all the ducks will inherit
“he’s an OO programmer…how hard can it be?”                                             it. Now’s my time to really show my
                                                                        true OO genius.


                                                                      Joe
 What we want.


                                Duck
                                 quack()
                                 swim()
                                      display()                        Joe added.                                           What                                 fly()    subclasses All    fly().                          // OTHER duck-like methods...  inherit


          MallardDuck           RedheadDuck                         types...                                               Duck                                            Other
        display() {                       display() {
            // looks like a mallard }               // looks like a redhead }


                                                                         you are here 4      3


---

## PDF page 42

something went wrong

But something went horribly wrong...


     Joe, I’m at the shareholders meeting.
    They just gave a demo and there were
    rubber duckies flying around the screen.
   Was this your idea of a joke?


               What happened?
                           Joe failed to notice that not all             Okay, so there’s a slight
                             subclasses of Duck should fly. When      flaw in my design. I don’t
                           Joe added new behavior to the           see why they can’t just call
                     Duck superclass, he was also adding         it a “feature.” It’s kind
                          behavior that was not appropriate            of cute...
                              for some Duck subclasses. He now
                          has flying inanimate objects in the
                    SimUDuck program.                  What Joe thought                    A localized update to the code caused a non-
                                    local side effect (flying rubber ducks)!                                             was a great use
                                             Duck                        of inheritance
                                              quack()                                                        for the purpose             the                swim()            in           fly() the                   display()     puttinghegaveALL                   fly()                              of reuse hasn’t By   superclass,abilitytothose                            // OTHER duck-like methods...                 turned out so well    flying includingfly.     ducks,shouldn’t                                 when it comes to    that                                                     maintenance.
                                                                                                rubber                       MallardDuck           RedheadDuck             RubberDuck                   too, that                                                                                 Notice                                                                                                           quack()                         display() {                    display() {                   quack() {                                                                                                    quack, so                                                                                        don’t                                                                                   ducks                                                                                to “Squeak”.                                      // looks like a mallard             // looks like a redhead               // overridden to Squeak                                                                                                  is overridden                                }                                     }                                       }
                                                                                        display() {
                                                                                                                                    // looks like a rubberduck
                                                                                                              }

4      Chapter 1


---

## PDF page 43

intro to design patterns

Joe thinks about inheritance...


    I could always just                                         But then what happens
    override the fly() method                                when we add wooden
      in rubber duck, like I have                                  decoy ducks to the
     with the quack() method...                                  program? They aren’t
                                                                supposed to fly or quack...


                             RubberDuck
                              quack()  { // squeak}
                                  display() { // rubber duck }
                                   fly() {
                                                  // override to do nothing
                                 }


                                                                                        DecoyDuck
                                                                                                quack() {
                                                                                                                                                                      // override to do nothing
                                                                                                                                         }
                                                        Here’s another class in the        display() { // decoy duck}
                                                                                                                                         fly() {                                                        hierarchy; notice that like                                                                     it doesn’t fly,                                                 RubberDuck,                                       // override to do nothing                                              but it also doesn’t quack.           }


                                       Which of the following are disadvantages of using inheritance to
                                            provide Duck behavior? (Choose all that apply.)


  ❏  A. Code is duplicated across subclasses.    ❏  D.  It’s hard to gain knowledge of all duck behaviors.
  ❏  B. Runtime behavior changes are difficult.   ❏  E. Ducks can’t fly and quack at the same time.
  ❏  C. We can’t make ducks dance.        ❏   F. Changes can unintentionally affect other ducks.


                                                                         you are here 4      5


---

## PDF page 44

inheritance is not the answer

How about an interface?

Joe realized that inheritance probably wasn’t the
answer, because he just got a memo that says that                    I could take the fly() out of the Duck
the executives now want to update the product every                   superclass, and make a Flyable() interface
six months (in ways they haven’t yet decided on). Joe                  with a fly() method. That way, only the ducks
knows the spec will keep changing and he’ll be forced                 that are supposed to fly will implement that
to look at and possibly override fly() and quack() for                    interface and have a fly() method...and I might
every new Duck subclass that’s ever added to the                      as well make a Quackable, too, since not all
program... forever.                                                  ducks can quack.
So, he needs a cleaner way to have only some (but not
all) of the duck types fly or quack.


                                                   Duck
                                                     swim()                          Quackable
              Flyable                                     display()                               quack()
                   fly()                                                                        // OTHER duck-like methods...


                   MallardDuck           RedheadDuck            RubberDuck              DecoyDuck
                    display()                     display()                     display()                         display()
                          fly()                                 fly()                       quack()
                  quack()                    quack()


       What do YOU think about this design?


6      Chapter 1


---

## PDF page 45

intro to design patterns


   That is, like, the dumbest idea
   you’ve come up with. Can you say,
  “duplicate code”? If you thought having
to override a few methods was bad, how
are you gonna feel when you need to make a
little change to the flying behavior...in all 48
  of the flying Duck subclasses?!


            What would you do if you were Joe?

                  We know that not all of the subclasses should have flying or quacking
                             behavior, so inheritance isn’t the right answer. But while having the
                              subclasses implement Flyable and/or Quackable solves part of the
                        problem (no inappropriately flying rubber ducks), it completely
                             destroys code reuse for those behaviors, so it just creates a different
                         maintenance nightmare. And of course there might be more than one
                           kind of flying behavior even among the ducks that do fly...
                        At this point you might be waiting for a Design Pattern to come riding
                              in on a white horse and save the day. But what fun would that be? No,
                           we’re going to figure out a solution the old-fashioned way—by applying
                               good OO software design principles.

                                                                    Wouldn’t it be dreamy
                                                                                if there were a way to build software
                                                            so that when we need to change it, we
                                                                could do so with the least possible
                                                            impact on the existing code? We could
                                                         spend less time reworking code and
                                                     more making the program do cooler
                                                                                         things...


                                                                   you are here 4      7


---

## PDF page 46

change is constant

The one constant in software development

Okay, what’s the one thing you can always count on in software development?
No matter where you work, what you’re building, or what language you are programming in, what’s
the one true constant that will be with you always?
     CHANGE
                                     (use a mirror to see the answer)

No matter how well you design an application, over time an
application must grow and change or it will die.


                                              Lots of things can drive change. List some reasons you’ve had to change code
                                                        in your applications (we put in a couple of our own to get you started). Check
                                             your answers with the solution at the end of the chapter before you go on.

        My customers or users decide they want something else, or they want new functionality.
        My company decided it is going with another database vendor and it is also purchasing
               its data from another supplier that uses a different data format. Argh!


8      Chapter 1


---

## PDF page 47

intro to design patterns

Zeroing in on the problem...

So we know using inheritance hasn’t worked out very well, since
the duck behavior keeps changing across the subclasses, and it’s not
appropriate for all subclasses to have those behaviors. The Flyable
and Quackable interface sounded promising at first—only ducks that
really do fly will be Flyable, etc.—except Java interfaces typically have
no implementation code, so no code reuse. In either case, whenever
you need to modify a behavior, you’re often forced to track down and
change it in all the different subclasses where that behavior is defined,
                   newprobably         introducing                       bugs along                                    the                                    way!
Luckily,          there’s              a design                         principle                                     for                                           just                                                this situation.          Take what varies and
                                             “encapsulate” it so it
               Design Principle                    won’t affect the rest of
                         Identify the aspects of your
                       application that vary and separate                                         your code.                  them from what stays the same.

                                       design                           many                         first of               The                                   more time             The result? Fewer                                 spend                                   We’ll                       principles.
                  on these throughout the book.                unintended consequences
In other words, if you’ve got some aspect of your code that is        from code changes and
changing,          say with                  every                  new                            requirement,                                       then                                        you know                                                        you’ve
got a behavior                that                  needs                          to be                               pulled out and                                            separated                                                from                                                                               all      more f lexibility in your
the stuff that doesn’t change.                            systems!
Here’s another way to think about this principle: take the parts
that vary and encapsulate them, so that later you can
alter or extend the parts that vary without affecting
those that don’t.
As simple as this concept is, it forms the basis for almost every
design pattern. All patterns provide a way to let some part of a
system vary independently of all other parts.
Okay, time to pull the duck behavior out of the Duck classes!


                                                                         you are here 4      9


---

## PDF page 48

pull out what varies

Separating what changes from what stays the same

Where do we start? As far as we can tell, other than the problems with fly() and quack(), the Duck
class is working well and there are no other parts of it that appear to vary or change frequently. So,
other than a few slight changes, we’re going to pretty much leave the Duck class alone.
Now, to separate the “parts that change from those that stay the same,” we are going to create
two sets of classes (totally apart from Duck), one for fly and one for quack. Each set of classes will
hold all the implementations of the respective behavior. For instance, we might have one class that
implements quacking, another that implements squeaking, and another that implements silence.

    We know that fly() and quack() are the parts of the
     Duck class that vary across ducks.
     To separate these behaviors from the Duck class, we’ll pull both methods
     out of the Duck class and create a new set of classes
      to represent each behavior.

  The Duck class is still the                      we                     but                   ducks,                    all          of   superclass                           quack                                                          Various behavior                     and                     fly               the            out                                                                                                  are   are pulling                                                                       each         implementations                putting them into           and                                                                     quacking                                                      and    behaviors                                                                flying                                       Now                                                                                              going to live here.                  structure.                                                         of classes.                                                                set                                                    own   another class                                                get their


                                Pull out what varies

                                                   iors                           ying Behav    Duck class            Fl
                                   rs                                   havio                      Quacking Be

                                                Duck Behaviors


10      Chapter 1


---

## PDF page 49

intro to design patterns

Designing the Duck Behaviors

So how are we going to design the set of classes that
implement the fly and quack behaviors?
We’d like to keep things flexible; after all, it was the inflexibility in
 the duck behaviors that got us into trouble in the first place. And we know that we want to assign behaviors to the instances of Duck. For     From now on, the Duck
 example,       we might                want                          to instantiate                                 a new                                     MallardDuck                                                           instance      behaviors will live in and      initialize                     it with                  a specific                                     type of flying                                           behavior.                                     And while
 we’re there, why not make sure that we can change the behavior of a                                       a separate class—a duck dynamically? In other words, we should include behavior setter
 methods in the Duck classes so that we can change the MallardDuck’s                                                   class that implements flying behavior at runtime.
Given these goals, let’s look at our second design principle:          a particular behavior
                                                  interface.
                Design Principle
                   Program to an interface, not an
                      implementation.                                     That way, the Duck
                                                   classes won’t need
We’ll use an interface to represent each behavior—for instance,                                                to know any of theFlyBehavior and QuackBehavior—and each implementation of a
 behavior will implement one of those interfaces.                                            implementation details
So this time it won’t be the Duck classes that will implement the flying and quacking interfaces. Instead, we’ll make a set of classes       for their own behaviors.
whose entire reason for living is to represent a behavior (for example,
“squeaking”), and it’s the behavior class, rather than the Duck class,
 that will implement the behavior interface.
This is in contrast to the way we were doing things before, where                                              <<interface>>
a behavior came either from a concrete implementation in the                                         FlyBehavior
 superclass Duck, or by providing a specialized implementation in the                                             fly()
 subclass itself. In both cases we were relying on an implementation. We
were locked into using that specific implementation and there was no
room for changing the behavior (other than writing more code).                                                                                                        FlyWithWings                FlyNoWay
With our new design, the Duck subclasses will use a behavior                                          fly() {                                       fly() {
 represented by an interface (FlyBehavior and QuackBehavior), so that                                 // implements duck flying                // do nothing - can’t fly!
 the actual implementation of the behavior (in other words, the specific                           }                                             }
 concrete behavior coded in the class that implements the FlyBehavior
 or QuackBehavior) won’t be locked into the Duck subclass.


                                                                        you are here 4      11


---

## PDF page 50

program to an interface


                                      I don’t see why you
                                  have to use an interface for
                                      FlyBehavior. You can do the
                               same thing with an abstract
                                       superclass. Isn’t the whole point
                                    to use polymorphism?


                               “Program to an interface” really means
                               “Program to a supertype.”

                                       The word interface is overloaded here. There’s the concept of an
                                                           interface, but there’s also the Java construct of an interface. You
                                              can program to an interface without having to actually use a Java
                                                           interface. The point is to exploit polymorphism by programming
                                                       to a supertype so that the actual runtime object isn’t locked into
                                                    the code. And we could rephrase “program to a supertype” as
                                                  “the declared type of the variables should be a supertype, usually
                                           an abstract class or interface, so that the objects assigned to
                                                    those variables can be of any concrete implementation of the
                                                     supertype, which means the class declaring them doesn’t have to
                                        know about the actual object types!”
                                               This is probably old news to you, but just to make sure we’re
                                                                     all saying the same thing, here’s a simple example of using a
                                              polymorphic type—imagine an abstract class Animal, with two
                                                   concrete implementations, Dog and Cat.
           Abstract                     Programming        bean    supertype                                  to an implementation would be:                             (could                abstract                                          Dog d = new Dog();                           class           interface).     OR                                    DogDeclaring(a concretethe variableimplementation“d” as type                                           d.bark();            of Animal) forces us to code to a                                                                              concrete implementation.
                       Animal
                                              But programming to an interface/supertype would be:                 makeSound()
                                           Animal animal = new Dog();                                                                     We know it’s a Dog, but                                                                         we can now use the animal                                           animal.makeSound();            reference polymorphically.Concrete implementations.                             Even better, rather than hardcoding the instantiation of the
                                                 subtype (like new Dog()) into the code, assign the concrete
         Dog                       Cat         implementation object at runtime:
  makeSound()                      {                 makeSound()                                                                      {
      bark();                                   meow();                                          a = getAnimal();                                                               We don’t know WHAT the actual
    }                                              }                                                                                      animal subtype is...all we care about
   bark() { // bark sound }           meow() { // meow sound }                                           a.makeSound();             is that it knows how to respond to                                                                                makeSound().

12      Chapter 1


---

## PDF page 51

intro to design patterns

Implementing the Duck Behaviors

Here we have the two interfaces, FlyBehavior and QuackBehavior, along with
the corresponding classes that implement each concrete behavior:
                                                                          Same thing here for the quack
                                                                                               behavior; we have an interface                              FlyBehavior is an interface                                                                                that just includes a quack()                            that all flying classes implement.                                                                           method that needs to be                                   All new flying classes just need                                                                                        implemented.                            to implement the fly() method.

                         <<interface>>                                                                             <<interface>>
                     FlyBehavior                                                         QuackBehavior
                        fly()                                                                                      quack()


       FlyWithWings              FlyNoWay                       Quack                 Squeak                 MuteQuack
    fly() {                                       fly() {                                     quack() {                        quack() {                         quack() {
       // implements duck flying                // do nothing - can’t fly!                                   // implements duck quacking          // rubber duckie squeak                   // do nothing - can’t quack!
    }                                             }                                                          }                                             }                                              }

                                             Quacks                                               that              And                                                                  Quacks that squeak.                          here’s                                                       really                                                                                       make                        the                                                                                      that                                                       quack.                for                                                                                   Quacks                          all  Here’s                        ducks      the                                                                                    at all.                          thatimplementation                                                                               no sound of                                   can’t     flying                                 fly.            implementationall that   for     have      ducks          wings.


          With this design, other types of objects can
          reuse our fly and quack behaviors because       So we get the benefit of
          these behaviors are no longer hidden away     REUSE without all the
            in our Duck classes!                                       baggage that comes along
                                                                                 with inheritance.

        And we can add new behaviors without
          modifying any of our existing behavior
          classes or touching any of the Duck classes
           that use flying behaviors.


                                                                        you are here 4      13


---

## PDF page 52

behavior in a class


     Do I always have to implement my                                                                                          It feels a little weird to have a classQ:                               Q:
application first, see where things are                                                          that’s just a behavior. Aren’t classes
                                            Should we make Duck an interface    supposed to represent things? Aren’tchanging, and then go back to separate  Q:
and encapsulate those things?             too?                                      classes supposed to have both state AND
                                                                                   behavior?
     Not always; often when you are               Not in this case. As you’ll see onceA:               A:designing an application, you anticipate        we’ve got everything hooked together, we do           In an OO system, yes, classes                                   A: those areas that are going to vary and then      benefit by having Duck not be an interface,      represent things that generally have both
go ahead and build the flexibility to deal       and having specific ducks, like MallardDuck,     state (instance variables) and methods.
 with it into your code. You’ll find that the          inherit common properties and methods.      And in this case, the thing happens to be
 principles and patterns can be applied at any   Now that we’ve removed what varies from      a behavior. But even a behavior can still
stage of the development lifecycle.              the Duck inheritance, we get the benefits of     have state and methods; a flying behavior
                                                        this structure without the problems.             might have instance variables representing
                                                                                               the attributes for the flying (wing beats per
                                                                                             minute, max altitude, speed, etc.) behavior.


     1  Using our new design, what would you do if you needed
             to add rocket-powered flying to the SimUDuck app?


     2  Can you think of a class that might want to use the Quack            behavior that isn’t a duck?


                                                                                       sounds). duck makes that device
                                                                                                 (a call duck a example, One 2)
                                                                                                                interface. FlyBehavior
                                                                                                 the implements that class
                                                                                 FlyRocketPowered a Create 1)
                                                                                                      Answers:

14      Chapter 1


---

## PDF page 53

intro to design patterns

Integrating the Duck Behaviors
Here’s the key: A Duck will now delegate its flying and
quacking behaviors, instead of using quacking and
flying methods defined in the Duck class (or subclass).

Here’s how:

         1    First we’ll add two instance variables of type FlyBehavior and
              QuackBehavior—let’s call them flyBehavior and quackBehavior. Each concrete duck
                  object will assign to those variables a specific behavior at runtime, like FlyWithWings for
                   flying and Squeak for quacking.
                  We’ll also remove the fly() and quack() methods from the Duck class (and any subclasses)
                because we’ve moved this behavior out into the FlyBehavior and QuackBehavior classes.
                  We’ll replace fly() and quack() in the Duck class with two similar methods, called
                 performFly() and performQuack(); you’ll see how they work next.
                                                      Instance variables hold a reference
 The behavior variables are                       to a specific behavior at runtime.  declared as the behavior
                                     Duck INTERFACE type.
                                   FlyBehavior flyBehavior
                                QuackBehavior quackBehavior
                                                viors  These methods replace      performQuack()                 Flying Beha
                                                 s   fly() and quack().            swim()                                   r                                    Quacking Behavio                                            display()
                                      performFly()
                                                                                     Duck Behaviors
                                                                  // OTHER duck-like methods...


         2  Now we implement performQuack():                                                                          to something that                                                                                  reference                                                       a                                                                                                      interface.              public abstract class Duck {           Each Duck has                                                                             QuackBehavior                                                                 the                 QuackBehavior quackBehavior;           implements
                 // more                                                  the quack                                                                  than handling                                                             Rather                                                                                           object                                                                      the Duck                                                                                           itself,                                                                                                object                                                                           to the                 public void performQuack() {              behavior                                                                   that behavior                   quackBehavior.quack();                   delegates                                                               by quackBehavior.                }                                               referenced
             }
                  Pretty simple, huh? To perform the quack, a Duck just asks the object that
                         is referenced by quackBehavior to quack for it. In this part of the code we
                  don’t care what kind of object the concrete Duck is, all we care about is
               that it knows how to quack()!

                                                                        you are here 4      15


---

## PDF page 54

integrating duck behavior

More integration...


          3  Okay, time to worry about how the flyBehavior and quackBehavior
                  instance variables are set. Let’s take a look at the MallardDuck
                     class:

              public class MallardDuck extends Duck {
                                               A MallardDuck uses the Quack
                                                                                       class to handle its quack, so when                 public MallardDuck() {                                                                      performQuack() is called, the
                    quackBehavior = new Quack();               responsibility for the quack is delegated
                    flyBehavior = new FlyWithWings();      to the Quack object and we get a real
                 }                                                      quack.
  Remember, MallardDuck inherits the                              And it uses FlyWithWings as its                                                                          FlyBehavior type.  quackBehavior and flyBehavior instance
  variables from class Duck.

                 public void display() {
                     System.out.println("I'm a real Mallard duck");
                 }
             }


                MallardDuck’s quack is a real live duck quack, not a squeak and not
                a mute quack. When a MallardDuck is instantiated, its constructor
                      initializes the MallardDuck’s inherited quackBehavior instance
                  variable to a new instance of type Quack (a QuackBehavior concrete
                implementation class).
             And the same is true for the duck’s flying behavior—the MallardDuck’s
                  constructor initializes the inherited flyBehavior instance variable
                 with an instance of type FlyWithWings (a FlyBehavior concrete
                implementation class).


16      Chapter 1


---

## PDF page 55

intro to design patterns


     Wait a second, didn’t you
    say we should NOT program to an
implementation? But what are we doing in that
constructor? We’re making a new instance of a
  concrete Quack implementation class!


 Good catch, that’s exactly what we’re doing...
  for now.
  Later in the book we’ll have more patterns in
  our toolbox that can help us fix it.
  Still, notice that while we are setting the
  behaviors to concrete classes (by instantiating
  a behavior class like Quack or FlyWithWings
 and assigning it to our behavior reference
  variable), we could easily change that at
  runtime.
  So, we still have a lot of flexibility here. That
  said, we’re doing a poor job of initializing
  the instance variables in a flexible way. But
  think about it: since the quackBehavior
  instance variable is an interface type, we
  could (through the magic of polymorphism)
  dynamically assign a different QuackBehavior
  implementation class at runtime.
 Take a moment and think about how you
  would implement a duck so that its behavior
  could change at runtime. (You’ll see the code
  that does this a few pages from now.)


                                            you are here 4      17


---

## PDF page 56

testing duck behaviors

Testing the Duck code

    1 Type and compile the Duck class below (Duck.java), and the
      MallardDuck class from two pages back (MallardDuck.java).

       public abstract class Duck {                                                     Declare two reference          FlyBehavior flyBehavior;              variables for the behavior          QuackBehavior quackBehavior;        interface types. All duck
          public Duck() { }                         subclasses (in the same                                                       package) inherit these.
          public abstract void display();
          public void performFly() {
             flyBehavior.fly();                 Delegate to the behavior class.
          }
          public void performQuack() {
             quackBehavior.quack();
          }
          public void swim() {
             System.out.println("All ducks float, even decoys!");
          }
       }

    2 Type and compile the FlyBehavior interface (FlyBehavior.java)
      and the two behavior implementation classes (FlyWithWings.java
      and FlyNoWay.java).
       public interface FlyBehavior {                                           The interface that all flying          public void fly();                                                         behavior classes implement.       }

       public class FlyWithWings implements FlyBehavior {
                                                                                         implementation          public void fly() {                                       Flying behavior              System.out.println("I'm flying!!");           for ducks that DO fly...
          }
       }
       public class FlyNoWay implements FlyBehavior {                                                                              Flying behavior implementation          public void fly() {                                                                     for ducks that do NOT fly (like              System.out.println("I can't fly");                                                                      rubber ducks and decoy ducks).          }
       }

18      Chapter 1


---

## PDF page 57

intro to design patterns

Testing the Duck code, continued...
 3 Type and compile the QuackBehavior interface
    (QuackBehavior.java) and the three behavior implementation
    classes (Quack.java, MuteQuack.java, and Squeak.java).
    public interface QuackBehavior {
       public void quack();
    }
    public class Quack implements QuackBehavior {
       public void quack() {
          System.out.println("Quack");
       }
    }

    public class MuteQuack implements QuackBehavior {
       public void quack() {
           System.out.println("<< Silence >>");
       }
    }
    public class Squeak implements QuackBehavior {
       public void quack() {
           System.out.println("Squeak");
       }
    }
 4 Type and compile the test class
    (MiniDuckSimulator.java).
    public class MiniDuckSimulator {
       public static void main(String[] args) {
          Duck               mallard = new MallardDuck();                                                                                          inherited                                                                      MallardDuck’s                                                       This calls the                                                                               then delegates to          mallard.performQuack();                                                                    method, which                                                        performQuack()                                                                                              quack() on          mallard.performFly();                                                                   QuackBehavior (i.e., calls                                                   the object’s                                                                                                   reference).                                                                             quackBehavior       }                                                   the duck’s inherited    }                                                                                        MallardDuck’s                                                Then we do the same thing with 5  Run the code!                                      inherited performFly() method.
          File Edit  Window Help Yadayadayada
    %java MiniDuckSimulator
    Quack
    I’m flying!!

                                                                        you are here 4      19


---

## PDF page 58

ducks with dynamic behavior

Setting behavior dynamically

What a shame to have all this dynamic talent built into our ducks and not be using
it! Imagine you want to set the duck’s behavior type through a setter method on the
Duck class, rather than by instantiating it in the duck’s constructor.

 1 Add two new methods to the Duck class:
          public void setFlyBehavior(FlyBehavior fb) {
              flyBehavior = fb;                                                          Duck
         }                                                                                                               FlyBehavior flyBehavior
                                                                                                                         QuackBehavior quackBehavior
          public void setQuackBehavior(QuackBehavior qb) {
              quackBehavior = qb;                                                                swim()
         }                                                                                                                               display()performQuack()
                                                                                                                                             performFly()
   We can call these methods anytime we want to change the                                   setFlyBehavior()
                                                                                                                                  setQuackBehavior()
     behavior of a duck on the fly.                                                                                                                                                                                                                                     // OTHER duck-like methods...
  Editor note:  gratuitous pun - fix

 2 Make a new Duck type (ModelDuck.java).
          public class ModelDuck extends Duck {                                  life grounded...                                                                   duck begins              public ModelDuck() {                    Our model                                                 a way to fly.                 flyBehavior = new FlyNoWay();          without
                 quackBehavior = new Quack();
             }
              public void display() {
                 System.out.println("I'm a model duck");
             }
         }
                                                                     That’s okay, we’re creating a
 3 Make a new FlyBehavior type                         rocket-powered flying behavior.    (FlyRocketPowered.java).

          public class FlyRocketPowered implements FlyBehavior {
             public void fly() {
                 System.out.println("I'm flying with a rocket!");
             }
         }

20      Chapter 1


---

## PDF page 59

intro to design patterns


4  Change the test class (MiniDuckSimulator.java), add the                                                                                          Before   ModelDuck, and make the ModelDuck rocket-enabled.

 public class MiniDuckSimulator {
     public static void main(String[] args) {
          Duck mallard = new MallardDuck();
           mallard.performQuack();
           mallard.performFly();                                                                                         performFly()                                                                                                   object                                                       The first call to                                                                                           flyBehavior                                                                    to the                                                                            delegates              constructor,                                                                               ModelDuck’s          Duck model = new ModelDuck();                                                                    set in the                                                                                                         instance.                                                                         FlyNoWay                                                                      which is a           model.performFly();
           model.setFlyBehavior(new FlyRocketPowered());                                                                        This invokes the model’s inherited                                                                              behavior setter method, and...voilà!           model.performFly();                             The model suddenly has rocket-
    }                                                                      powered flying capability!               If it worked,                         the model                                   duck                                              dynamically}               changed                           its flying                                   behavior!                                     You                                               can’t do          THAT if the                             implementation lives inside             the Duck class.


5  Run it!                File Edit  Window Help Yabbadabbadoo
                 %java MiniDuckSimulator
                 Quack
                 I'm flying!!                                                After
                 I can't fly
                 I’m flying with a rocket!
                                 To change a duck’s
                                      behavior at runtime, just
                                                call the duck’s setter
                                   method for that behavior.


                                                                       you are here 4      21


---

## PDF page 60

the big picture

The Big Picture on encapsulated behaviors

Okay, now that we’ve done the deep dive on the
duck simulator design, it’s time to come back up
for air and take a look at the big picture.

Below is the entire reworked class structure. We have everything you’d expect:
ducks extending Duck, fly behaviors implementing FlyBehavior, and quack
behaviors implementing QuackBehavior.
Notice also that we’ve started to describe things a little differently. Instead
of thinking of the duck behaviors as a set of behaviors, we’ll start thinking of
them as a family of algorithms. Think about it: in the SimUDuck design, the
algorithms represent things a duck would do (different ways of quacking or
flying), but we could just as easily use the same techniques for a set of classes
that implement the ways to compute state sales tax by different states.
                                                      In fact,                                                          grabPay    careful            attention                      to                       the relationships                                 between the                                                          classes.
your    pen and              write the                      appropriate                                     relationship                                                 (IS-A,                                        HAS-A,                                                  and                                                         Make sure you do this.
IMPLEMENTS) on each arrow in the class diagram.

      Client makes use of an                                    Encapsulated fly behavior      encapsulated family of algorithms                                                                                               <<interface>>
                                                                                                                                                      FlyBehavior     for both flying and quacking.                                                                                                                                         fly()                                                                                         Think of each
                                                                                            set of behaviors
                                            Duck Client
                                             FlyBehavior flyBehavior                                                                                                                                 FlyWithWings                FlyNoWay         as a family of                                          QuackBehavior quackBehavior                                                                                                                fly() {                                       fly() {                 algorithms.
                                                                                                                                                                                                                                                                                 // implements duck flying                // do nothing - can’t fly!
                                                swim()
                                                                                                                                                                                                                                  }                                             }
                                                        display()
                                               performQuack()
                                                    performFly()
                                                    setFlyBehavior()                                  Encapsulated quack behavior
                                                setQuackBehavior()
                                                                                     // OTHER duck-like methods...                                                                                                       <<interface>>
                                                                                                                                         QuackBehavior
                                                                                                                                                                            quack()


         MallardDuck           RedheadDuck             RubberDuck               DecoyDuck
                                                                                                            Quack                  Squeak                MuteQuack
        display() {                       display() {                         display() {                             display() {                                quack() {                        quack() {                         quack() {
            // looks like a mallard }               // looks like a redhead }                // looks like a rubberduck }                 // looks like a decoy duck }                              // implements duck quacking          // rubber duckie squeak                   // do nothing - can’t quack!
                                                                                                                                                                                                            }                                             }                                              }

                                                                                                behaviorsare
                                                                       These“algorithms”                                                                                                    interchangeable.

22      Chapter 1


---

## PDF page 61

intro to design patterns

HAS-A can be better than IS-A

The HAS-A relationship is an interesting one: each duck
has a FlyBehavior and a QuackBehavior to which it
delegates flying and quacking.
When you put two classes together like this you’re using
composition. Instead of inheriting their behavior, the                          Guru and Student...
ducks get their behavior by being composed with the right                               Guru: Tell me what you
behavior object.                                                                have learned of the
                                                                                         Object-Oriented ways.
This is an important technique; in fact, it is the basis of our
                                                                                Student: Guru, I havethird design principle:                                                                           learned that the promise of the object-
                                                                               oriented way is reuse.
                                                                  Guru: Continue...
              Design Principle                                                                       Student: Guru, through inheritance all
                  Favor composition over inheritance.                    good things may be reused and so we
                                                          come to drastically cut development
                                                                            time like we swiftly cut bamboo in the
                                                                    woods.
                                                                  Guru: Is more time spent on code
As you’ve seen, creating systems using composition gives you                                                                      before or after development is
a lot more flexibility. Not only does it let you encapsulate                    complete?
a family of algorithms into their own set of classes, but it                                                                       Student: The answer is after,also lets you change behavior at runtime as long as                                                                       Guru. We always spend more time
the object you’re composing with implements the correct                      maintaining and changing software
behavior interface.                                                        than on initial development.
Composition is used in many design patterns and you’ll see a                Guru: So, should effort go into reuse
lot more about its advantages and disadvantages throughout               above maintainability and extensibility?
the book.                                                              Student: Guru, I believe that there is
                                                                                          truth in this.
                                                                  Guru: I can see that you still have
                                                          much to learn. I would like for you to
                                                                go and meditate on inheritance further.
                                                             As you’ve seen, inheritance has its
     A duck call is a device that hunters use to                             problems, and there are other ways of
       mimic the calls (quacks) of ducks. How                                achieving reuse.
       would you implement your own duck call
         that does not inherit from the Duck class?


                                                                        you are here 4      23


---

## PDF page 62

the strategy pattern

Speaking of Design Patterns...


                      Congratulations on
                    your first pattern!


          You just applied your first design pattern—the STRATEGY
             Pattern. That’s right, you used the Strategy Pattern to
            rework the SimUDuck app.
           Thanks to this pattern, the simulator is ready for any
           changes those execs might cook up on their next
            business trip to Maui.
         Now that we’ve made you take the long road to learn it,
             here’s the formal definition of this pattern:


                                                                                    when you                                                                                                definition          The Strategy Pattern defines a family of algorithms,     Use THIS                                                                                                 friends and                                                                                            impress                encapsulates each one, and makes them interchangeable.     need to                                                                                                      executives.               Strategy lets the algorithm vary independently from            influence key
                  clients that use it.


24      Chapter 1


---

## PDF page 63

intro to design patterns

      Design Puzzle


Below you’ll find a mess of classes and interfaces for an action adventure game. You’ll
find classes for game characters along with classes for weapon behaviors the characters
can use in the game. Each character can make use of one weapon at a time, but can
change weapons at any time during the game. Your job is to sort it all out...
(Answers are at the end of the chapter.)

  Your task:
    1.1  Arrange the classes.
   22.  Identify one abstract class, one interface, and eight classes.
   33. Draw arrows between classes.
               a. Draw this kind of arrow for inheritance (“extends”).
              b. Draw this kind of arrow for interface (“implements”).
                c. Draw this kind of arrow for HAS-A.
    4.4  Put the method setWeapon() into the right class.


                         Character
                  WeaponBehavior weapon
                           fight()                                           KnifeBehavior            BowAndArrowBehavior
                                                                     useWeapon() { // implements            useWeapon() { // implements
                                                                                  cutting with a knife }   <<interface>>    shooting an arrow with a bow }                               Queen
                                            fight() { ... }                                 WeaponBehavior
                                                                            useWeapon();                    King
                 fight() { ... }                                           Troll                       AxeBehavior
                                                                    fight() { ... }                            useWeapon() { // implements
                                                                                          chopping with an axe }
                                        Knight                                                                     SwordBehavior
                                                fight() { ... }                                  useWeapon() { // implements
                                                                                    swinging a sword }

                  setWeapon(WeaponBehavior w) {
                      this.weapon = w;
                 }


                                                             you are here 4      25


---

## PDF page 64

diner talk

Overheard at the local diner...


           Alice


       I need a cream cheese with jelly on white
      bread, a chocolate soda with vanilla ice cream, a
                                                                  Flo     grilled cheese sandwich with bacon, a tuna fish
 salad on toast, a banana split with ice cream & sliced
    bananas, and a coffee with a cream and two sugars ...                Give me a C.J. White,
      oh, and put a hamburger on the grill!                             a black & white, a Jack
                                                                 Benny, a radio, a house boat, a
                                                                coffee regular, and burn one!


             What’s the difference between these two orders? Not a thing! They’re both the
            same order, except Alice is using twice the number of words and trying the
              patience of a grumpy short-order cook.
             What’s Flo got that Alice doesn’t? A shared vocabulary with the short-order
              cook. Not only does that make it easier to communicate with the cook, but it gives
              the cook less to remember because he’s got all the diner patterns in his head.
             Design Patterns give you a shared vocabulary with other developers. Once you’ve
              got the vocabulary, you can more easily communicate with other developers and
                inspire those who don’t know patterns to start learning them. It also elevates your
               thinking about architectures by letting you think at the pattern level, not the
                 nitty-gritty object level.


26      Chapter 1


---

## PDF page 65

intro to design patterns

Overheard in the next cubicle...


       So I created this broadcast class. It keeps
       track of all the objects listening to it, and
       anytime a new piece of data comes along it sends
      a message to each listener. What’s cool is that the
        listeners can join the broadcast at any time or
       they can even remove themselves. It is really
               dynamic and loosely coupled!
                                                   Can you think of other shared
                                                                  vocabularies that are used
                                                         beyond OO design and diner        Rick                                                                          talk? (Hint: how about auto
                                                             mechanics, carpenters, gourmet
                                                                      chefs, and air traffic controllers?)
                                                     What qualities are communicated
                                                                along with the lingo?
                                                   Can you think of aspects of OO
                                                               design that get communicated
                                                                along with pattern names? What
                                                                            qualities get communicated along
                                                                      with the name “Strategy Pattern”?


                                                                                 Exactly. If you communicate
                                                                                         in patterns, then other developers
                                                               know immediately and precisely the       Rick, why didn’t you
                                                                         design you’re describing. Just don’t      just say you are using
                                                                     get Pattern Fever...you’ll know you     the Observer Pattern?
                                                                   have it when you start using patterns
                                                                       for Hello World...


                                                                        you are here 4      27


---

## PDF page 66

shared vocabulary

The power of a shared pattern vocabulary

    When you communicate using patterns, you
     are doing more than just sharing LINGO.
                                                                                     Pattern to                                                                            Strategy                                                                   “We’re using the                                                                             of our                                                                                             behaviors      Shared pattern vocabularies are POWERFUL.                the various                                                                  implement                                                                                                   behavior                                                                                  duck     When            you communicate                               with                                  another developer                                                     or                                                     your                                                                                              tells you the                                                                      This                                                                         ducks.”                                                                                               set                                                                                                        its own                                                                                            into       team using                    patterns, you are                               communicating                                                not                                                                  just                                                    a                                                                               encapsulated                                                                 has been                                                                                                          easily expanded                                                                          be                                                                           can        pattern            name but                      a whole                                       set of                                                                    that                                                                                  classes                                              qualities, characteristics,     of                                                                                              if needed.                                                                                     runtime                                                                        at                                                                               even       and constraints                         that                           the pattern                                          represents.                                                                         changed,                                                          and

       Patterns allow you to say more with less. When you
        use a pattern in a description, other developers quickly
      know precisely the design you have in mind.
                                                                                      have you                                                                                   meetings      Talking               at the                    pattern                                level                                allows                                   you to                                               stay “in                                                                                design                                                            many                                                   How                                                                               degrade into                             Talking                                  about                                            software                                                   systems                                                            using       the design”                    longer.                                                                                        quickly                                                                           in that                                                              been        patterns allows you to keep the discussion at the design                         details?                                                                      implementation          level, without having to dive down to the nitty-gritty details
         of implementing objects and classes.
                                                             As your team begins to share
      Shared vocabularies can turbo-charge your              design ideas and experience in
      development team. A team well versed in design           terms of patterns, you will build
        patterns can move more quickly with less room for            a community of pattern users.
        misunderstanding.

      Shared vocabularies encourage more junior            Think about starting a patterns
      developers to get up to speed. Junior developers look       study group at your organization.
      up to experienced developers. When senior developers         Maybe you can even get paid while
      make use of design patterns, junior developers also become       you’re learning...
       motivated to learn them. Build a community of pattern
        users at your organization.


28      Chapter 1


---

## PDF page 67

intro to design patterns

How do I use Design Patterns?

We’ve all used off-the-shelf libraries and frameworks. We take them, write some code against their APIs,
compile them into our programs, and benefit from a lot of code someone else has written. Think about
the Java APIs and all the functionality they give you: network, GUI, IO, etc. Libraries and frameworks go
a long way toward a development model where we can just pick and choose components and plug them
right in. But...they don’t help us structure our own applications in ways that are easier to understand, more
maintainable, and more flexible. That’s where design patterns come in.
Design patterns don’t go directly into your code, they first go into your BRAIN. Once you’ve loaded your
brain with a good working knowledge of patterns, you can then start to apply them to your new designs,
and rework your old code when you find it’s degrading into an inflexible mess.


                                                                                                                                     fly behavior                                                                                                  Encapsulated
                                                                                                                                                                                                                                                                                               <<interface>>FlyBehavior
                                                                                                                                                                                                                                                                                                                                                                      fly()                                                        BRAIN                                                           Your
                                                                                                                                                                                                                                                 FlyNoWay

                                                                                                                                                                                                                                                                                                                                                                                                fly()                                                                                                                                                                                                                                                                                                                                                                                                                         fly!                                                                                                                                                                                                                                                               -can’t                                                                                                                                                                                                                                                                                                            nothing                                                                                                                                                                                                                         do{                                                                                                                                                                                                                             {FlyWithWings                                                                                                                                                                                                                                                                                                                                                         fly()                                                                                                                                                                                                                                                                                                                                          flying                                                                                                                                                                                                                                            duck                                                                                                                                                                                                                                                    }//                                                                                                                                                                                                                                                                                                                                   //implements
                                                                                                                                                                                                                           }                                                                                                                     DuckflyBehavior;                                                                                                                                                      FlyBehavior                                                                                                                                                                 quackBehavior;                                                                                                                         behavior                                                                                                                                            QuackBehavior                                                                                                      quack                                                                                                     Encapsulated                                                                                                                                                                                                                                     QuackBehavior<<interface>>
                                                                                                                                                                                                                                                                                       quack()                                                                                                                                                          swim()display()performQuack()performFly()setFlyBehavior()setQuackBehavior()                                                                                                                                                                                             methods...                                                                                                                                                                                               duck-like                                                                                                                 OTHER                                                                                                                                                                                                                                               MuteQuack                                                                                                                                                                                                           //
                                                                                                                                                                                                                       Squeak                                                                                                                                                                                                                                                                                                                           quack()                                                                                                                                                                                                                                                                                                                                      nothing{    -can’tquack!                                                                                                                                                                                                                                                     {                                                                                                                                                                                         Quack                                                                                                                                                                                                                                                                                             quack()                                                                                                                                                                                                                                                                          squeak                                                                                                                                                                                                                                                                                                duckie                                                                                                                                                              Duck                                                                                                                                                                                                                                                                          }//do                                                                                                                                                                                                                           {                                                                                                                                                               Decoy                                                                                                                                                                                                                                                 quack)                                                                                                                                                                                                                                        duckquacking                                                                                                                                                                                                                                                }//rubber                                                                                                                                        Duck                                                                                                                                              Rubber                                                                                                                                                                                                           duck}                                                                                                                                                                                                                       }//implements                                                                                                                                                                                                                                                                    like{ adecoy                                                                                                                    Duck                                                                                                                                                                                                                                                         display()//looks                                                                                                                    Redhead                                                                                                                                                                               }                                                                                                 Duck                                                                                                                                                                                                                               like{ arubberduck                                                                                                                                          {                                                                                                                                                                                                                    display()//looks                                                                                                                                                    }          Patterns                  ClientObject                                                                                                                                                           redhead                                                                                                       a                                                                                                                                                                                              like                                                                                                                                                             looks                                                                                                                                                                                    display()//                                                that}                                                                                                                   { a                                                holdsdisplay()//looksMallardlike                                                                                                                                                mallardstate   of

                                                                              8                                                            8
                                                                              8                                                                D                                                                                                og Object
                                                                                                                                    int                                                                              8
                      Subjec                                                                     t Object          8
                                                 t      Bunch                                                        DuckObjec                                                                      Cat Object      Objects
                                     MVC A                                                Mouse ObjectObservers      Dependent                                               Automatic update/notification             Controller
                                                                                                                     Model
                                                                                                                    Request                                                                     Your Code, now new                                                                 and improved with
                                                                                      View                                                                                 design patterns!


          If design patterns are so great, why          Aren’t libraries and frameworks             So, there are no libraries of designQ:               Q:               Q:
can’t someone build a library of them so I    also design patterns?                       patterns?
don’t have to?
                                             Frameworks and libraries are not              No, but you will learn later about                 A:               A:     Design patterns are higher level than      design patterns; they provide specific            patterns catalogs with lists of patterns thatA: libraries. Design patterns tell us how to         implementations that we link into our          you can apply to your applications.
structure classes and objects to solve certain    code. Sometimes, however, libraries and
problems, and it is our job to adapt those       frameworks make use of design patterns in
designs to fit our particular application.            their implementations. That’s great, because
                                         once you understand design patterns, you’ll
                                       more quickly understand APIs that are
                                                 structured around design patterns.


                                                                        you are here 4      29


---

## PDF page 68

why design patterns?


                   Patterns are nothing
               more than using OO
                  design principles...
                                           A common misconception,
                                                            but it’s more subtle than that.
                                                        You have much to learn...


  Skeptical Developer                                         Friendly Patterns Guru


           Developer: Okay, hmm, but isn’t this all just good object-oriented design; I
           mean as long as I follow encapsulation and I know about abstraction, inheritance,
           and polymorphism, do I really need to think about Design Patterns? Isn’t it pretty
            straightforward? Isn’t this why I took all those OO courses? I think Design Patterns
            are useful for people who don’t know good OO design.
          Guru: Ah, this is one of the true misunderstandings of object-oriented
            development: that by knowing the OO basics we are automatically going to be good at
              building flexible, reusable, and maintainable systems.
           Developer: No?
          Guru: No. As it turns out, constructing OO systems that have these properties is
            not always obvious and has been discovered only through hard work.
           Developer: I think I’m starting to get it. These, sometimes non-obvious, ways of
             constructing object-oriented systems have been collected...
          Guru: ...yes, into a set of patterns called Design Patterns.
           Developer: So, by knowing patterns, I can skip the hard work and jump straight to
             designs that always work?
          Guru: Yes, to an extent, but remember, design is an art. There will always be
             tradeoffs. But, if you follow well-thought-out and time-tested design patterns, you’ll
           be way ahead.
           Developer: What do I do if I can’t find a pattern?


30      Chapter 1


---

## PDF page 69

intro to design patterns


      Remember, knowing concepts
like abstraction, inheritance, and
polymorphism does not make you a good
object-oriented designer. A design guru
thinks about how to create flexible
designs that are maintainable and can
cope with change.


                                  Guru: There are some object-oriented principles that
                                           underlie the patterns, and knowing these will help you
                                        to cope when you can’t find a pattern that matches your
                                         problem.
                                   Developer: Principles? You mean beyond abstraction,
                                            encapsulation, and...
                                  Guru: Yes, one of the secrets to creating maintainable
                         OO systems is thinking about how they might change in the
                                           future, and these principles address those issues.


                                                                   you are here 4      31


---

## PDF page 70

your design toolbox


          Tools for your Design Toolbox
                You’ve nearly made it through the first chapter! You’ve
                 already put a few tools in your OO toolbox; let’s make a
                                                                  Knowing the OO basics                          list of them before we move on to Chapter 2.
                                                                                   does not make you a good
                                                          OO designer.
                                                                  Good OO designs are
                                                  the                      reusable, extensible, and                                               know                                              you                             Weassume    abstraction,                                                    basics    polymorphism,            Basics       OO                                                                   Patterns show you how to                                                         area     OO                                    like                               maintainable.                                                Ifyou                                                    encapsulation,                                                        out               build systems with good                                                                         pull                                                        inheritance.                 Abstraction                and                                           onthese,                                                          OO design qualities.                                                 rusty                                                     little       object-oriented                  Encapsulation                                                     favorite   thenskim          Patterns are proven                                          your                                                             review,                                                                                                      object-oriented                   Polymorphism                 bookand    again.                                                 chapter                            experience.                                                this                    Inheritance
                                                                   Patterns don’t give you
                                                                                            code, they give you       Principles                                                                general solutions to  OO
                                                                                            design problems. You                                      a closer look at                                                  taking                          varies.                                      be                                                                        also                                                 We’ll              what                                                   and                                                                                              apply                                                                                      them to your specific                                                  road                                             the      Encapsulate                                       down                                                                                          list.                                         these                                                     the                                                                                                           application.                                                 to                      over                                                more                                         few                                 a             composition                  adding      Favor                                                         Patterns aren’t invented,        inheritance.                                                                          they are discovered.            to interfaces, not       Program                                                     Most patterns and         implementations.                                                                            principles address issues
                                                    Throughout the                    of change in software.
                                                            book, think about
                                                how patterns rely          Most patterns allow some
                                                    on OO basics and                 part of a system to vary
                                                                       principles.                       independently of all other                                                                                                            parts.       Patterns   OO                           of algorithms,                              We often try to take what                   a family                      defines                                them          -                                                                                                      varies                                                                                                                            in a system                                                                                                and                               makes        Strategy                           one, and                                           algorithm                   each                                                                                            encapsulate                                                                                                                                                                                                    it.                                    lets the           encapsulates                                          use it.                        Strategy                                  that            interchangeable.  from clients                                      Patterns provide a          vary independently                                                                                         shared language that can
                                                                                      maximize the value of
                           One down, many to go!                                   your communication with
                                                                                                   other developers.


32      Chapter 1


---

## PDF page 71

intro to design patterns

         Design Patterns Crossword
                     Let’s give your right brain something to do.
                         It’s your standard crossword; all of the solution words
                   are from this chapter.

                               1                     2
                  3                                                    4            5
                                                              6
                  7
                                                              8
                                                                                    9
                                    10
                                                                                         11
                                        12
                                    13
                                                     14


                                    15
                  16


                                                          17
                  18

ACROSS
1. Paatterns can help us build ________ applications.     DOWN
4. Strategies can be __________.                               2. Patterns go into your _______.
7. Favor this over inheritance.                                   3. Duck that can't quack.
8. Development constant.                                        5. Rubber ducks make a _______.
9. Java IO, Networking, Sound.                                  6. ________ what varies.
10. Most patterns follow from OO _________.                 11. Grilled cheese with bacon.
12. Design patterns are a shared __________.               13. Rick was thrilled with this pattern.
14. High-level libraries.                                      16. Duck demo was located here.
15. Learn from the other guy's ___________.
17. Pattern that fixed the simulator.
18. Program to this, not an implementation.

                                                                        you are here 4      33


---

## PDF page 72

design puzzle solution

               Design Puzzle Solution


                          Character is the abstract class for all the other characters (King, Queen,
                           Knight, and Troll), while WeaponBehavior is an interface that all weapon
                            behaviors implement. So all actual characters and weapons are concrete
                                  classes.
                      To switch weapons, each character calls the setWeapon() method, which
                                         is defined in the Character superclass. During a fight the useWeapon()
                       method is called on the current weapon set for a given character to inflict
                             great bodily damage on another character.
                  Abstract


                                      Character
                              WeaponBehavior weapon
                                             fight()
                               setWeapon(WeaponBehavior w) {
                                     this.weapon = w;                     A Character HAS-A                                                 }
                                                                WeaponBehavior.

            King                             Knight
   fight() { ... }                                         fight() { ... }
             Queen                                           Troll
         fight() { ... }                                                fight() { ... }                                                          <<interface>>
                                                                                              WeaponBehavior
                                                                                                          useWeapon()


                                                                                 SwordBehavior              BowAndArrowBehavior
                                                                                               useWeapon() { // implements                useWeapon() { // implements
                                                                                                    swinging a sword }                          shooting an arrow with a bow                                                                                                        KnifeBehavior                    }AxeBehavior
                                                                                                                 useWeapon() { // implements              useWeapon() { // implements
                                                                                                                                        cutting with a knife }                     chopping with an axe }                                               could                                        object                       ANY                           that                                          of                     Note                              the WeaponBehaviora tube                           implement   a paper clip,                             interface—say,         sea bass.                                      mutated                              or a                             toothpaste,


34      Chapter 1


---

## PDF page 73

intro to design patterns


                            Which of the following are disadvantages of using subclassing to provide
                                     specific Duck behavior? (Choose all that apply.) Here’s our solution.


❏  A. Code is duplicated across subclasses.   ❏  D.  It’s hard to gain knowledge of all duck behaviors.
❏  B. Runtime behavior changes are difficult. ❏  E. Ducks can’t fly and quack at the same time.
❏  C. We can’t make ducks dance.      ❏   F.  Changes can unintentionally affect other ducks.


                             What are some factors that drive change in your applications?
                               You might have a very different list, but here’s a few of ours. Look
                                         familiar? Here’s our solution.

My customers or users decide they want something else, or they want new functionality.
My company decided it is going with another database vendor and it is also purchasing its data
from another supplier that uses a different data format. Argh!
Well, technology changes and we’ve got to update our code to make use of protocols.
We’ve learned enough building our system that we’d like to go back and do things a little better.


                                                                 you are here 4      35


---

## PDF page 74

crossword solution

          Design Patterns Crossword Solution


                          1                     2                  F  L  E X  I  B  L  E
             3                                                    4            5       D                     R          R  E U S  E D
                                                         6         E                  A     E         Q
             7         C O M  P O S  I  T  I O N           U
                                                         8       O                 N     C H A N G  E
                                                                               9        Y                       A           A  P  I  S
                              10       D            P  R  I N  C  I  P  L  E  S     K
                                                                                    11       U                        S               J
                                   12         C            V O  C A  B  U  L  A  R  Y    A
                              13         K        O                  L                C
                                                14                    B           F  R  A M  E W O  R  K  S
                  S              T                B
                              15                    E X  P  E  R  I  E N  C  E       E
             16      M          R                         N
       A          V                         N
                                                     17       U          E            S  T  R  A T  E  G  Y
             18          I N T  E  R  F A  C  E


36      Chapter 1
