# 12: compound patterns: Patterns of Patterns

_Extracted from PDF pages 531-600. Text only; images and diagrams are not embedded._


---

## PDF page 531

12 compound patterns
    Patterns
        of Patterns


 Who would have ever guessed that Patterns could work together?
 You’ve already witnessed the acrimonious Fireside Chats (and you haven’t even seen the Pattern
 Death Match pages that the editor forced us to remove from the book), so who would have
 thought patterns can actually get along well together? Well, believe it or not, some of the most
 powerful OO designs use several patterns together. Get ready to take your pattern skills to the
 next level; it’s time for compound patterns.


                                                                           this is a new chapter      493


---

## PDF page 532

patterns can work together

Working together

One of the best ways to use patterns is to get them out of the house so
they can interact with other patterns. The more you use patterns the
more you’re going to see them showing up together in your designs. We
have a special name for a set of patterns that work together in a design
that can be applied over many problems: a compound pattern. That’s right,
we are now talking about patterns made of patterns!

You’ll find a lot of compound patterns in use in the real world. Now
that you’ve got patterns in your brain, you’ll see that they are really just
patterns working together, and that makes them easier to understand.

We’re going to start this chapter by revisiting our friendly ducks in the
SimUDuck duck simulator. It’s only fitting that the ducks should be here
when we combine patterns; after all, they’ve been with us throughout
the entire book and they’ve been good sports about taking part in lots
of patterns. The ducks are going to help you understand how patterns
can work together in the same solution. But just because we’ve combined
some patterns doesn’t mean we have a solution that qualifies as a
compound pattern. For that, it has to be a general-purpose solution that
can be applied to many problems. So, in the second half of the chapter
we’ll visit a real compound pattern: the Model-View-Controller, otherwise
known as MVC. If you haven’t heard of MVC, you will, and you’ll find
MVC is one of the most powerful compound patterns in your design
toolbox.


           Patterns are often used together and
          combined within the same design solution.

      A compound pattern combines two or
          more patterns into a solution that solves a
            recurring or general problem.


494      Chapter 12


---

## PDF page 533

compound patterns

Duck reunion

As you’ve already heard, we’re going to get to work with the ducks again. This
time the ducks are going to show you how patterns can coexist and even
cooperate within the same solution.

We’re going to rebuild our duck simulator from scratch and give it some
interesting capabilities by using a bunch of patterns. Okay, let’s get started...

  1   First, we’ll create a Quackable interface.
       Like we said, we’re starting from scratch. This time around, the Ducks are
       going to implement a Quackable interface. That way we’ll know what things
        in the simulator can quack()—like Mallard Ducks, Redhead Ducks, Duck
        Calls, and we might even see the Rubber Duck sneak back in.

         public interface Quackable {                    only need to do                                                       Quackables             public void quack();                             well: Quack!                                                 one thing         }


  2   Now, some Ducks that implement Quackable
     What good is an interface without some classes to implement it? Time to
       create some concrete ducks (but not the “lawn art” kind, if you know what
     we mean).
                                                               Your standard                                                                               duck.                                                                    Mallard         public class MallardDuck implements Quackable {
             public void quack() {
                 System.out.println("Quack");
             }
         }
         public class RedheadDuck implements Quackable {
             public void quack() {                                                                               We’ve got to have some variation                 System.out.println("Quack");                                                                 of species if we want this to be
             }                                                       an interesting simulator.
         }


                                                                       you are here 4      495


---

## PDF page 534

adding more ducks

      This wouldn’t be much fun if we didn’t add other kinds of Ducks too.
     Remember last time? We had duck calls (those things hunters use—they
      are definitely quackable) and rubber ducks.

           public class DuckCall implements Quackable {
               public void quack() {
                   System.out.println("Kwak");           A DuckCall that quacks but                                                                               doesn’t sound quite like the real               }                                                                                     thing.           }
           public class RubberDuck implements Quackable {
               public void quack() {
                   System.out.println("Squeak");             A RubberDuck that makes a
                                                                                  squeak when it quacks.               }
           }

 3    Okay, we’ve got our ducks; now all we need is a simulator.
       Let’s cook up a simulator that creates a few ducks and makes sure their
      quackers are working...                                                                                        Here’s our main() method                                                                                            everything going.           public class DuckSimulator {                             to get
               public static void main(String[] args) {                   DuckSimulator simulator = new DuckSimulator();       We create a simulator
                   simulator.simulate();                                   and then call its
               }                                                                               simulate() method.
               void simulate() {
                   Quackable mallardDuck = new MallardDuck();                                                               We need some ducks, so                   Quackable redheadDuck = new RedheadDuck();                                                                                 here we create one of                   Quackable duckCall = new DuckCall();                                                                               each Quackable...                   Quackable rubberDuck = new RubberDuck();
                   System.out.println("\nDuck Simulator");
                   simulate(mallardDuck);                      ...then we simulate
                   simulate(redheadDuck);                  each one.
                   simulate(duckCall);
                   simulate(rubberDuck);                             Here we overload the simulate()
               }                                                     method to simulate just one duck.
               void simulate(Quackable duck) {
                   duck.quack();                                                  Here we let polymorphism do its magic: no
               }                                               matter what kind of Quackable gets passed in,           }                                                 the simulate() method asks it to quack.

496      Chapter 12


---

## PDF page 535

compound patterns


  Not too            exciting yet, but we   haven’t                                                          File Edit  Window Help ItBetterGetBetterThanThis        added                patterns!             % java DuckSimulator
                                  Duck Simulator
                                  Quack
                                  Quack
                                  Kwak
                                  Squeak

                                           They all implement the same Quackable                                                                          implementations allow                                                         interface, but their                                            them to quack in their own way.

     It looks like everything is working; so far, so good.

4   When ducks are around, geese can’t be far.
    Where there is one waterfowl, there are probably two. Here’s a Goose
      class that has been hanging around the simulator.

       public class Goose {                                           A Goose is a honker,           public void honk() {                                                           not a quacker.
               System.out.println("Honk");
           }
       }


      Let’s say we wanted to be able to use a Goose anywhere we’d want to use a
     Duck. After all, geese make noise; geese fly; geese swim. Why can’t we have
    Geese in the simulator?
    What pattern would allow Geese to easily intermingle with Ducks?


                                                                     you are here 4      497


---

## PDF page 536

goose adapter

 5  We need a goose adapter.
     Our simulator expects to see Quackable interfaces. Since geese
       aren’t quackers (they’re honkers), we can use an adapter to adapt
      a goose to a duck.
                                                                          an Adapter                                                                     Remember,                                                                                                         interface,        public class GooseAdapter implements Quackable {              the target                                                                            implements                                                                                                Quackable.            Goose goose;                                            which in this case is
            public GooseAdapter(Goose goose) {         The constructor takes the
                this.goose = goose;                          goose we are going to adapt.
            }
            public void quack() {                When quack is called, the call is delegated
                goose.honk();                        to the goose’s honk() method.
            }
        }
 6   Now geese should be able to play in the simulator, too.
        All we need to do is create a Goose and wrap it in an adapter
      that implements Quackable, and we should be good to go.
        public class DuckSimulator {
            public static void main(String[] args) {
                DuckSimulator simulator = new DuckSimulator();
                simulator.simulate();
            }
            void simulate() {                                   We make a Goose that acts                Quackable mallardDuck = new MallardDuck();                                                                                                    like a Duck by wrapping the                                                                                            GooseAdapter.                Quackable redheadDuck = new RedheadDuck();          Goose in the                Quackable duckCall = new DuckCall();
                Quackable rubberDuck = new RubberDuck();
                Quackable gooseDuck = new GooseAdapter(new Goose());
                System.out.println("\nDuck Simulator: With Goose Adapter");
                                                            Once the Goose is wrapped, we can treat                simulate(mallardDuck);                simulate(redheadDuck);                     it just like other duck Quackable objects.
                simulate(duckCall);
                simulate(rubberDuck);
                simulate(gooseDuck);
            }
            void simulate(Quackable duck) {
                duck.quack();
            }
        }

498      Chapter 12


---

## PDF page 537

compound patterns


7   Now let’s give this a quick run...
     This time when we run the simulator, the list of objects passed
     to the simulate() method includes a Goose wrapped in a duck
     adapter. The result? We should see some honking!


                                                                 File Edit  Window Help GoldenEggs
                            % java DuckSimulator
                              Duck Simulator: With Goose Adapter
                              Quack
                              Quack
                              Kwak     There’s the goose! Now the
     Goose can quack with the       Squeak
     rest of the Ducks.            Honk


         Quackology


           Quackologists are fascinated by all aspects of Quackable behavior. One
            thing Quackologists have always wanted to study is the total number of
          quacks made by a flock of ducks.
        How can we add the ability to count duck quacks without having to
         change the duck classes?
        Can you think of a pattern that would help?


                                                                             J. Brewer,
                                                                  Park Ranger and
                                                                         Quackologist


                                                                     you are here 4      499


---

## PDF page 538

duck decorator


  8   We’re going to make those Quackologists happy and give
      them some quack counts.
     How? Let’s create a decorator that gives the ducks some new
       behavior (the behavior of counting) by wrapping them with a
      decorator object. We won’t have to change the Duck code at all.

                                         As with Adapter, we need to             QuackCounter is a decorator.                                               implement the target interface.                                                                                We’ve got an instance variable
                                                                        to hold on to the quacker
                                                                                  we’re decorating.      public class QuackCounter implements Quackable {
          Quackable duck;                                       And we’re counting ALL
          static int numberOfQuacks;                                       quacks, so we’ll use a static
                                                                                           variable to keep track.
          public QuackCounter (Quackable duck) {
              this.duck = duck;                                We get the reference to the
          }                                                                Quackable we’re decorating
                                                                                             in the constructor.
          public void quack() {
              duck.quack();                   When quack() is called, we delegate the call              numberOfQuacks++;                                                   to the Quackable we’re decorating...
          }
                                                                     ...then we                                                                         increase the number of quacks.          public static int getQuacks() {
              return numberOfQuacks;
          }
      }                                                              We’re adding one other method to the
                                                              decorator. This static method just
                                                              returns the number of quacks that
                                                             have occurred in all Quackables.


500      Chapter 12


---

## PDF page 539

compound patterns

9  We need to update the simulator to create decorated ducks.
    Now, we must wrap each Quackable object we instantiate in a
    QuackCounter decorator. If we don’t, we’ll have ducks running
    around making uncounted quacks.
    public class DuckSimulator {
        public static void main(String[] args) {
            DuckSimulator simulator = new DuckSimulator();                                                                    Each time we create a            simulator.simulate();                                                                                Quackable, we wrap it with        }                                                                 a new decorator.
        void simulate() {
            Quackable mallardDuck = new QuackCounter(new MallardDuck());
            Quackable redheadDuck = new QuackCounter(new RedheadDuck());
            Quackable duckCall = new QuackCounter(new DuckCall());
            Quackable rubberDuck = new QuackCounter(new RubberDuck());
            Quackable gooseDuck = new GooseAdapter(new Goose());
            System.out.println("\nDuck Simulator: With Decorator");
                                                       The park ranger told us he            simulate(mallardDuck);                                                                        didn’t want to count geese            simulate(redheadDuck);                                                                            honks, so we don’t decorate it.            simulate(duckCall);
            simulate(rubberDuck);
            simulate(gooseDuck);                                                                                             Here’s where we
                                                                                   gather the quacking            System.out.println("The ducks quacked " +                                                                                          behavior for the                               QuackCounter.getQuacks() + " times");                                                                                               Quackologists.        }
        void             simulate(Quackable duck) {                                                             Nothing changes here; the decorated            duck.quack();                                                                                   Quackables.        }                                                        objects are still
    }

                                                 File Edit  Window Help DecoratedEggs
                       % java DuckSimulator
   Here’s the             Duck Simulator: With Decorator
   output!               Quack
                        Quack
                        Kwak
      Remember,          Squeak
      we’re not          Honk                geese.       counting           The ducks quacked 4 times
                       %
                                                                    you are here 4      501


---

## PDF page 540

duck factory


                  This quack counting is great. We’re learning
                  things we never knew about the little quackers.
               But we’re finding that too many quacks aren’t
                 being counted. Can you help?


                     You have to decorate objects to
                        get decorated behavior.

                                He’s right, that’s the problem with wrapping objects:
                             you have to make sure they get wrapped or they don’t
                                    get the decorated behavior.

                      Why don’t we take the creation of ducks and localize
                                                     it in one place; in other words, let’s take the duck
                                   creation and decorating and encapsulate it.

                         What pattern does that sound like?


  10  We need a factory to produce ducks!
      Okay, we need some quality control to make sure our ducks get wrapped.
      We’re going to build an entire factory just to produce them. The factory
       should produce a family of products that consists of different types of
       ducks, so we’re going to use the Abstract Factory Pattern.
       Let’s start with the definition of the AbstractDuckFactory class:
                                                                            We’re defining an abstract factory                                                                    that subclasses will implement to                                                                           create different families.
       public abstract class AbstractDuckFactory {

           public abstract Quackable createMallardDuck();
           public abstract Quackable createRedheadDuck();
           public abstract Quackable createDuckCall();
           public abstract Quackable createRubberDuck();
       }
                                              Each method creates one kind of duck.


502      Chapter 12


---

## PDF page 541

compound patterns

Next we’ll create a factory that creates ducks without decorators, just to
get the hang of the factory:
        public class DuckFactory extends AbstractDuckFactory {
            public Quackable createMallardDuck() {             DuckFactory extends
                return new MallardDuck();                        the abstract factory.
            }
            public Quackable createRedheadDuck() {                                                             Each method creates a product:                return new RedheadDuck();                                                                                             Quackable.                                                        a particular kind of            }                                                        The actual product is unknown to                                                                                                just knows it’s                                                                the simulator — it            public Quackable createDuckCall() {                                                                         getting a Quackable.                return new DuckCall();
            }
            public Quackable createRubberDuck() {
                return new RubberDuck();
            }
        }
                                                                                     CountingDuckFactory
Now let’s create the factory we really want, the CountingDuckFactory:               also extends the
                                                                                         abstract factory.
        public class CountingDuckFactory extends AbstractDuckFactory {
            public Quackable createMallardDuck() {
                return new QuackCounter(new MallardDuck());            Each method wraps the
            }                                                                       Quackable with the quack
                                                                                             counting decorator. The
            public Quackable createRedheadDuck() {                            simulator will never know
                return new QuackCounter(new RedheadDuck());             the difference; it just
            }                                                                          gets back a Quackable.
                                                                           But now our rangers can
            public Quackable createDuckCall() {                             be sure that all quacks
                return new QuackCounter(new DuckCall());                  are being counted.
            }
            public Quackable createRubberDuck() {
                return new QuackCounter(new RubberDuck());
            }
        }


                                                                       you are here 4      503


---

## PDF page 542

families of ducks

 11   Let’s set up the simulator to use the factory.
    Remember how Abstract Factory works? We create a polymorphic method
     that takes a factory and uses it to create objects. By passing in different
     factories, we get to use different product families in the method.
    We’re going to alter the simulate() method so that it takes a factory and
     uses it to create ducks.                                                we create                                                                                          First
                                                                            the factory     public class DuckSimulator {                                            that we’re going
         public static void main(String[] args) {                         to pass into                                                                                                          simulate()             DuckSimulator simulator = new DuckSimulator();                the
                                                                                     method.             AbstractDuckFactory duckFactory = new CountingDuckFactory();

             simulator.simulate(duckFactory);
         }
                                                                            The simulate()         void simulate(AbstractDuckFactory duckFactory) {                                                                                  method takes an
             Quackable mallardDuck = duckFactory.createMallardDuck();      AbstractDuckFactory
             Quackable redheadDuck = duckFactory.createRedheadDuck();      and uses it to create
             Quackable duckCall = duckFactory.createDuckCall();              ducks rather than
                                                                                                        instantiating them             Quackable rubberDuck = duckFactory.createRubberDuck();                                                                                                             directly.             Quackable gooseDuck = new GooseAdapter(new Goose());

             System.out.println("\nDuck Simulator: With Abstract Factory");

             simulate(mallardDuck);
             simulate(redheadDuck);
             simulate(duckCall);
             simulate(rubberDuck);
             simulate(gooseDuck);
                                                                                    Nothing changes
             System.out.println("The ducks quacked " +                      here! Same ol’ code.
                                QuackCounter.getQuacks() +
                               " times");
         }

         void simulate(Quackable duck) {
             duck.quack();
         }
     }

504      Chapter 12


---

## PDF page 543

compound patterns


                              Here’s the output using the factory...


                                                        File Edit  Window Help EggFactory
                           % java DuckSimulator
     as last time,             Duck Simulator: With Abstract FactorySamebut this time                Quack      ensuring that           Quack we’re the ducks are all             Kwak           because decorated                  Squeak
 we are using the             Honk  CountingDuckFactory.                           4 quacks were counted
                           %


                                          We’re still directly instantiating Geese by relying on concrete
                                                 classes. Can you write an Abstract Factory for Geese? How should
                                                                    it handle creating “goose ducks”?


                                                                     you are here 4      505


---

## PDF page 544

flock of ducks


                                                       It’s getting a little difficult to manage
                                                                 all these different ducks separately.
                                            Is there any way you can help us
                                         manage ducks as a whole, and perhaps even
                                                   allow us to manage a few duck “families”
                                             that we’d like to keep track of?


                      Ah, he wants to manage a flock
                         of ducks.

                              Here’s another good question from Ranger Brewer:
                    Why are we managing ducks individually?

                        Quackable mallardDuck = duckFactory.createMallardDuck();
   This isn’t very           Quackable redheadDuck = duckFactory.createRedheadDuck();
    manageable!             Quackable duckCall = duckFactory.createDuckCall();
                        Quackable rubberDuck = duckFactory.createRubberDuck();
                        Quackable gooseDuck = new GooseAdapter(new Goose());

                        simulate(mallardDuck);
                        simulate(redheadDuck);
                        simulate(duckCall);
                        simulate(rubberDuck);
                        simulate(gooseDuck);

                       What we need is a way to talk about collections of
                             ducks and even subcollections of ducks (to deal with
                               the family request from Ranger Brewer). It would
                                  also be nice if we could apply operations across the
                           whole set of ducks.

                       What pattern can help us?


506      Chapter 12


---

## PDF page 545

compound patterns

12    Let’s create a flock of ducks (well, actually a flock of Quackables).
     Remember the Composite Pattern that allows us to treat a collection of
      objects in the same way as individual objects? What better composite than
     a flock of Quackables!
      Let’s step through how this is going to work:
                                                                       to implement                                                                         needs                                                      the composite                                              Remember,                                                                           Our                                                                            leaf elements.                                                                    as the                                             the same interface                                                   leaf elements are Quackables.
                                                                        We’re using an ArrayList inside each Flock to
      public class Flock implements Quackable {          hold the Quackables that belong to the Flock.
          List<Quackable> quackers = new ArrayList<Quackable>();

          public void add(Quackable quacker) {                   The add() method adds a
              quackers.add(quacker);                                   Quackable to the Flock.
          }

          public void quack() {
              Iterator<Quackable> iterator = quackers.iterator();
              while (iterator.hasNext()) {
                  Quackable quacker = iterator.next();
                  quacker.quack();
              }                                                                                                       too.                                                                                  Quackable                                                                      a                                                                                                               is                                                                         Flock                                                                the                                                                                                    all,                                                  method — after                                              quack()                                   for the          }                        Now                                                                                              Flock. Here                                                                                       entire                                                                       the                                                                          over                                                             work                                                            to                                                           needs                                                     Flock                                                              in                                      method                                      quack()                          The                                                                                             element.      }                                                                                each                                                                          on                                                                           quack()                                                                                       call                                                          and                                                    ArrayList                                              the                                         through                           we iterate


           Code Up Close
                                   Did you notice that we tried to sneak a Design Pattern
                                  by you without mentioning it?
       public void quack() {                                                                         There it is! The Iterator           Iterator<Quackable> iterator = quackers.iterator();                                                                               Pattern at work!           while (iterator.hasNext()) {
               Quackable quacker = iterator.next();
               quacker.quack();
           }
       }


                                                                      you are here 4      507


---

## PDF page 546

duck composite

 13   Now we need to alter the simulator.
     Our composite is ready; we just need some code to round up the
      ducks into the composite structure.
public class DuckSimulator {
    // main method here                                                         Create all the
                                                                                               Quackables,    void simulate(AbstractDuckFactory duckFactory) {                                                                                                    just like before.        Quackable redheadDuck = duckFactory.createRedheadDuck();
        Quackable duckCall = duckFactory.createDuckCall();
        Quackable rubberDuck = duckFactory.createRubberDuck();
        Quackable gooseDuck = new GooseAdapter(new Goose());
        System.out.println("\nDuck Simulator: With Composite - Flocks");
        Flock flockOfDucks = new Flock();                                                                                          First we create a Flock and
        flockOfDucks.add(redheadDuck);                                      load it up with Quackables.
        flockOfDucks.add(duckCall);
        flockOfDucks.add(rubberDuck);                                                                     Then we create a new        flockOfDucks.add(gooseDuck);                                                                                 Flock of mallards.
        Flock flockOfMallards = new Flock();
                                                                                             Here we’re        Quackable mallardOne = duckFactory.createMallardDuck();                                                                                                       creating a        Quackable mallardTwo = duckFactory.createMallardDuck();                                                                                                                        little family of        Quackable mallardThree = duckFactory.createMallardDuck();                                                                                                                      mallards...        Quackable mallardFour = duckFactory.createMallardDuck();
        flockOfMallards.add(mallardOne);                                       ...and adding them to the        flockOfMallards.add(mallardTwo);                                                                                  Flock of mallards.        flockOfMallards.add(mallardThree);
        flockOfMallards.add(mallardFour);                             Then we add the Flock of
                                                                                            mallards to the main flock.        flockOfDucks.add(flockOfMallards);
        System.out.println("\nDuck Simulator: Whole Flock Simulation");
        simulate(flockOfDucks);                                       Let’s test out the entire Flock!
        System.out.println("\nDuck Simulator: Mallard Flock Simulation");
        simulate(flockOfMallards);                                                             Then let’s just test out the mallard Flock.
        System.out.println("\nThe ducks quacked " +
                           QuackCounter.getQuacks() +
                           " times");                                        Finally, let’s give the
    }                                                                            Quackologist the data.
    void simulate(Quackable duck) {
        duck.quack();
    }                                             Nothing needs to change here; a Flock is a Quackable!}

508      Chapter 12


---

## PDF page 547

compound patterns

Let’s give it a spin...


                                File Edit  Window Help FlockADuck
               % java DuckSimulator
              Duck Simulator: With Composite - Flocks
              Duck Simulator: Whole Flock Simulation
              Quack                                                  Here’s the first flock.              Kwak
              Squeak
              Honk
              Quack
              Quack
              Quack
              Quack

              Duck Simulator: Mallard Flock Simulation
              Quack                      And now the mallards.
              Quack
                                                The data looks              Quack                                                        good (remember the              Quack                                                               goose doesn’t get
                                                                counted).
              The ducks quacked 11 times


                                           Safety versus transparency

        You might remember that in the Composite Pattern chapter the composites (the Menus) and the
          leaves (the MenuItems) had the same exact set of methods, including the add() method. Because
         they had the same set of methods, we could call methods on MenuItems that didn’t really make
         sense (like trying to add something to a MenuItem by calling add()). The benefit of this was that the
          distinction between leaves and composites was transparent: the client didn’t have to know whether
               it was dealing with a leaf or a composite; it just called the same methods on both.

          Here, we’ve decided to keep the composite’s child maintenance methods separate from the leaf
         nodes: that is, only Flocks have the add() method. We know it doesn’t make sense to try to add
        something to a Duck, and in this implementation, you can’t. You can only add() to a Flock. So
           this design is safer—you can’t call methods that don’t make sense on components—but it’s less
          transparent. Now the client has to know that a Quackable is a Flock in order to add Quackables to it.

        As always, there are tradeoffs when you do OO design and you need to consider them as you create
         your own composites.


                                                                      you are here 4      509


---

## PDF page 548

duck observer


                       The Composite is working great! Thanks!
                    Now we have the opposite request: we also
                         need to track individual ducks. Can you give
                           us a way to keep track of individual duck
                            quacking in real time?


                Can you say “observer”?

                                   It sounds like the Quackologist would like to observe individual
                       duck behavior. That leads us right to a pattern made for observing
                           the behavior of objects: the Observer Pattern.

 14    First we need an interface for our Subject.
     Remember that the Subject is the object being observed. Let’s call it
      something more memorable—how about Observable? An Observable needs
      methods for registering and notifying observers. We could also have a
      method for removing observers, but we’ll keep the implementation simple
      here and leave that out.                                                                       is the interface                                                                       QuackObservable                                                                 that Quackables should implement                                                                          if they want to be observed.
       public interface QuackObservable {
           public void registerObserver(Observer observer);
                                                                                       It has a method for registering           public void notifyObservers();                                                                                      Observers. Any object implementing      }                                                                          the Observer interface can listen
                                                                            to quacks. We’ll define the Observer                                              It also has a method for                                                                                    interface in a sec.                                             notifying the observers.


     Now we need to make sure all Quackables implement this interface...

       public interface Quackable extends QuackObservable {
           public void quack();
      }                                                                        So, we extend the Quackable
                                                                                interface with QuackObserver.

510      Chapter 12


---

## PDF page 549

compound patterns


                                                                          Stop looking at me.
 15   Now, we need to make sure all the concrete                                                                                      You’re making me
      classes that implement Quackable can handle                                                                                            nervous!
      being a QuackObservable.
    We could approach this by implementing registration and
       notification in each and every class (like we did in Chapter
       2). But we’re going to do it a little differently this time:
      we’re going to encapsulate the registration and notification
     code in another class, call it Observable, and compose it
      with QuackObservable. That way, we only write the real
     code once and QuackObservable just needs enough code to
      delegate to the helper class Observable.
       Let’s begin with the Observable helper class.

                                                                                              QuackObserverable
                              functionality                     the                           all          implementsObservable                                                        Observable                                                              must                            We                                                                      implement                                                                              QuackObservable                             observable.                    an                  be               to            needs  Quackablea                                                        because                                                               these                                                                     are                                                                   the                                                                       same                                                                      method                                                                                                                  calls                          and have                             class                  a                    into             plug it    need tojust                                                  that                                                            are                                                                     going                                                                  to                                                                     be                                                                           delegated                                                                                 to it.that class delegate to Observable.                                                                                              In the constructor we get                                                                                                QuackObservable      public class Observable implements QuackObservable {                passed the                                                                              that is using this object          List<Observer> observers = new ArrayList<Observer>();                                                                             to manage its observable          QuackObservable duck;                                                                                                 behavior. Check out the
                                                                                            notifyObservers() method
          public Observable(QuackObservable duck) {                           below; you’ll see that when              this.duck = duck;                                        a notify occurs, Observable
         }                                                                                  passes this object along so                                                                               that the observer knows
                                                                                      which object is quacking.          public void registerObserver(Observer observer) {
              observers.add(observer);                                        Here’s the code for
         }                                                                                registering an observer.

          public void notifyObservers() {
              Iterator iterator = observers.iterator();
              while (iterator.hasNext()) {
                  Observer observer = iterator.next();
                  observer.update(duck);                                                             And the code for doing
             }                                                    the notifications.
         }
     }           Now let’s see how a Quackable class uses this helper...

                                                                      you are here 4      511


---

## PDF page 550

quack decorators are observables too


 16    Integrate the helper Observable with the Quackable classes.
      This shouldn’t be too bad. All we need to do is make sure the Quackable classes
      are composed with an Observable and that they know how to delegate to it. After
       that, they’re ready to be Observables. Here’s the implementation of MallardDuck;
      the other ducks are the same.
      public class MallardDuck implements Quackable {    Each Quackable has an                                                                          Observable instance variable.          Observable observable;
          public MallardDuck() {                                          In the constructor, we create an
              observable = new Observable(this);                Observable and pass it a reference
          }                                                           to the MallardDuck object.
          public void quack() {
              System.out.println("Quack");                        When we quack, we need
              notifyObservers();                                       to let the observers know
          }                                                                about it.
          public void registerObserver(Observer observer) {
              observable.registerObserver(observer);
          }
          public void notifyObservers() {
              observable.notifyObservers();                 Here are our two QuackObservable
          }                                                         methods. Notice that we just
                                                                           delegate to the helper.      }


                               We haven’t changed the implementation of one Quackable, the
                                        QuackCounter decorator. We need to make it an Observable too.
                                 Why don’t you write that one:


512      Chapter 12


---

## PDF page 551

compound patterns


17   We’re almost there! We just need to work on the Observer side
     of the pattern.

     We’ve implemented everything we need for the Observables; now we
     need some Observers. We’ll start with the Observer interface:
                                     The Observer interface just has one                                             method, update(), which is passed the                                               QuackObservable that is quacking.

      public interface Observer {
          public void update(QuackObservable duck);
     }


    Now we need an Observer: where are
     those Quackologists?!
                                         We need to implement the Observer interface or else
                                            we won’t be able to register with a QuackObservable.

     public class Quackologist implements Observer {

         public void update(QuackObservable duck) {
             System.out.println("Quackologist: " + duck + " just quacked.");
         }
     }
                                          The                                                             Quackologist                                                                                          is                                                                                     simple;                                                                                   it just                                                                                   has                                                                                   one                                                   method,                                                                  update(),                                                                     which                                                                                  prints                                                                          out                                                                            the                                                    Quackable that just quacked.


                                                                      you are here 4      513


---

## PDF page 552

flock composites are observables too


                                    What if a Quackologist wants to observe an entire flock? What does that
                                 mean anyway? Think about it like this: if we observe a composite, then
                                             we’re observing everything in the composite. So, when you register with
                                          a flock, the flock composite makes sure you get registered with all its
                                              children (sorry, all its little quackers), which may include other flocks.

                                 Go ahead and write the Flock observer code before we go any further.


514      Chapter 12


---

## PDF page 553

compound patterns


18  We’re ready to observe. Let’s update the
     simulator and give it a try:

    public class DuckSimulator {
        public static void main(String[] args) {
            DuckSimulator simulator = new DuckSimulator();
            AbstractDuckFactory duckFactory = new CountingDuckFactory();

            simulator.simulate(duckFactory);
        }

        void simulate(AbstractDuckFactory duckFactory) {

            // create duck factories and ducks here

            // create flocks here

            System.out.println("\nDuck Simulator: With Observer");
                                                                                                All we do here is create
            Quackologist quackologist = new Quackologist();         a Quackologist and set
            flockOfDucks.registerObserver(quackologist);               him as an observer of
                                                                             the flock.
            simulate(flockOfDucks);
                                                                                     This time we’ll            System.out.println("\nThe ducks quacked " +                                                                         we just simulate
                               QuackCounter.getQuacks() +              the entire flock.
                               " times");
        }
                                                                       Let’s give it a try        void simulate(Quackable duck) {
                                                                 and see how it works!            duck.quack();
        }
    }


                                                                      you are here 4      515


---

## PDF page 554

the duck finale

This is the big finale. Five—no, six—patterns have come together to
create this amazing Duck Simulator. Without further ado, we present
DuckSimulator!


                              File Edit  Window Help DucksAreEverywhere
                % java DuckSimulator
                                                                     After each
              Duck Simulator: With Observer                           quack, no
              Quack                                                  matter what
              Quackologist: Redhead Duck just quacked.            kind of quack
              Kwak                                                               it was, the
              Quackologist: Duck Call just quacked.                observer gets a
              Squeak                                                               notification.
              Quackologist: Rubber Duck just quacked.
              Honk
              Quackologist: Goose pretending to be a Duck just quacked.
              Quack
              Quackologist: Mallard Duck just quacked.
              Quack
              Quackologist: Mallard Duck just quacked.
              Quack
              Quackologist: Mallard Duck just quacked.                                                                  And the              Quack                                                                                       quackologist still
              Quackologist: Mallard Duck just quacked.        gets his counts.
              The Ducks quacked 7 times.


                                                                                     We’re going to talk more about this in the     So this was a compound pattern?         So the real beauty of DesignQ:               Q:                                         next chapter, but you only want to apply                                            Patterns is that I can take a problem and                                                                                                 patterns when and where they make sense.                                                   start                                                applying                                                           patterns to it until I have a     No,            this was                      just                   a set of                               patterns                                                                              You                                                                                           never                                                                                            want to                                                                                                                                     start                                                                                                                     out                                                                                                                              with                                                                                                                              the                                                                                                                                             intentionA:                                               solution.                                                  Right? working         together.            A                compound                               pattern                                                is a                                                                                                          of using                                                                                                         patterns                                                                                                                                    just                                                                                                                                         for                                                                                                                       the                                                                                                           sake                                                                                                                                              of                                                                                                                                                                                                                                     it. You
set of a few patterns that are combined to                                                   should consider the design of the Duck
solve a general problem. We’re just about                                              Wrong. We went through this exercise     Simulator to be forced and artificial. But hey,                 A:
 to take a look at the Model-View-Controller      with Ducks to show you how patterns can             it was fun and gave us a good idea of how
compound pattern; it’s a collection of a few     work together. You’d never actually want to      several patterns can fit into a solution.
 patterns that has been used over and over in   approach a design like we just did. In fact,
many design solutions.                         there may be solutions to parts of the Duck
                                               Simulator for which some of these patterns
                                         were big-time overkill. Sometimes just using
                                        good OO design principles can solve a
                                           problem well enough on its own.

516      Chapter 12


---

## PDF page 555

compound patterns


What did we do?

We started with a bunch of Quackables...

A goose came along and wanted to act like a Quackable too. So we
used the Adapter Pattern to adapt the goose to a Quackable. Now, you can call quack() on a
goose wrapped in the adapter and it will honk!

Then, the Quackologists decided they wanted to count quacks. So we
used the Decorator Pattern to add a QuackCounter decorator that keeps track of the number
of times quack() is called, and then delegates the quack to the Quackable it’s wrapping.

But the Quackologists were worried they’d forget to add the
QuackCounter decorator. So we used the Abstract Factory Pattern to create ducks
for them. Now, whenever they want a duck, they ask the factory for one, and it hands back
a decorated duck. (And don’t forget, they can also use another duck factory if they want an
undecorated duck!)

We had management problems keeping track of all those ducks and
geese and quackables. So we used the Composite Pattern to group Quackables
into Flocks. The pattern also allows the Quackologist to create subFlocks to manage duck
families. We used the Iterator Pattern in our implementation by using java.util’s iterator in
ArrayList.

The Quackologists also wanted to be notified when any Quackable
quacked. So we used the Observer Pattern to let the Quackologists register as Quackable
Observers. Now they’re notified every time any Quackable quacks. We used iterator again
in this implementation. The Quackologists can even use the Observer Pattern with their
composites.


     That was quite a Design Pattern
     workout. You should study the class
    diagram on the next page and then
    take a relaxing break before continuing
      on with Model-View-Controller.


                                                            you are here 4      517


---

## PDF page 556

duck's-eye view

A bird’s duck’s-eye view: the class diagram

We’ve packed a lot of patterns into one small duck simulator! Here’s the big picture of what we did:


            DuckSimulator
                                                     uses a factory to create Ducks.                                  DuckSimulator


                                                                   AbstractDuckFactory

                                                                                 createMallardDuck()
                                                                           createRedheadDuck()
                                                                                   createDuckCall()
                                                                             createRubberDuck()


                                                    DuckFactory                 CountingDuckFactory

                                                           createMallardDuck()                      createMallardDuck()
                                                       createRedheadDuck()                   createRedheadDuck()
                                                            createDuckCall()                                                                                                       createDuckCall()
                                                        createRubberDuck()                                                                                               createRubberDuck()                 Here are two different
                                                                                                 factories that produce
                                                                                the same family of                                                                                               DuckFactory                                                                                              products. The
                                                                                            creates ducks, and the
                          If a class                                                  CountingDuckFactory                                                                                            creates Ducks wrapped in                            implements                             Observer, that                                            QuackCounter decorators.                                                                            <<interface>>                         means it can                   Observer
                            observe Quackables,     update(QuackObservable)                       and will be                                       notified                          whenever a
                          Quackable quacks.
                                                                        Quackologist

                                                                            update(QuackObservable)
     We only              implemented one kind of      for the                                    Observer              Quackables — the     But any                class that       Quackologist.                        implements the      interface can                                     Observer                   observe      implementing a        ducks...how about                  BirdWatcher                                observer?

518      Chapter 12


---

## PDF page 557

compound patterns


                                        The QuackObservable interface                                                            gives us a set of methods that                                                 any Observable must implement.
                                                                     Each Quackable has an
                                                   <<interface>>                                      instance of Observable
                                            QuackObservable                               to keep track of theirQuackable is the                 interface                                                      registerObserver(Observer)                                 observers and notify themthat all classes that have                                                         notifyObservers()quacking                                                                       when the Quackable quacks.        behavior                 implement.

                                                                                           Observable

                                                    <<interface>>                                        List observers
                                               Quackable                               QuackObservable duck
                                                      quack()                                                                                                             registerObserver(Observer)
                                                                                                                  notifyObservers()

                         MallardDuck                                    GooseAdapter

                         quack()  RedheadDuck                              Goose goose
                         registerObserver(Observer)                             quack()    DuckCall                                    quack()               This Adapter...                          notifyObservers()
                             registerObserver(Observer)                                 registerObserver(Observer)
                                 quack()  RubberDuck                                notifyObservers()                              notifyObservers()
                                 registerObserver(Observer)
                                    quack()                                   notifyObservers()
                                     registerObserver(Observer)                             Flock
                                      notifyObservers()                                                                                                           List ducks
          We have two kinds of                               add(Quackable)quack()                     ...and this
                                                                                        registerObserver(Observer)      Composite...             Quackables: ducks and
                                                                                            notifyObservers()            other things that want
             Quackable behavior: like
            the GooseAdapter, which                        QuackCounter
             wraps a Goose and makes                       Quackable duck               it look like a Quackable;                                                                                    getQuacks()                  ...and this               Flock, which is a                                      quack()                 Decorator             Quackable Composite, and                         registerObserver(Observer)        all act like             QuackCounter, which adds                        notifyObservers()            Quackables!               behavior to Quackables.


                                                                you are here 4      519


---

## PDF page 558

the model view controller song

The King of Compound Patterns
If Elvis were a compound pattern, his name would be Model-View-Controller,
and he’d be singing a little song like this...
 Model, View, Controller                               Model a bottle of fine Chardonnay
 Lyrics and music by James Dempsey.                      Model all the glottal stops people say
                                                     Model the coddling of boiling eggs
 MVC’s a paradigm for factoring your code                  You can model the waddle in Hexley’s legs
 into functional segments, so your brain does not explode.
 To achieve reusability, you gotta keep those boundaries       Model View, you can model all the models that pose for GQ
 clean                                                Model View Controller
 Model on the one side, View on the other, the Controller’s                                  Java!                                                            Sodoes in between.                                                         View objects tend to be controls used to display and edit
                                                              Cocoa’s got a lot of those, well written to its credit.
 View                                                    Take an NSTextView, hand it any old Unicode string
                                                 The user can interact with it, it can hold most anything                                     Creamy
                                             Controller       But the view don’t know about the Model
                                                  That string could be a phone number or the works of
                                                                 Aristotle
                                                      Keep the coupling loose
                                                       and so achieve a massive level of reuse                               Model
                                                     Model View, all rendered very nicely in aqua blue
 Model View, it’s got three layers like Oreos do             Model View Controller
 Model View Controller
 Model View, Model View, Model View Controller               You’re probably wondering now
                                                                You’re probably wondering how
 Model objects represent your application’s raison d’être      Data flows between Model and View
 Custom objects that contain data, logic, and et cetera      The Controller has to mediate
 You create custom classes, in your app’s problem domain       Between each layer’s changing state
 you can choose to reuse them with all the views              To synchronize the data of the two
 but the model objects stay the same.                           It pulls and pushes every changed value

 You can model a throttle and a manifold                  Model View, mad props to the smalltalk crew!
 Model the toddle of a two year old                      Model View Controller


520      Chapter 12


---

## PDF page 559

compound patterns

                                                How we gonna deep six all that glue
Model View, it’s pronounced Oh Oh not Ooo Ooo            Model View Controller
Model View Controller
                                                              Controllers know the Model and View very intimately
There’s a little left to this story                       They often use hardcoding which can be foreboding for
                                                                    reusabilityA few more miles upon this road
                                                 But now you can connect each model key that you selectNobody seems to get much glory                                                         to any view propertyFrom writing the controller code
                                                And once you start bindingWell, the model’s mission critical                                                                                             I think you’ll be finding less code in your source treeAnd gorgeous is the view
I might be lazy, but sometimes it’s just crazy                                                             Yeah, I know I was elated by the stuff they’ve automatedHow much code I write is just glue                                                      and the things you get for freeAnd it wouldn’t be so tragic
But the code ain’t doing magic                                                And I think it bears repeatingIt’s just moving values through                                                                                     all the code you won’t be needing
                                                     when you hook it up in IB.And I don’t mean to be vicious                                                                                                     Swing.                                                                                           UsingBut it gets repetitious                                                    Model View even handles multiple selections tooDoing all the things controllers do                                                    Model View Controller
And I wish I had a dime                                                    Model View, bet I ship my application before youFor every single time                                                    Model View ControllerI sent a TextField StringValue.

Model View


   Ear
   power
                      Don’t just read! After all, this is a Head First book...check out this URL:

                     https://www.youtube.com/watch?v=YYvOGPMLVDo

                            Sit back and give it a listen.


                                                                      you are here 4      521


---

## PDF page 560

mvc is patterns put together


                          Cute song, but is that really supposed
                           to teach me what Model-View-
                             Controller is? I’ve tried learning MVC
                          before and it made my brain hurt.


                                 Design Patterns are your key
                                     to understanding MVC.

                                We were just trying to whet your appetite
                                               with the song. Tell you what, after you finish
                                                reading this chapter, go back and listen to the
                                             song again—you’ll have more fun.

                                                                It sounds like you’ve had a bad run-in with
                           MVC before? Most of us have. You’ve
                                              probably had other developers tell you it’s
                                           changed their lives and could possibly create
                                             world peace. It’s a powerful compound
                                                    pattern, for sure, and while we can’t claim it
                                                          will create world peace, it will save you hours
                                                     of writing code once you know it.

                                           But first you have to learn it, right? Well,
                                                       there’s going to be a big difference this time
                                           around because now you know patterns!

                                                 That’s right, patterns are the key to MVC.
                                             Learning MVC from the top down is difficult;
                                               not many developers succeed. Here’s the
                                                      secret to learning MVC: it’s just a few patterns
                                                         put together. When you approach learning
                           MVC by looking at the patterns, all of a
                                           sudden it starts to make sense.

                                                       Let’s get started. This time around, you’re
                                              going to nail MVC!


522      Chapter 12


---

## PDF page 561

compound patterns

Meet Model-View-Controller

Imagine you’re using your favorite music player, like iTunes. You can use its interface to add
new songs, manage playlists, and rename tracks. The player takes care of maintaining a little
database of all your songs along with their associated names and data. It also takes care of
playing the songs and, as it does, the user interface is constantly updated with the current song
title, the running time, and so on.

Well, underneath it all sits Model-View-Controller...


                                                                        thethe           the                                              youyouuseuse  andand             view                                                                                    interfaceinterface            display                                                                                    actionsactions                is                                                                     youryour       updated                                                                         thethe               for                                                       gogototo                     You see the song          you                                                                                         controllercontroller                          display update and
                       hear the new song                               “Play new song”
                           playing


        View                                              Controller
                    Model tells the
                       view the state has                             Controller asks
                                                                      Player model to                     changed                   class Player {
                                                                play(){}               begin playing
            the                                      rip(){}               song              model           the                                       burn(){}                        the controller              viewofanotifies              }                              manipulates           instate                     change                                                                       the model
  The model contains all the state,       Model
  data, and application logic needed
  to maintain and play mp3s.

                                                                       you are here 4      523


---

## PDF page 562

mvc up close

A closer look...

The music player description gives us a high-level view of MVC, but it really
doesn’t help you understand the nitty-gritty of how the compound pattern
works, how you’d build one yourself, or why it’s such a good thing. Let’s start by
stepping through the relationships among the model, view, and controller, and
then we’ll take second look from the perspective of Design Patterns.


                             CONTROLLER
                                   Takes user input and figures out
                                   what it means to the model.
                                                        MODEL
                                                                  The model holds all   VIEW                                                                           the data, state, and                                          Here’s the creamy    Gives you a presentation                      it lives in                                            controller;                                     application logic. The    of      the model.              The                     view           the middle.                              themodelviewis obliviousand controller,to    usually          gets the                   state
    and data it needs to                                                          although it provides an
    display directly from                                                          interface to manipulate
   the model.                                                             and retrieve its
                                                                                state and it can send
                                                    2         notifications of state
                                                                            changes to observers.                                                                Change your
          1 The user did            Controller                state
                 something
                           3 Change your
                                                display                                                         class Player {
                                                                                                                                        play(){}
                                    4                                                rip(){}
                                                                                                                          burn(){}                                                   I’ve changed!                                                                                                                      }
                                                      Model
         View                      5
                                      I need your state                                                                                                Here’s the
      This is the user                            information                               model; it
        interface.                                                                            handles all
                                                                                                    application data
                                                                             and logic.


524      Chapter 12


---

## PDF page 563

compound patterns


 1    You’re the user—you interact with the view.
     The view is your window to the model. When you do something to the view (like click
      the Play button), then the view tells the controller what you did. It’s the controller’s
       job to handle that.
 2   The controller asks the model to change its state.
     The controller takes your actions and interprets them. If you click a button,
          it’s the controller’s job to figure out what that means and how the model
       should be manipulated based on that action.

 3   The controller may also ask the view to change.
     When the controller receives an action from the view, it may need to tell the view
       to change as a result. For example, the controller could enable or disable certain
       buttons or menu items in the interface.

 4   The model notifies the view when its state has changed.
     When something changes in the model, based either on some action you took (like
        clicking a button) or some other internal change (like the next song in the playlist
       has started), the model notifies the view that its state has changed.

 5   The view asks the model for state.
     The view gets the state it displays directly from the model. For instance, when the
      model notifies the view that a new song has started playing, the view requests the
       song name from the model and displays it. The view might also ask the model for
       state as the result of the controller requesting some change in the view.


                                                                              You could; however, you don’t want to for two     Does the controller ever become an           All the controller does is take userQ:               Q:                                        reasons. First, you’ll complicate your viewobserver of the model?                      input from the view and send it to the                                                                                 code because it now has two responsibilities:                                         model, correct? Why have it at all if that                                                                                managing the user interface and dealing                                                              all                                                                                it                                           does?                                         Why                                                            not                                                                          just                                                              have the                                                                    code      Sure.             In           some                   designs                            the                                    controller        is                                                                                                   with the logic                                                                                                                        of                                                                                    how to                                                                                                                              control the                                                                                                                       model.A:                                                  in                                               the                                              view                                                                 itself?                                                                      In                                                      most                                                              cases                                                                                           isn’t                                                                                the registers          with              the               model                    and                                    is notified                                                                                    Second,                                                                                                         you’re                                                                                                                                       tightly                                                                                                                   coupling                                                                                                                       your                                                                                                                        view
 of changes. This can be the case when         controller just calling a method on the         to the model. If you want to reuse the view
something in the model directly affects the     model?                                         with another model, forget it. The controller
user interface controls. For instance, certain                                                 separates the logic of control from the view
states in the model may dictate that some                                           The controller does more than just       and decouples the view from the model.                 A:
 interface items be enabled or disabled. If so,   “send it to the model”; it is responsible for      By keeping the view and controller loosely
 it’s really the controller’s job to ask the view      interpreting the input and manipulating the      coupled, you are building a more flexible and
 to update its display accordingly.             model based on that input. But your real         extensible design, one that can more easily
                                              question is probably, “Why can’t I just do that   accommodate change down the road.
                                                         in the view code?”

                                                                       you are here 4      525


---

## PDF page 564

the patterns in mvc

Understanding MVC as a set of Patterns

We’ve already suggested that the best path to learning MVC is to see it for what it is: a
set of patterns working together in the same design.

Let’s start with the model: the model uses Observer to keep the views and controllers
updated on the latest state changes. The view and the controller, on the other hand,
implement the Strategy Pattern. The controller is the strategy of the view, and it
can be easily exchanged with another controller if you want different behavior. The
view itself also uses a pattern internally to manage the windows, buttons, and other
components of the display: the Composite Pattern.

Let’s take a closer look:

                         Strategy
                      The view and controller implement the classic Strategy Pattern: the
                       view is an object that is configured with a strategy. The controller
                         provides the strategy. The view is concerned only with the visual
                         aspects of the application, and delegates to the controller any
                          decisions about the interface behavior. Using the Strategy Pattern also
                       keeps the view decoupled from the model because it is the controller
                           that is responsible for interacting with the model to carry out user
                           requests. The view knows nothing about how this gets done.


                    The user did                                                                   Change your
                        something         Controller                state   Observer
                                        Change your
                                                   display                                                                                                                                         class Player {    Composite                                                                                                     play(){}
                                                                                                                            rip(){}
                                                                                                                            burn(){}
                                                                                                                     }                                                      I’ve changed!
                                                        Model
          View
                                           I need your state
The display consists of a nested set of                   information         The model implements the Observer Pattern
windows, panels, buttons, text labels, and so                                 to keep interested objects updated when
on. Each display component is a composite                                    state changes occur. Using the Observer
(like a window) or a leaf (like a button). When                                Pattern keeps the model completely
the controller tells the view to update, it                                 independent of the views and controllers. It
only has to tell the top view component, and                                allows us to use different views with the same
Composite takes care of the rest.                                        model, or even use multiple views at once.

526      Chapter 12


---

## PDF page 565

compound patterns

Observer                                                                                                             All these observers will be                                   Observers                                                                                               notified whenever state
       Observable                                                                     changes in the model.
                    My state has
                              changed!
                 class Foo {                                          View
                  void bar()
                {
                    doBar();
                 }
                }
        Model                                                        View
                                                                     Controller
                                     Any object that’s
                                              interested in state        I’d             like              to                  register                                                      model                                                the                                                          in                                             changes         as           an              observer                                                             The model has no dependencies on                                                   the                              View                                                  with                                                  registers                                          model as an observer.           viewers or controllers!

Strategy                                                                                        controller is the                               The user did                      The                                                                             for the                                     something                              strategy                                                                            the object                                                                                             view — it’s                                                                     that knows how to The view                                                                                                          actions.                                                Controller      handle the user delegates to
 the controller
 to handle the                                                  We can swap in
user actions.                                                                 another behavior for            View                                                the view by                                                                                              changing                                                                      the controller.
  The view only worries about presentation. The controller     Controller
   worries about translating user input to actions on the model.

                                      paint()
Composite                                                             The view is a composite                                                                of GUI components (labels,                                                                                   buttons, text entry, etc.).                                                                                       component                                                              The top-level                                                                                               components,                                                                                    contains other
                                                                             which contain other                                                                               and so on until                                                                                 components,        View                                                         you get to the leaf nodes.


                                                                       you are here 4      527


---

## PDF page 566

mvc and the dj view

Using MVC to control the beat...

It’s your time to be the DJ. When you’re a DJ it’s all about the beat. You might start
your mix with a slowed, down-tempo groove at 95 beats per minute (BPM) and
then bring the crowd up to a frenzied 140 BPM of trance techno. You’ll finish off
your set with a mellow 80 BPM ambient mix.

How are you going to do that? You have to control the beat, and you’re going to
build the tool to get you there.

Meet the Java DJ View
Let’s start with the view of the tool. The view allows you to create
a driving drumbeat and tune its beats per minute...


                                             A pulsing bar shows the beat in real time.


                                            A display shows the current BPMs and is
                                                                  automatically set whenever the BPM changes.
 The view has two
  parts, the part
  for viewing the
  state of the model
  and the part for
   controlling things.
                                                                   You can enter a specific BPM and click                                120                                                                   the Set button to set a specific beats
                                                                          per minute, or you can use the increase
                                                                 and decrease buttons for fine tuning.

                             Decreases         Increases
                          the BPM by     the BPM by
                            one beat per     one beat per
                               minute.          minute.


528      Chapter 12


---

## PDF page 567

compound patterns

 Here are a few more ways to control the DJ View...
                                                         You use the Stop                              You can start the        button to shut                                beat kicking by         down the beat                                     the Start                                      choosing                   generation.                               menu item in the “DJ
                                   Control” menu.

                               Notice Stop is             Notice Start is
                                   disabled until you            disabled after
                                start the beat.            the beat has
                                                             started.
                                                                                                              All user actions are
                                                                                             sent to the controller.
The controller is in the middle...
The controller sits between the view and
model. It takes your input, like selecting
Start from the DJ Control menu, and turns
it into an action on the model to start the     The controller takes input
beat generation.                           from the user and figures
                                            out how to translate that
                                                    into requests on the model.
                                                Controller

Let’s not forget about the model underneath it all...
You can’t see the model, but you can hear it. The
model sits underneath everything else, managing the
beat and driving the speakers.
              atMod           e              el         B
                                                on()
    The BeatModel is the heart of
    the application. It implements             setBPM()   off()
    the logic to start and stop
    the beat, set the BPM, and              getBPM()
    generate the sound.

           The model also allows us to
              obtain its current state through
            the getBPM() method.

                                                                       you are here 4      529


---

## PDF page 568

the dj model, view, and controller

Putting the pieces together


              The beat is set at 119 BPM and you
                  would like to increase it to 120.


                                                                                   Click the
                                                                                    increase beat
                                                                                        button...


                     View                                                                               ...which results in the
                                                                      controller being invoked.


                                                                   The controller asks
                                                                             the model to update
                                                                                                    its BPM by one.
                                         Controller

             You see the beat bar
                pulse every 1/2 second.
                          atMod                     e                        el                                              Because the BPM is 120, the  B   View                                                                                     on()                                                 view gets a beat notification                                                every 1/2 second.
                                                                                setBPM()   off()
                                                                           getBPM()

             The view is updated            View is notified that the
               to 120 BPM.            BPM changed. It calls                                        getBPM() on the model state.


530      Chapter 12


---

## PDF page 569

compound patterns

Building the pieces

Okay, you know the model is responsible for maintaining all the data, state, and any
application logic. So what’s the BeatModel got in it? Its main job is managing the beat,
so it has state that maintains the current beats per minute and code to play an audio
clip to create the beat that we hear. It also exposes an interface that lets the controller
manipulate the beat and lets the view and controller obtain the model’s state. Also,
don’t forget that the model uses the Observer Pattern, so we also need some methods to
let objects register as observers and send out notifications.

Let’s check out the BeatModelInterface before
looking at the implementation:
                                                                              after                                                                                         called                                                                         gets                      public interface BeatModelInterface {  This                                                                                           is instantiated.                                                                  BeatModel                          void initialize();
    These are the methods                                                                        These methods turn the     the controller will         void on();                                                                           beat generator on and off.      use to direct the
     model based on user                          void off();     interaction.                                                               This method sets the beats per
                                                                                     minute. After it is called, the beat
                          void setBPM(int bpm);                   frequency changes immediately.

                          int getBPM();                           The getBPM() method
                                                                                     returns the current BPMs,    These methods allow                                                          or 0 if the generator is off.    the view and the          void registerObserver(BeatObserver o);
     controller to get
     state and to become       void removeObserver(BeatObserver o);
      observers.
                          void registerObserver(BPMObserver o);

                          void removeObserver(BPMObserver o);
                     }

                      This should look familiar.              We’ve split this into two kinds of observers:                     These methods allow objects          observers that want to be notified on every                     to register as observers for           beat, and observers that just want to be
                       state changes.                        notified when the beats per minute change.


                                                                       you are here 4      531


---

## PDF page 570

the beat model

Now let’s have a look at the concrete BeatModel class
                                                                   We implement the
                                                                                 BeatModeIInterface and Runnable.public class BeatModel implements BeatModelInterface, Runnable {
   List<BeatObserver> beatObservers = new ArrayList<BeatObserver>();
   List<BPMObserver> bpmObservers = new ArrayList<BPMObserver>();
   int bpm = 90;                            We use these to start and                These Lists hold the two kinds of   Thread thread;                                     stop the beat thread.                        observers (Beat and BPM observers).   boolean stop = false;
   Clip clip;           This is the audio clip we play for the beat.      The bpm variable holds the frequency
                                                                   of beats — by default, 90 BPM.  public void initialize() {
      try {
         File resource = new File("clap.wav");                                This method does setup         clip = (Clip) AudioSystem.getLine(new Line.Info(Clip.class));                                                                                         for the beat track.         clip.open(AudioSystem.getAudioInputStream(resource));
      }
      catch(Exception ex) { /* ... */}
   }   public void on() {               The on() method sets the BPMs to the default,
      bpm = 90;                        and starts the thread to play the beat.
      notifyBPMObservers();
      thread = new Thread(this);
      stop = false;
      thread.start();
   }                                    And off() shuts it down by setting BPMs to   public void off() {
      stopBeat();              0 and stopping the thread playing the beat.
      stop = true;
   }
   public void run() {      while (!stop) {                          The run() method runs the beat thread, playing         playBeat();                              a beat determined by the BPM, and notifies the         notifyBeatObservers();                    beat observers that a beat’s been played. The loop
         try {                                          terminates when we select Stop from the menu.
            Thread.sleep(60000/getBPM());
         } catch (Exception e) {}
      }                                   The setBPM() method is the way   }                                        the controller manipulates the            Ready Bake Code   public void setBPM(int bpm) {                                              beat. It sets the bpm variable, and              This model uses an      this.bpm = bpm;                                                           audio clip to generate                                                notifies all BPM Observers that      notifyBPMObservers();                                                            beats. You can check   }                                   the BPM has changed.                        out the complete
                                                                                   implementation of all   public int getBPM() {       The getBPM() method just returns      return bpm;                                                                                       the DJ classes                                                                                                                      in the Java                                    the current beats per minute.   }                                                                                       source                                                                                                                                         files, available                                                                                           on
   // Code to register and notify observers                                              site,the wickedlysmart.comor look at the code
   // Audio code to handle the beat                                                  at the end of the chapter.}

532      Chapter 12


---

## PDF page 571

compound patterns

The View

Now the fun starts; we get to hook up a view and visualize the BeatModel!

The first thing to notice about the view is that we’ve implemented it so that it is displayed in two
separate windows. One window contains the current BPM and the pulse; the other contains
the interface controls. Why? We wanted to emphasize the difference between the interface that
contains the view of the model and the rest of the interface that contains the set of user controls.
Let’s take a closer look at the two parts of the view:
                                                         We’ve separated
                                                  the view of the
                                                     model from the
                                                          view with the
                                                               controls.
  The DJ view
   displays two
   aspects of the
   BeatModel...
                                         ...and a “beat bar”              ...the current                               that pulses in sync           beats per                                 with the beat, driven            minute, from the                                                            This                                  the BeatObserver                               by                                                                               is the          BPMObserver                                                          you                                                                  use                                       notifications.                                                          to                                                                  part of the view that              notifications...                                                                       change the beat. This                                                               view passes                                                    to the                                                                             everything you do on                                                                               controller.


     Our BeatModel makes no assumptions about the view. The model is implemented using the
      Observer Pattern, so it just notifies any view registered as an observer when its state changes.
     The view uses the model’s API to get access to the state. We’ve implemented one type of view;
      can you think of other views that could make use of the notifications and state in the BeatModel?

     A light show that is based on the real-time beat.
     A textual view that displays a music genre based on the BPM (ambient, downbeat, techno, etc.).


                                                                       you are here 4      533


---

## PDF page 572

the dj view

Implementing the View                                                      The code on these two
                                                          pages is just an outline!The two parts of the view—the view of the model, and
the view with the user interface controls—are displayed                    What we’ve done here is
in two windows, but live together in one Java class. We’ll                                split ONE class into TWO,
first show you just the code that creates the view of the                       showing you one part of
model, which displays the current BPM and the beat bar.            the view on this page, and the other
Then we’ll come back on the next page and show you just            part on the next page. All this code is
the code that creates the user interface controls, which                really in ONE class—DJView.java. It’s
displays the BPM text entry field, and the buttons.                        all listed at the end of the chapter.

                          DJView is an observer for both real-time beats and BPM changes.
public class DJView implements ActionListener,  BeatObserver, BPMObserver {
    BeatModelInterface model;               The view holds a reference to both the model and    ControllerInterface controller;                                                    the controller. The controller is only used by the    JFrame viewFrame;                                                          control interface, which we’ll go over in a sec...    JPanel viewPanel;                                      Here, we create a few    BeatBar beatBar;                                   components for the display.    JLabel bpmOutputLabel;
    public DJView(ControllerInterface controller, BeatModelInterface model) {
        this.controller = controller;                                                             The constructor gets a reference        this.model = model;                                                                       to the controller and the model,        model.registerObserver((BeatObserver)this);                                                                     and we store references to those        model.registerObserver((BPMObserver)this);                                                                                              in the instance variables.    }
                                                             We also register as a BeatObserver and    public void createView() {                                                                    a BPMObserver of the model.        // Create all Swing components here
    }
                                                  The updateBPM() method is called when a state
    public void updateBPM() {                         change occurs in the model. When that happens, we
        int bpm = model.getBPM();                    update the display with the current BPM. We can get
        if (bpm == 0) {                                    this value by requesting it directly from the model.            bpmOutputLabel.setText("offline");
        } else {
            bpmOutputLabel.setText("Current BPM: " + model.getBPM());
        }
    }                                                  Likewise, the updateBeat() method is called
                                         when the model starts a new beat. When that    public void updateBeat() {
                                                  happens, we need to pulse our beat bar. We do        beatBar.setValue(100);
                                                   this by setting it to its maximum value (100)    }
}                                         and letting it handle the animation of the pulse.

534      Chapter 12


---

## PDF page 573

compound patterns

Implementing the View, continued...

Now, we’ll look at the code for the user interface controls part of the view. This view lets you control
the model by telling the controller what to do, which in turn, tells the model what to do. Remember,
this code is in the same class file as the other view code.

public class DJView implements ActionListener,  BeatObserver, BPMObserver {
    BeatModelInterface model;
    ControllerInterface controller;
    JLabel bpmLabel;
    JTextField bpmTextField;
    JButton setBPMButton;
    JButton increaseBPMButton;
    JButton decreaseBPMButton;
    JMenuBar menuBar;
    JMenu menu;
    JMenuItem startMenuItem;
    JMenuItem stopMenuItem;
    public           void                createControls()                                 {                                                           This                                                         method                                                                           creates                                                                                                              all the                                                                                            controls                                                                                     and                                                                                                                places                                                                                         them        //           Create                  all Swing components                                       here                                                                         in the                                                                          interface.                                                                                It also                                                                                   takes                                                                                        care of                                                                                        the                                                                                                      menu.    }                                                                                        When                                                       the stop or start items are chosen, the corresponding                                                       methods are called on the controller.    public void enableStopMenuItem() {
        stopMenuItem.setEnabled(true);
    }
                                                                          All these methods allow the start and
    public void disableStopMenuItem() {                stop items in the menu to be enabled and
        stopMenuItem.setEnabled(false);                 disabled. We’ll see that the controller uses    }                                                         these to change the interface.
    public void enableStartMenuItem() {
        startMenuItem.setEnabled(true);
    }
                                                                This method is called when a button is clicked.    public void disableStartMenuItem() {
        startMenuItem.setEnabled(false);
    }                                                                                       If the Set button is
                                                                                                        clicked, then it is passed
    public void actionPerformed(ActionEvent event) {                      on to the controller
        if (event.getSource() == setBPMButton) {                             along with the new bpm.
            int bpm = Integer.parseInt(bpmTextField.getText());
            controller.setBPM(bpm);
        } else if (event.getSource() == increaseBPMButton) {           Likewise, if the increase or
            controller.increaseBPM();                                        decrease button is clicked,
        } else if (event.getSource() == decreaseBPMButton) {           this information is passed
            controller.decreaseBPM();                                      on to the controller.
        }
    }
}

                                                                       you are here 4      535


---

## PDF page 574

the dj controller

Now for the Controller

It’s time to write the missing piece: the controller. Remember the controller
is the strategy that we plug into the view to give it some smarts.

Because we are implementing the Strategy Pattern, we need to start with
an interface for any Strategy that might be plugged into the DJ View. We’re
going to call it ControllerInterface.
                                                                     Here are all the
                                                                   methods the view can
                                                                                            call on the controller.          public interface ControllerInterface {
             void start();                                                               These should look familiar to you after seeing
             void stop();                                 the model’s interface. You can stop and start
             void increaseBPM();                         the beat generation and change the BPM.
                                                                    This interface is “richer” than the BeatModel             void decreaseBPM();                                                                        interface because you can adjust the BPMs             void setBPM(int bpm);                                                                   with increase and decrease.
         }


       Design Puzzle
                                      You’ve seen that the view and controller together make use of the Strategy
                                           Pattern. Can you draw a class diagram of the two that represents this pattern?


536      Chapter 12


---

## PDF page 575

compound patterns

And here’s the implementation of the controller:                                                             The controller implements
                                                                      the ControllerInterface.

 public class BeatController implements ControllerInterface {
     BeatModelInterface model;                               The controller is the creamy stuff
     DJView view;                                                                      in the middle of the MVC Oreo                                                                                         cookie, so it is the object that
                                                                              gets to hold on to the view and the     public BeatController(BeatModelInterface model) {                                                                          model and glues it all together.         this.model = model;
         view = new DJView(this, model);                                                    The controller is passed the         view.createView();                                                              model in the constructor and         view.createControls();                                                             then creates the view.         view.disableStopMenuItem();
         view.enableStartMenuItem();
         model.initialize();
     }                                         When you choose Start from the user                                                            interface menu, the controller turns     public void start() {                       the model on and then alters the user         model.on();                                   interface so that the Start menu         view.disableStartMenuItem();           item is disabled and the Stop menu
         view.enableStopMenuItem();              item is enabled.
     }
                                                            Likewise, when you choose Stop from     public void stop() {
                                                   the menu, the controller turns the         model.off();
                                                     model off and alters the user interface         view.disableStopMenuItem();
                                                           so that the Stop menu item is disabled         view.enableStartMenuItem();
                                                  and the Start menu item is enabled.     }
                                                                       NOTE: the controller is
     public void increaseBPM() {                                                 making the intelligent
         int bpm = model.getBPM();      If the increase button is clicked,             decisions for the view.
         model.setBPM(bpm + 1);         the controller gets the current          The view just knows how
     }                          BPM from the model, adds one,           to turn menu items on
                                            and then sets a new BPM.               and off; it doesn’t know
     public void decreaseBPM() {                                              the situations in which
         int bpm = model.getBPM();                                                       it should disable them.                                            Same thing here, only we subtract         model.setBPM(bpm - 1);                                                   one from the current BPM.     }
     public void setBPM(int bpm) {
         model.setBPM(bpm);                       Finally, if the user interface is used to
     }                                              set an arbitrary BPM, the controller
 }                                                        instructs the model to set its BPM.

                                                                       you are here 4      537


---

## PDF page 576

putting it all together

Putting it all together...

We’ve got everything we need: a model, a view, and a controller.
Now it’s time to put them all together! We’re going to see and
hear how well they work together.

All we need is a little code to get things started; it won’t take much:


public class DJTestDrive {

    public static void main (String[] args) {                                                                            First create a model...        BeatModelInterface model = new BeatModel();
        ControllerInterface controller = new BeatController(model);
    }
                                                                                   ...then create a controller and}                                                                           pass it the model. Remember,
                                                                the controller creates the view,
                                                                           so we don’t have to do that.And now for a test run...


                                               File Edit  Window Help LetTheBassKickMake sure you have
the file clip.wav at       % java DJTestDrive
 the top level of the      %                                                                Run this... code folder!

                                                                     ...and you’ll see this.


Things to try

  1   Start the beat generation with the Start menu item;
      notice the controller disables the item afterward.
  2  Use the text entry along with the increase and
     decrease buttons to change the BPM. Notice how the
     view display reflects the changes despite the fact that
         it has no logical link to the controls.
  3   Notice how the beat bar always keeps up with the beat
      since it’s an observer of the model.
  4  Put on your favorite song and see if you can match the
      beat by using the increase and decrease controls.
  5  Stop the generator. Notice how the controller disables
      the Stop menu item and enables the Start menu item.


538      Chapter 12


---

## PDF page 577

compound patterns

Exploring Strategy

Let’s take the Strategy Pattern just a little further to get a
better feel for how it is used in MVC. We’re going to see
another friendly pattern pop up too—a pattern you’ll often
see hanging around the MVC trio: the Adapter Pattern.

Think for a second about what the DJ View does: it displays
a beat rate and a pulse. Does that sound like something else?
How about a heartbeat? It just so happens that we have a
heart monitor class; here’s the class diagram:

                     HeartModel                We’ve got a method for getting                   getHeartRate()                  the current heart rate.
                   registerBeatObserver()
                  registerBPMObserver()                                       And luckily, its developers knew about the
                                // other heart methods                                          Beat and BPM Observer interfaces!


            It certainly would be nice to reuse our current view with the HeartModel, but we need a
        controller that works with this model. Also, the interface of the HeartModel doesn’t match what
       the view expects because it has a getHeartRate() method rather than a getBPM(). How would
      you design a set of classes to allow the view to be reused with the new model? Jot down your
       class design ideas below.


                                                                       you are here 4      539


---

## PDF page 578

mvc and adapter

Adapting the Model

For starters, we’re going to need to adapt the HeartModel to a BeatModel. If we don’t, the
view won’t be able to work with the model, because the view only knows how to getBPM(),
and the equivalent heart model method is getHeartRate(). How are we going to do this?
We’re going to use the Adapter Pattern, of course! It turns out that this is a common
technique when working with MVC: use an adapter to adapt a model to work with existing
controllers and views.
Here’s the code to adapt a HeartModel to a BeatModel:                   We need to implement the
                                                                         target interface — in this
                                                                                         case, BeatModelInterface.
 public class HeartAdapter implements BeatModelInterface {
    HeartModelInterface heart;
    public HeartAdapter(HeartModelInterface heart) {             Here, we store a reference        this.heart = heart;                                                                         to the heart model.    }
    public void initialize() {}
                                           We don’t know what these would
    public void on() {}                     do to a heart, but it sounds scary.
                                               So we’ll just leave them as “no ops.”    public void off() {}
    public int getBPM() {                                When getBPM() is called, we’ll just
        return heart.getHeartRate();                          translate it to a getHeartRate()
    }                                                                                 call on the heart model.
    public void setBPM(int bpm) {}                                                          We don’t want to do this on a heart!
                                                                                Again, let’s leave it as a “no op.”    public void registerObserver(BeatObserver o) {
        heart.registerObserver(o);
    }
    public void removeObserver(BeatObserver o) {                                                                       Here are our observer methods.        heart.removeObserver(o);                                                            We just delegate them to the    }                                                                      wrapped heart model.
    public void registerObserver(BPMObserver o) {
        heart.registerObserver(o);
    }
    public void removeObserver(BPMObserver o) {
        heart.removeObserver(o);
    }
}


540      Chapter 12


---

## PDF page 579

compound patterns

Now we’re ready for a HeartController

With our HeartAdapter in hand, we should be ready to create a controller and get
the view running with the HeartModel. Talk about reuse!                      The HeartController implements
                                                                            the ControllerInterface, just
                                                                                                         like the BeatController did.
 public class HeartController implements ControllerInterface {
     HeartModelInterface model;
     DJView view;
                                                                                     Like before, the
     public HeartController(HeartModelInterface model) {                   controller creates the
         this.model = model;                                                        view and gets everything
         view = new DJView(this, new HeartAdapter(model));                glued together.
         view.createView();
         view.createControls();                                 There is one change: we are passed
         view.disableStopMenuItem();                           a HeartModel, not a BeatModel...
         view.disableStartMenuItem();
     }                                                                               ...and we need to wrap that
                                                                    model with an adapter before
     public void start() {}                                we hand it to the view.
                                                                            Finally, the HeartController disables the     public void stop() {}                                                        menu items because they aren’t needed.
     public void increaseBPM() {}
     public void decreaseBPM() {}                      There’s not a lot to do here; after all,
                                                      we can’t really control hearts like we     public void setBPM(int bpm) {}                                                              can beat machines. }


And that’s it! Now it’s time for some test code...

 public class HeartTestDrive {

     public static void main (String[] args) {
         HeartModel heartModel = new HeartModel();
         ControllerInterface model = new HeartController(heartModel);
     }
 }
                                                               All we need to do is create the
                                                          controller and pass it a heart monitor.

                                                                       you are here 4      541


---

## PDF page 580

test the heart model

And now for a test run...


                                 File Edit  Window Help CheckMyPulse
              % java HeartTestDrive
                                                                                 Run this...              %


                                                           ...and you’ll see this.


  Things to try

    1  Notice that the display works great with a heart!
      The beat bar looks just like a pulse. Because the
       HeartModel also supports BPM and Beat Observers,
     we can get beat updates just like with the DJ beats.
    2  As the heartbeat has natural variation, notice the
        display is updated with the new beats per minute.
                                                                                              Nice healthy
    3  Each time we get a BPM update, the adapter is doing                    heart rate.         its job of translating getBPM() calls to getHeartRate()
         calls.
    4  The Start and Stop menu items are not enabled
       because the controller disabled them.
    5  The other buttons still work but have no effect
       because the controller implements no ops for them.
      The view could be changed to support the disabling
        of these items.


542      Chapter 12


---

## PDF page 581

compound patterns


           It seems like you are really hand-         When MVC was named they needed a        Does the view always have to askQ:               A:               Q: waving the fact that the Composite          word that began with a “M” or otherwise they    the model for its state? Couldn’t we use
 Pattern is really in MVC. Is it really there?     couldn’t have called it MVC.                   the push model and send the model’s
                                                                                              state with the update notification?
      Yes, Virginia, there really is a             But seriously, we agree with you. EveryoneA: Composite Pattern in MVC. But, actually,        scratches their head and wonders what a             Yes, the model could certainly send                                   A: this is a very good question. Today GUI        model is. But then everyone comes to the                                                                                                                                   its state with the notification, and we could
 packages, like Swing, have become so           realization that they can’t think of a better      do something similar with the BeatModel
 sophisticated that we hardly notice the         word either.                                by sending just the state that the view
 internal structure and the use of Composite                                                                    is interested in. If you remember the
 in the building and update of the display.             You’ve talked a lot about the state     Observer Pattern chapter, however, you’ll                 Q:
 It’s even harder to see when we have web      of the model. Does this mean it has the       also remember that there are a couple of
 browsers that can take markup language       State Pattern in it?                          disadvantages to this. If you don’t, go back
 and convert it into a user interface.                                                                    to Chapter 2 and have a second look. The
                                                No, we mean the general idea of state.   MVC model has been adapted to a number Back when MVC was first discovered,    A:But certainly some models do use the State      of similar models—in particular, for the web’s
 creating GUIs required a lot more manual       Pattern to manage their internal states.         browser/server environment—so you’ll find a
 intervention and the pattern was more                                                                            lot of exceptions to the rule out there.
 obviously part of the MVC.                                                            I’ve seen descriptions of MVC                 Q:                                                                                                                                                          If I have more than one view, do I                                       where the controller is described as    Q:
     Does the controller ever implement    a “mediator” between the view and the      always need more than one controller?Q:
 any application logic?                     model. Is the controller implementing the
                                           Mediator Pattern?                                       Typically, you need one controller                                   A:      No, the controller implements behavior                                                  per view at runtime; however, the sameA:
 for the view. It is the smarts that translates        We haven’t covered the Mediator           controller class can easily manage many the actions from the view to actions on the  A:Pattern (although you’ll find a summary of       views.
 model. The model takes those actions and      the pattern in the appendix), so we won’t go
 implements the application logic to decide        into too much detail here, but the intent of           The view is not supposed to                                  Q: what to do in response to those actions. The    the mediator is to encapsulate how objects     manipulate the model; however, I noticed
 controller might have to do a little work to         interact and promote loose coupling by          in your implementation that the view has
 determine what method calls to make on        keeping two objects from referring to each        full access to the methods that change
 the model, but that’s not considered the         other explicitly. So, to some degree, the        the model’s state. Is this dangerous?
“application logic.” The application logic is the     controller can be seen as a mediator, since
 code that manages and manipulates your       the view never sets state directly on the            You are correct; we gave the view full data and it lives in your model.                model, but rather always goes through the  A:access to the model’s set of methods. We
                                                        controller. Remember, however, that the         did this to keep things simple, but there may
        I’ve always found the word “model”    view does have a reference to the model to     be circumstances where you want to give theQ:
 hard to wrap my head around. I now         access its state. If the controller were truly a    view access to only part of your model’s API.
 get that it’s the guts of the application,       mediator, the view would have to go through    There’s a great design pattern that allows
 but why was such a vague, hard-to-          the controller to get the state of the model      you to adapt an interface to provide only a
 understand word used to describe this      as well.                                        subset. Can you think of it?
 aspect of MVC?


                                                                       you are here 4      543


---

## PDF page 582

your design toolbox


                           Most of my user
                                 interfaces are
                                   actually browser-based.
                              Is any of this going to
                                 help me?


                        Yes!
                  MVC is so useful that it has been adapted to many web
                               frameworks. Of course, the web works differently than your
                               standard application, so there are several different approaches
                                  to applying the MVC Pattern to the web.
                      Web applications have a client side (the browser) and a server
                                       side. Given that, we can make different design tradeoffs based
                          on where the model, the view, and the controller reside. In
                                         thin client approaches, the model, most of the view, and the
                                   controller all reside in the server, with the browser providing
                             a way to display the view, and to get input from the browser
                                  to the controller. Another approach is the single page application,
                            where almost all of the model, view, and controller reside on
                                the client side. Those are the two ends of the spectrum, and
                                     you’ll find frameworks that vary the extent to which each
                           component—that is the model, the view, and the controller—
                                   reside on the client or the server, along with hybrid models
                            where some components are shared across the client and server.
                           There are many popular web MVC frameworks, like Spring
                      Web MVC, Django, ASP.NET MVC, AngularJS, EmberJS,
                             JavaScriptMVC, Backbone, and no doubt more on the way.
                               For the most part each framework has its own unique way it
                          maps the model, the view, and the controller across the client
                           and the server. Now that you know the MVC Pattern, you
                                       will have no problem adapting your knowledge to whatever
                            framework you choose to use.


544      Chapter 12


---

## PDF page 583

compound patterns


       Tools for your Design Toolbox
       You could impress anyone with your design toolbox. Wow, look
          at all those principles, patterns, and now, compound patterns!
                                                              The Model View Controller
                                                                         (MVC) Pattern is a compound
                                                                                               pattern consisting of the
                                                                                        Observer, Strategy, and
                                                                                Composite Patterns.     Principles OO                                                              The                                                                                  model                                                                                 makes                                                                                              use                                                                                                                              of                                                                                                                    the                      varies.                    Basics          OO   Encapsulate what                                                                                   Observer                                                                                                      Pattern                                                                                               so                                                                                                                            that                                                                                                                                                                                                                      it                   over inheritance.        Abstraction   Favor composition                                                                can keep observers updated
                                                                                               yet stay decoupled from them.          to interfaces, not               Encapsulation    Program
     implementations.                       Polymorphism                         The controller is the Strategy                               designs                      coupled          for loosely                                                                                       for the view. The view can use     Strive        that interact.            Inheritance              objects                                                                                     different implementations of     between                               extension               be open for              should                                                                           the controller to get different       Classes               for modification.                                                                 behavior.      but closed                   Do not            on abstractions.                                            The view uses the Composite       Depend              classes.            on concrete                                                                     Pattern to implement        depend
                            friends.                                                               the user interface, which        Only talk to your
         Don’t call us, we’ll call you.                                                                usuallycomponentsconsistslike ofpanels,nested                                   reason                                                                                         frames, and buttons.                      have only one                  should      A class
         to change.                                                  These patterns work together
                                                                                                      to decouple the three players
                                                                                                             in the MVC model, which
                                                                                keeps designs clear and   PatternsOO                                                                                                                 flexible.                                                       new                                                  a                    family                           an                                                        have                                   one             a                                          We                           additional                                 has                      one-to-many                                          its                                  requestan                           ProvideDefine                -               a                    a            defines                                 onlyrequest                Attach         -          -                                   alter                    a                                class                 a                defines                                requestto                   a         -                              butor                           that                                      MVC            Factory         Method                     Encapsulates                   Ensure                          sodynamically.                -object           -                           surrogate                                                        category!                a                    Encapsulates Strategy                               object,                  anobject               encapsulates                        ofpoint                   Encapsulates                                                                                 an                       objects          -                an   ObserverDecorator                             families                              youyou                                                                          The                                                                                         Adapter                                                                                                         Pattern                                                                                                can                                                                                                be    Factory          -                 Allowto-   Abstract                              tochanges.of          -                               global                 a                               state      Singleton                               youits                   creating                             lettingletting                   creating-Provide     AdapterCommand                              letting                them                                      all                            to    algorithms,             betweenfor     Facade      State            for                   provide      Proxy                                                        compound                           internal of                                              a                               objectwithout                   therebythereby                                  class                            state,      responsibilities                                                                         is                           flexible                       its                   thereby            and                      another            makes              a    dependency      interface                                         its      interface                       which                 for                         objects              when              object,object,                                                                              used                                                                                                            to                                                                                            adapt                                                                                        a new                                                                                               model                   changes                                differentdifferent         andobject,        instance                provide                               changedifferent        ananan                  decide       asas      one,                         withwith                                extending       as                       to             object         behavior                         with               depedent                            updated                                   lets                        for        one                  Strategy          or  each                              it.                      and     Decorators                      appear                   it.          placeholdersubclasses                        clientsclientsclients                                    classes.                                                        pattern.    when                  to           to                       will                     Method      relatedlet                              andandand                     subclassing                   notified                                                                                                      to                                                                              an                                                                                                          existing                                                                                                 view                                                                                            and                  access        access            to                    concrete             object                                requests,requests,        parameterizeparameterize              are                 Factory                                requests,         parameterizeThe                         loglog               their          control                          log                            the                 vary                  oror  interchangeable.                  or                         to      alternative     dependents                queuequeue       specifyinginstantiate.                 queue         algorithm                                                                                                            controller.                     instantiation          requests,requests,     the          requests,            class.                            operations.operations.            defer                            operations.   lets       functionality.          class      automatically     a                 undoableundoable                 undoable         supportsupport                                Patterns          support                                                              MVC has been adapted to         subclasses.         Compound          two or                                                       combines                                            Pattern                  A Compound                                                  into a solution that                                  the web.                               more patterns  or general problem.                     There are many web MVC                                               recurring                                           solves a                                                                                  frameworks with various
                                                                                          adaptations of the MVC
                                                                                               pattern to fit the client/server
                                                                                                  application structure.


                                                                     you are here 4      545


---

## PDF page 584

exercise solutions

         Exercise Solutions


                                       The QuackCounter is a Quackable too. When we change
                                         Quackable to extend QuackObservable, we have to change every
                                                   class that implements Quackable, including QuackCounter:
                                                                                                      is a Quackable, so                                                           QuackCounter                                                       now it’s a QuackObservable too.
       public class QuackCounter implements Quackable {
           Quackable duck;
           static int numberOfQuacks;                           Here’s the duck that QuackCounter
                                                                                                       is decorating. It’s this duck that
                                                                                     really needs to handle the observable           public QuackCounter(Quackable duck) {                                                                     methods.               this.duck = duck;
           }

           public void quack() {                                                                         All of this code is the               duck.quack();                                                                                       previous                                                            same as the                                                                          QuackCounter.               numberOfQuacks++;                               version of
           }

           public static int getQuacks() {
               return numberOfQuacks;
           }

           public void registerObserver(Observer observer) {
               duck.registerObserver(observer);                         Here are the two
           }                                                                     QuackObservable
                                                                                   methods. Notice that
                                                                      we just delegate both           public void notifyObservers() {                                                                                                           calls to the duck
               duck.notifyObservers();                                  that we’re decorating.           }
       }


546      Chapter 12


---

## PDF page 585

compound patterns


                          What if our Quackologist wants to observe an entire flock? What does that
                        mean anyway? Think about it like this: if we observe a composite, then we’re
                               observing everything in the composite. So, when you register with a flock, the
                                    flock composite makes sure you get registered with all its children, which may
                                include other flocks.
                                                        Flock is a Quackable, so now                                                                           it’s a QuackObservable too.
public class Flock implements Quackable {
    List<Quackable> quackers = new ArrayList<Quackable>();
                                                                            Here are the Quackables
    public void add(Quackable duck) {                              that are in the Flock.
        ducks.add(duck);
    }

    public void quack() {
        Iterator<Quackable> iterator = quackers.iterator();
        while (iterator.hasNext()) {
            Quackable duck = iterator.next();
            duck.quack();                                                           When you register as an Observer        }                                                          with the Flock, you actually                                                                                  with everything    }                                                            get registered                                                                                                                             is                                                                                         which                                                                             that’s IN the flock,                                                                             a                                                                                                                             it’s                                                                                  whether                                                                         every Quackable,    public void registerObserver(Observer observer) {                                                                   duck or another Flock.        Iterator<Quackable> iterator = ducks.iterator();
        while (iterator.hasNext()) {                         We iterate through all the
            Quackable duck = iterator.next();                   Quackables in the Flock
                                                                     and delegate the call to            duck.registerObserver(observer);
                                                                          each Quackable. If the        }                                                                          Quackable is another Flock,
    }                                                                                  it will do the same.
    public void notifyObservers() { }
                                 Each Quackable does its own notification, so}                                     Flock doesn’t have to worry about it. This
                                      happens when Flock delegates quack() to each
                                    Quackable in the Flock.


                                                                  you are here 4      547


---

## PDF page 586

exercise solutions


                                     We’re still directly instantiating Geese by relying on concrete classes.
                                Can you write an Abstract Factory for Geese? How should it handle
                                       creating “goose ducks”?

                You could add a createGooseDuck() method to the existing Duck Factories. Or,
                 you could create a completely separate Factory for creating families of Geese.


       Design Puzzle Solution
                                      You’ve seen that the view and controller together make use of the Strategy
                                           Pattern. Can you draw a class diagram of the two that represents this pattern?


                                                                      The    The view delegates                                         DJView                                                    <<interface>>        ControllerInterface     behavior to the                                                                                  ControllerInterface        is the interface
     controller. The                controller                                                          setBPM()              that all concrete
     behavior it                      createView()                                                        increaseBPM()              controllers
                                                                                                         decreaseBPM()     delegates is how to        updateBPM()                                                                                               implement. This     control the model                                              updateBeat()                                                                        is the strategy
                                                 createControls()    based on user                                           enableStopMenuItem()                                                         interface.     input.
                                             disableStopMenuItem()                                                                                                                  Controller
                                             enableStartMenuItem()
                                              disableStartMenuItem()                                              setBPM()
                                               actionPerformed()                                                    increaseBPM()          We can plug
                                                                                                         decreaseBPM()                                                                                                              in different
                                                                                                     controllers
                                                                                    to provide
                                                                                             different
                                                                                                  behaviors for
                                                                                   the view.


548      Chapter 12


---

## PDF page 587

compound patterns

       Ready Bake                     MIDIHere’scodethe completeto generateimplementationthe sound, andofallthetheDJView.Swing componentsIt shows all theto
                                                   create the view. You can also download this code at       Code                                               https://www.wickedlysmart.com. Have fun!

package headfirst.designpatterns.combined.djview;

public class DJTestDrive {

    public static void main (String[] args) {
        BeatModelInterface model = new BeatModel();
        ControllerInterface controller = new BeatController(model);
    }
}

The Beat Model
package headfirst.designpatterns.combined.djview;

public interface BeatModelInterface {
    void initialize();

    void on();

    void off();

    void setBPM(int bpm);

    int getBPM();

    void registerObserver(BeatObserver o);

    void removeObserver(BeatObserver o);

    void registerObserver(BPMObserver o);

    void removeObserver(BPMObserver o);
}

                                                                       you are here 4      549


---

## PDF page 588

ready-bake code: model


package headfirst.designpatterns.combined.djview;
import java.util.*;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import java.io.*;
import javax.sound.sampled.Line;
public class BeatModel implements BeatModelInterface, Runnable {
       List<BeatObserver> beatObservers = new ArrayList<BeatObserver>();
       List<BPMObserver> bpmObservers = new ArrayList<BPMObserver>();
       int bpm = 90;
       Thread thread;
       boolean stop = false;
       Clip clip;
       public void initialize() {
             try {
                    File resource = new File("clap.wav");
                    clip = (Clip) AudioSystem.getLine(new Line.Info(Clip.class));
                    clip.open(AudioSystem.getAudioInputStream(resource));
             }
              catch(Exception ex) {
                    System.out.println("Error: Can’t load clip");
                    System.out.println(ex);
             }
       }
       public void on() {
             bpm = 90;
              notifyBPMObservers();
              thread = new Thread(this);
              stop = false;
              thread.start();
       }
       public void off() {
              stopBeat();
              stop = true;
       }


550      Chapter 12


---

## PDF page 589

compound patterns

  Ready Bake
  Code

public void run() {
       while (!stop) {
              playBeat();
              notifyBeatObservers();
             try {
                    Thread.sleep(60000/getBPM());
             } catch (Exception e) {}
       }
}
public void setBPM(int bpm) {
       this.bpm = bpm;
       notifyBPMObservers();
}
public int getBPM() {
       return bpm;
}
public void registerObserver(BeatObserver o) {
       beatObservers.add(o);
}
public void notifyBeatObservers() {
       for (int i = 0; i < beatObservers.size(); i++) {
              BeatObserver observer = (BeatObserver)beatObservers.get(i);
              observer.updateBeat();
       }
}
public void registerObserver(BPMObserver o) {
       bpmObservers.add(o);
}
public void notifyBPMObservers() {
       for (int i = 0; i < bpmObservers.size(); i++) {
              BPMObserver observer = (BPMObserver)bpmObservers.get(i);
              observer.updateBPM();
       }
}


                                                                you are here 4      551


---

## PDF page 590

ready-bake code: model


       public void removeObserver(BeatObserver o) {
              int i = beatObservers.indexOf(o);
              if (i >= 0) {
                    beatObservers.remove(i);
             }
       }
       public void removeObserver(BPMObserver o) {
              int i = bpmObservers.indexOf(o);
              if (i >= 0) {
                    bpmObservers.remove(i);
             }
       }
       public void playBeat() {
              clip.setFramePosition(0);
              clip.start();
       }
       public void stopBeat() {
              clip.setFramePosition(0);
              clip.stop();
       }
}


552      Chapter 12


---

## PDF page 591

compound patterns

The View
                                                                 Ready Bake
package headfirst.designpatterns.combined.djview;                        Code

public interface BeatObserver {
    void updateBeat();
}
package headfirst.designpatterns.combined.djview;

public interface BPMObserver {
    void updateBPM();
}
package headfirst.designpatterns.combined.djview;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class DJView implements ActionListener,  BeatObserver, BPMObserver {
    BeatModelInterface model;
    ControllerInterface controller;
    JFrame viewFrame;
    JPanel viewPanel;
    BeatBar beatBar;
    JLabel bpmOutputLabel;
    JFrame controlFrame;
    JPanel controlPanel;
    JLabel bpmLabel;
    JTextField bpmTextField;
    JButton setBPMButton;
    JButton increaseBPMButton;
    JButton decreaseBPMButton;
    JMenuBar menuBar;
    JMenu menu;
    JMenuItem startMenuItem;
    JMenuItem stopMenuItem;

    public DJView(ControllerInterface controller, BeatModelInterface model) {
        this.controller = controller;
        this.model = model;
        model.registerObserver((BeatObserver)this);
        model.registerObserver((BPMObserver)this);
    }


                                                                       you are here 4      553


---

## PDF page 592

ready-bake code: view

    public void createView() {
        // Create all Swing components here
        viewPanel = new JPanel(new GridLayout(1, 2));
        viewFrame = new JFrame("View");
        viewFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        viewFrame.setSize(new Dimension(100, 80));
        bpmOutputLabel = new JLabel("offline", SwingConstants.CENTER);
        beatBar = new BeatBar();
        beatBar.setValue(0);
        JPanel bpmPanel = new JPanel(new GridLayout(2, 1));
        bpmPanel.add(beatBar);
        bpmPanel.add(bpmOutputLabel);
        viewPanel.add(bpmPanel);
        viewFrame.getContentPane().add(viewPanel, BorderLayout.CENTER);
        viewFrame.pack();
        viewFrame.setVisible(true);
    }
    public void createControls() {
        // Create all Swing components here
        JFrame.setDefaultLookAndFeelDecorated(true);
        controlFrame = new JFrame("Control");
        controlFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        controlFrame.setSize(new Dimension(100, 80));
        controlPanel = new JPanel(new GridLayout(1, 2));
        menuBar = new JMenuBar();
        menu = new JMenu("DJ Control");
        startMenuItem = new JMenuItem("Start");
        menu.add(startMenuItem);
        startMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                controller.start();
            }
        });
        stopMenuItem = new JMenuItem("Stop");
        menu.add(stopMenuItem);
        stopMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                controller.stop();
            }
        });
        JMenuItem exit = new JMenuItem("Quit");
        exit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent event) {
                System.exit(0);
            }
        });


554      Chapter 12


---

## PDF page 593

compound patterns

    Ready Bake
    Code
    menu.add(exit);
    menuBar.add(menu);
    controlFrame.setJMenuBar(menuBar);
    bpmTextField = new JTextField(2);
    bpmLabel = new JLabel("Enter BPM:", SwingConstants.RIGHT);
    setBPMButton = new JButton("Set");
    setBPMButton.setSize(new Dimension(10,40));
    increaseBPMButton = new JButton(">>");
    decreaseBPMButton = new JButton("<<");
    setBPMButton.addActionListener(this);
    increaseBPMButton.addActionListener(this);
    decreaseBPMButton.addActionListener(this);
    JPanel buttonPanel = new JPanel(new GridLayout(1, 2));
    buttonPanel.add(decreaseBPMButton);
    buttonPanel.add(increaseBPMButton);
    JPanel enterPanel = new JPanel(new GridLayout(1, 2));
    enterPanel.add(bpmLabel);
    enterPanel.add(bpmTextField);
    JPanel insideControlPanel = new JPanel(new GridLayout(3, 1));
    insideControlPanel.add(enterPanel);
    insideControlPanel.add(setBPMButton);
    insideControlPanel.add(buttonPanel);
    controlPanel.add(insideControlPanel);
    bpmLabel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
    bpmOutputLabel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
    controlFrame.getRootPane().setDefaultButton(setBPMButton);
    controlFrame.getContentPane().add(controlPanel, BorderLayout.CENTER);
    controlFrame.pack();
    controlFrame.setVisible(true);
}
public void enableStopMenuItem() {
    stopMenuItem.setEnabled(true);
}
public void disableStopMenuItem() {
    stopMenuItem.setEnabled(false);
}


                                                                   you are here 4      555


---

## PDF page 594

ready-bake code: controller

    public void enableStartMenuItem() {
        startMenuItem.setEnabled(true);
    }
    public void disableStartMenuItem() {
        startMenuItem.setEnabled(false);
    }
    public void actionPerformed(ActionEvent event) {
        if (event.getSource() == setBPMButton) {
            int bpm = 90;
            String bpmText = bpmTextField.getText();
            if (bpmText == null || bpmText.contentEquals("")) {
                bpm = 90;
            } else {
                bpm = Integer.parseInt(bpmTextField.getText());
            }
            controller.setBPM(bpm);
        } else if (event.getSource() == increaseBPMButton) {
            controller.increaseBPM();
        } else if (event.getSource() == decreaseBPMButton) {
            controller.decreaseBPM();
        }
    }
    public void updateBPM() {
        int bpm = model.getBPM();
        if (bpm == 0) {
            bpmOutputLabel.setText("offline");
        } else {
            bpmOutputLabel.setText("Current BPM: " + model.getBPM());
        }
    }
    public void updateBeat() {
        beatBar.setValue(100);
    }
}
The Controller
package headfirst.designpatterns.combined.djview;
public interface ControllerInterface {
    void start();
    void stop();
    void increaseBPM();
    void decreaseBPM();
    void setBPM(int bpm);
}

556      Chapter 12


---

## PDF page 595

compound patterns

                                                                 Ready Bake
package headfirst.designpatterns.combined.djview;                        Code
public class BeatController implements ControllerInterface {
    BeatModelInterface model;
    DJView view;
    public BeatController(BeatModelInterface model) {
        this.model = model;
        view = new DJView(this, model);
        view.createView();
        view.createControls();
        view.disableStopMenuItem();
        view.enableStartMenuItem();
        model.initialize();
    }
    public void start() {
        model.on();
        view.disableStartMenuItem();
        view.enableStopMenuItem();
    }
    public void stop() {
        model.off();
        view.disableStopMenuItem();
        view.enableStartMenuItem();
    }
    public void increaseBPM() {
        int bpm = model.getBPM();
        model.setBPM(bpm + 1);
    }
    public void decreaseBPM() {
        int bpm = model.getBPM();
        model.setBPM(bpm - 1);
    }
    public void setBPM(int bpm) {
        model.setBPM(bpm);
    }
}


                                                                       you are here 4      557


---

## PDF page 596

ready-bake code: heart model

The Heart Model

package headfirst.designpatterns.combined.djview;
public class HeartTestDrive {
    public static void main (String[] args) {
        HeartModel heartModel = new HeartModel();
        ControllerInterface model = new HeartController(heartModel);
    }
}
package headfirst.designpatterns.combined.djview;
public interface HeartModelInterface {
    int getHeartRate();
    void registerObserver(BeatObserver o);
    void removeObserver(BeatObserver o);
    void registerObserver(BPMObserver o);
    void removeObserver(BPMObserver o);
}
package headfirst.designpatterns.combined.djview;
import java.util.*;
public class HeartModel implements HeartModelInterface, Runnable {
    List<BeatObserver> beatObservers = new ArrayList<BeatObserver>();
    List<BPMObserver> bpmObservers = new ArrayList<BPMObserver>();
    int time = 1000;
    int bpm = 90;
    Random random = new Random(System.currentTimeMillis());
    Thread thread;
    public HeartModel() {
        thread = new Thread(this);
        thread.start();
    }
    public void run() {
        int lastrate = -1;
        for(;;) {
            int change = random.nextInt(10);
            if (random.nextInt(2) == 0) {
                change = 0 - change;
            }
            int rate = 60000/(time + change);

558      Chapter 12


---

## PDF page 597

compound patterns
            if (rate < 120 && rate > 50) {
                time += change;
                notifyBeatObservers();                                 Ready Bake
                if (rate != lastrate) {                                                                 Code                    lastrate = rate;
                    notifyBPMObservers();
                }
            }
            try {
                Thread.sleep(time);
            } catch (Exception e) {}
        }
    }
    public int getHeartRate() {
        return 60000/time;
    }
    public void registerObserver(BeatObserver o) {
        beatObservers.add(o);
    }
    public void removeObserver(BeatObserver o) {
        int i = beatObservers.indexOf(o);
        if (i >= 0) {
            beatObservers.remove(i);
        }
    }
    public void notifyBeatObservers() {
        for(int i = 0; i < beatObservers.size(); i++) {
            BeatObserver observer = (BeatObserver)beatObservers.get(i);
            observer.updateBeat();
        }
    }
    public void registerObserver(BPMObserver o) {
        bpmObservers.add(o);
    }
    public void removeObserver(BPMObserver o) {
        int i = bpmObservers.indexOf(o);
        if (i >= 0) {
            bpmObservers.remove(i);
        }
    }
    public void notifyBPMObservers() {
        for(int i = 0; i < bpmObservers.size(); i++) {
            BPMObserver observer = (BPMObserver)bpmObservers.get(i);
            observer.updateBPM();
        }
    }
}
                                                                       you are here 4      559


---

## PDF page 598

ready-bake code: heart adapter

The Heart Adapter

package headfirst.designpatterns.combined.djview;
public class HeartAdapter implements BeatModelInterface {
    HeartModelInterface heart;
    public HeartAdapter(HeartModelInterface heart) {
        this.heart = heart;
    }
    public void initialize() {}
    public void on() {}
    public void off() {}
    public int getBPM() {
        return heart.getHeartRate();
    }
    public void setBPM(int bpm) {}
    public void registerObserver(BeatObserver o) {
        heart.registerObserver(o);
    }
    public void removeObserver(BeatObserver o) {
        heart.removeObserver(o);
    }
    public void registerObserver(BPMObserver o) {
        heart.registerObserver(o);
    }
    public void removeObserver(BPMObserver o) {
        heart.removeObserver(o);
    }
}


560      Chapter 12


---

## PDF page 599

compound patterns

The Controller
                                                                 Ready Bake
package headfirst.designpatterns.combined.djview;                        Code

public class HeartController implements ControllerInterface {
    HeartModelInterface model;
    DJView view;

    public HeartController(HeartModelInterface model) {
        this.model = model;
        view = new DJView(this, new HeartAdapter(model));
        view.createView();
        view.createControls();
        view.disableStopMenuItem();
        view.disableStartMenuItem();
    }

    public void start() {}

    public void stop() {}

    public void increaseBPM() {}

    public void decreaseBPM() {}

    public void setBPM(int bpm) {}
}


                                                                       you are here 4      561
