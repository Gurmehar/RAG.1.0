# 8: the Template Method Pattern: Encapsulating Algorithms

_Extracted from PDF pages 315-354. Text only; images and diagrams are not embedded._


---

## PDF page 315

8 the Template Method Pattern
   Encapsulating
           Algorithms


                Yeah, he’s a great
          boss until it comes to getting
         down in this hole, then it ALL
         becomes MY job. See what I
         mean? He’s nowhere in sight!


       We’re on an encapsulation roll; we’ve encapsulated object
        creation, method invocation, complex interfaces, ducks,
        pizzas...what could be next? We’re going to get down to encapsulating
           pieces of algorithms so that subclasses can hook themselves right into a
           computation anytime they want. We’re even going to learn about a design principle
            inspired by Hollywood. Let’s get started...


                                                                          this is a new chapter      277


---

## PDF page 316

coffee and tea recipes are similar

It’s time for some more caffeine

Some people can’t live without their coffee; some
people can’t live without their tea. The common
ingredient? Caffeine, of course!
But there’s more; tea and coffee are made in very
similar ways. Let’s check it out:


                                   Manual                                 Training                           Barista                   Coffee           Starbuzz                         precisely                                      recipes                               these                         follow                   Please       beverages.          Baristas!     Starbuzz               preparing          when
                         Recipe                    Coffee            Starbuzz                                                    The recipe for                                                                                a lot                                                                                                             looks                        water                   some                                    water                                   coffee              Boil                                                                                                 for          (1)                                                                                                             recipe                       in boiling                                                                                                                like the                    coffee               Brew           (2)                       in cup                                                  tea, doesn’t it?                    coffee               Pour           (3)             milk                       and                   sugar               Add           (4)
                   Tea Recipe               Starbuzz
                          water                     some           water                 Boil             (1)                       in boiling                      tea                  Steep             (2)                       in cup                     tea                  Pour             (3)                      lemon                 Add              (4)
                                                                       be kept                                                                   and should                                                                 secrets                                                          trade                                                     Coffeeconfidential.                                             Starbuzz                                                  strictly                           All recipes are


278      Chapter 8


---

## PDF page 317

the template method pattern

Whipping up some coffee and tea classes
(in Java)

Let’s play “coding barista” and write some code for
creating coffee and tea.
Here’s the coffee:
                        Here’s our Coffee class for making coffee.
                                                               for coffee,                                                                        recipe                                                                                       manual.  public class Coffee {                              Here’s our                                                                                 training                                                    of the                                                        out                                                           straight
      void           prepareRecipe() {                                                                            implemented as          boilWater();                                                Each of the steps is                                                                method.          brewCoffeeGrinds();               a separate
          pourInCup();
          addSugarAndMilk();
      }

      public void boilWater() {
          System.out.println("Boiling water");
      }                                                                               Each of these methods
                                                                                             implements one step of
      public void brewCoffeeGrinds() {                                        the algorithm. There’s
          System.out.println("Dripping Coffee through filter");           a method to boil water,                                                                                  brew the coffee, pour      }                                                                                   the coffee in a cup,
                                                                                 and add sugar and milk.
      public void pourInCup() {
          System.out.println("Pouring into cup");
      }

      public void addSugarAndMilk() {
          System.out.println("Adding Sugar and Milk");
      }
  }


                                                                       you are here 4      279


---

## PDF page 318

tea implementation

And now the Tea...
    public class Tea {                                                       This looks very similar to the one
                                                 we just implemented in Coffee;        void prepareRecipe() {                                                    the second and fourth steps are            boilWater();                                                           different, but it’s basically the            steepTeaBag();                                                     same recipe.            pourInCup();
            addLemon();
        }
        public void boilWater() {
            System.out.println("Boiling water");                                                                                          Notice that these        }                                                                              two methods
                                                                These two            are exactly the        public void steepTeaBag() {                                                                 methods are          same as they
            System.out.println("Steeping the tea");         specialized to Tea.     are in Coffee!
        }                                                                    So we definitely
                                                                                            have some code
        public void addLemon() {                                                            duplication going
            System.out.println("Adding Lemon");                                on here.
        }
        public void pourInCup() {
            System.out.println("Pouring into cup");
        }
    }
                              When we’ve got code
                                     duplication, that’s a good sign we need to
                                  clean up the design. It seems like here we
                                should abstract the commonality into a base
                                    class since coffee and tea are so similar.


280      Chapter 8


---

## PDF page 319

the template method pattern

    Design Puzzle

You’ve seen that the Coffee and Tea classes have a fair bit of code duplication. Take another
look at the Coffee and Tea classes and draw a class diagram showing how you’d redesign the
classes to remove redundancy:


                                                            you are here 4      281


---

## PDF page 320

first cut at abstraction

Let’s abstract that Coffee and Tea

It looks like we’ve got a pretty straightforward design
exercise on our hands with the Coffee and Tea classes.
Your first cut might have looked something like this:

                                                                           and pourInCup()                                                        The boilWater()                                                                                                                       subclasses,                                                                  methods are shared by both                                                                                                                     superclass.                                                                    CaffeineBeverage                                                                       so they are defined in the
                                                                         prepareRecipe()   The prepareRecipe() method                                                                                boilWater()    differs in each subclass, so it                      pourInCup()     is defined as abstract.


 Each subclass                                 Coffee                                       Tea                  Each subclass
 implements its                       prepareRecipe()                                       prepareRecipe()                          overrides the
 own recipe.                            brewCoffeeGrinds()                                   steepTeaBag()                          prepareRecipe()
                                            addSugarAndMilk()                                 addLemon()                       method and
                                                                                                implements its own
                                                                                                                  recipe.

                               The methods specific to                                    Coffee and Tea stay in
                                   the subclasses.


      Did we do a good job on the redesign? Hmmmm, take another
       look. Are we overlooking some other commonality? What are
       other ways that Coffee and Tea are similar?


282      Chapter 8


---

## PDF page 321

the template method pattern

Taking the design further...

So what else do Coffee and Tea have in common? Let’s start with the recipes.


                             Recipe                        Coffee                Starbuzz
                           water                      some             water                  Boil              (1)          in boiling                        coffee                  Brew              (2)          in cup                        coffee               Starbuzz Tea Recipe                   Pour               (3)             milk                           and                       sugar                  Add               (4)                         (1) Boil some water
                                            (2) Steep tea in boiling water
                                            (3) Pour tea in cup
                                            (4) Add lemon


Notice that both recipes follow the same algorithm:

    1   Boil some water.
                                                                 These aren’t    2  Use the hot water to extract the coffee         abstracted but      These two are                                                                                                   abstracted                                                                                                already                                                                                  same;                                                                    the         or tea.                                                  are                                                                                                     base class.                                                                                                    into the                                                                                      apply                                                                                    just                                                                  they
                                                                 to different    3  Pour the resulting beverage into a cup.                                                                                beverages.
    4  Add the appropriate condiments to the
         beverage.


So, can we find a way to abstract prepareRecipe() too? Yes, let’s find out...


                                                                       you are here 4      283


---

## PDF page 322

abstract the algorithm

Abstracting prepareRecipe()

Let’s step through abstracting prepareRecipe() from each subclass (that is,
the Coffee and Tea classes)...

   1   The first problem we have is that Coffee uses brewCoffeeGrinds()
        and addSugarAndMilk() methods, while Tea uses steepTeaBag() and
        addLemon() methods.

               Coffee                             Tea
           void prepareRecipe() {                    void prepareRecipe() {
               boilWater();                              boilWater();
               brewCoffeeGrinds();                       steepTeaBag();
               pourInCup();                              pourInCup();
               addSugarAndMilk();                        addLemon();
           }                                        }

           Let’s think through this: steeping and brewing aren’t so different; they’re pretty analogous.
        So let’s make a new method name, say, brew(), and we’ll use the same name whether
          we’re brewing coffee or steeping tea.
          Likewise, adding sugar and milk is pretty much the same as adding a lemon: both
          are adding condiments to the beverage. Let’s also make up a new method name,
         addCondiments(), to handle this. So, our new prepareRecipe() method will look like this:

                        void prepareRecipe() {
                            boilWater();
                            brew();
                            pourInCup();
                            addCondiments();
                        }                                               the                                                          on                                                                       (Code                                                                                           page.)   2  Now we have a new prepareRecipe() method, but we need to fit it into the code.       next
        To do this we’ll start with the CaffeineBeverage superclass:


284      Chapter 8


---

## PDF page 323

the template method pattern
                                                    is abstract,                        CaffeineBeverage                          just like in the class design.                                                                             prepareRecipe() method                                                    Now, the same                                                                           will be used to make both Tea and Coffee. public abstract class CaffeineBeverage {                              is declared final because                                                               prepareRecipe()                                                                                     to                                                                                                 able                                                                               be                                                                            to                                                                                        subclasses                                                                     our                                                           want                                                              don’t                                                we                                                                                                              recipe!                                                                                 the                                                                                 change                                                                     and     final           void prepareRecipe() {                                                              method                                                                          this                                                               override                                                                                         the                                                                                           brew()                                                                                to                                             4                                                                         and                                                2                                                                                 steps         boilWater();                                                                     generalized                                                             We’ve                                                                        addCondiments().         brew();                                        beverage and         pourInCup();
         addCondiments();
     }
                                                            Because Coffee and Tea handle these
     abstract void brew();                          methods in different ways, they’re going to
                                                              have to be declared as abstract. Let the
     abstract void addCondiments();                    subclasses worry about that stuff!
     void boilWater() {
         System.out.println("Boiling water");
     }                                                           Remember, we moved these into
                                                                    the CaffeineBeverage class
     void pourInCup() {                                           (back in our class diagram).
         System.out.println("Pouring into cup");
     }
 }

3    Finally, we need to deal with the Coffee and Tea classes. They now rely on CaffeineBeverage
     to handle the recipe, so they just need to handle brewing and condiments:
                                                        As in our design, Tea and Coffee
  public class Tea extends CaffeineBeverage {        now extend CaffeineBeverage.
      public void brew() {
          System.out.println("Steeping the tea");
      }                                                           Tea needs to define brew() and                                                                    addCondiments()—the two abstract      public void addCondiments() {                                                                   methods from CaffeineBeverage.          System.out.println("Adding Lemon");
      }                                                       Same for Coffee, except Coffee
  }                                                                             deals with coffee, and sugar and milk
                                                                              instead of tea bags and lemon.  public class Coffee extends CaffeineBeverage {
      public void brew() {
          System.out.println("Dripping Coffee through filter");
      }
      public void addCondiments() {
          System.out.println("Adding Sugar and Milk");
      }
  }

                                                                  you are here 4      285


---

## PDF page 324

class diagram for caffeine beverages


                                     Draw the new class diagram now that we’ve moved the
                                          implementation of prepareRecipe() into the CaffeineBeverage class:


286      Chapter 8


---

## PDF page 325

the template method pattern

What have we done?
                                                  We’ve recognized
                                            that the two recipes
                                                are essentially the
                                                  same, although
                                             some of the steps
                                                    require different
                                                   implementations.                                                        So                                            Coffee     Tea                                 we’ve                                                        generalized                                                            the
                                                     recipe and placed it         1       1  Boil some water                        in the base class.                      Boilsomewater
                                                                 Brewthe       2  Steep the tea bag in the water                      2                                                                                          coffee                                                3                 grinds                                                                            Pour       3  Pour tea in a cup                                                       coffee                                                                                    inacup
                                               4 Add                                                                               sugarand                                                                                      milk        4 Add lemon

                          Caffeine Beverage
                generalize            1   Boil some water               generalize
                                2  Brew
                     relies on            3  Pour beverage in a cup             relies on
                 subclass                                                 subclass
                     for some            4  Add condiments                    for some
         subclass  steps                                                     steps            Coffee    Tea                                                                                                                 subclass


   2  Steep the tea bag in the water                                                                                           grinds                                                    Beverage                                                                                    coffee                                              Caffeine                                                            Brew the                                                           controls the        2   4  Add lemon                                           knows and                                                       and                                                                     recipe,                                                 steps of the                                            3         4 Add sugar and milk                                                     1 and                                                          steps                                              performs                                                         itself, but relies on Tea                                         or Coffee to do steps
                          2 and 4.


                                                                       you are here 4      287


---

## PDF page 326

meet the template method pattern

Meet the Template Method

We’ve basically just implemented the Template Method Pattern. What’s that? Let’s look at
the structure of the CaffeineBeverage class; it contains the actual “template method”:
                                                                                   prepareRecipe() is our
                                                                             template method. Why?
       public abstract class CaffeineBeverage {                                                                                 Because:
           final void prepareRecipe() {                                     (1) It is a method, after all.
                                                                            (2) It serves as a template for an
                 boilWater();                                          algorithm—in this case, an algorithm
                                                                           for making caffeinated beverages.
                 brew();                                                         In the template, each
                                                                                   step of the algorithm is
                                                                                  represented by a method.                 pourInCup();
                                                                   Some methods are
                                                                             handled by this class...                 addCondiments();
           }                                                                                               ...and some are handled
                                                                     by the subclass.
           abstract void brew();
                                                               The methods that need to
           abstract void addCondiments();                         be supplied by a subclass are
                                                                                declared abstract.
           void boilWater() {
                // implementation
           }

           void pourInCup() {
                // implementation
           }
        }

 The Template Method defines the steps of an algorithm and allows
  subclasses to provide the implementation for one or more steps.

288      Chapter 8


---

## PDF page 327

the template method pattern

Let’s make some tea...
Let’s step through making a tea and trace through how the                  Behind
template method works. You’ll see that the template method                                                       the Scenescontrols the algorithm; at certain points in the algorithm, it lets
the subclass supply the implementation of the steps...

                                                             boilWater();
   1    Okay, first we need a Tea object...                          brew();
                                                             pourInCup();            Tea myTea = new Tea();                                                             addCondiments();

   2   Then we call the template method:                                                                 The prepareRecipe() method
                                                                                      controls the algorithm. No
            myTea.prepareRecipe();                                one can change this, and
                                                                                              it counts on subclasses to
          which follows the algorithm for making caffeine                         provide some or all of the
             beverages...                                                              implementation.
   3     First we boil water:
                                                                                                                                                   CaffeineBeverage
            boilWater();                                                                                                           prepareRecipe()
                                                                                                                                                                                        boilWater()
          which happens in CaffeineBeverage.                                                                                    pourInCup()

   4    Next we need to brew the tea, which only the subclass knows
         how to do:
            brew();
                                                                                                                                                   Tea

                                                                                                                                                                            brew()   5   Now we pour the tea in the cup; this is the same for all beverages,                                                                                                                                                                    addCondiments();
            so it happens in CaffeineBeverage:
            pourInCup();
   6     Finally, we add the condiments, which are specific to each beverage,
            so the subclass implements this:
            addCondiments();


                                                                       you are here 4      289


---

## PDF page 328

what did template method get us?

What did the Template Method get us?


       Underpowered Tea & Coffee              New, hip CaffeineBeverage
             implementation                  powered by Template Method


           Coffee and Tea are running the show;            The CaffeineBeverage class runs
           they control the algorithm.                          the show; it has the algorithm, and
                                                                 protects it.


         Code is duplicated across Coffee and            The CaffeineBeverage class
           Tea.                                          maximizes reuse among the
                                                             subclasses.


         Code changes to the algorithm                 The algorithm lives in one place and
            require opening the subclasses and              code changes only need to be made
          making multiple changes.                             there.


           Classes are organized in a structure              The Template Method Pattern provides
             that requires a lot of work to add a                a framework that other caffeine
         new caffeine beverage.                          beverages can be plugged into. New
                                                                    caffeine beverages only need to
                                                         implement a couple of methods.

          Knowledge of the algorithm and how             The CaffeineBeverage class
             to implement it is distributed over                    concentrates knowledge about the
         many classes.                                       algorithm and relies on subclasses to
                                                               provide complete implementations.


290      Chapter 8


---

## PDF page 329

the template method pattern

Template Method Pattern defined

You’ve seen how the Template Method Pattern works in our Tea and Coffee example;
now, check out the official definition and nail down all the details:


                 The Template Method Pattern defines the skeleton
                           of an algorithm in a method, deferring some steps to
                           subclasses. Template Method lets subclasses redefine
                          certain steps of an algorithm without changing the
                          algorithm’s structure.


This pattern is all about creating a template for an algorithm. What’s a template?
As you’ve seen it’s just a method; more specifically, it’s a method that defines an
algorithm as a set of steps. One or more of these steps is defined to be abstract and
implemented by a subclass. This ensures the algorithm’s structure stays unchanged,
while subclasses provide some part of the implementation.
Let’s check out the class diagram:
                                            The template method makes use of the
                                                              primitive operations to implement an
                                                           algorithm. It is decoupled from the actual
                                                        implementation of these operations.

  The AbstractClass
    contains the template
    method...                                                AbstractClass                                   primitiveOperation1();
                                                                 templateMethod()                                                                                                                                        primitiveOperation2();    ...and abstract versions                            primitiveOperation1()
   of the operations                                    primitiveOperation2()
    used in the template
    method.


                                                              ConcreteClass
        bemany                                     primitiveOperation1()primitiveOperation2()                The ConcreteClass implements     may There         each                 of                                       the abstract operations,                  set                   full  ConcreteClasses,the  implementing    bythe                                           which are called when the             required                                                templateMethod() needs them.   operations           method.   template


                                                                       you are here 4      291


---

## PDF page 330

template method pattern up close

       Code Up Close

           Let’s take a closer look at how the AbstractClass is defined, including the template method
        and primitive operations.

            Here we have our abstract class; it                 is declared abstract and meant to            be subclassed by classes that provide                                                               the template method. It’s              implementations of the operations.                     Here’s                                                                 declared final to prevent subclasses                                                       from reworking the sequence of
                                                                     steps in the algorithm.
                  abstract class AbstractClass {

                      final void templateMethod() {             The template method
                          primitiveOperation1();                     defines the sequence of
                                                                                            steps, each represented                          primitiveOperation2();                                                                    by a method.                          concreteOperation();
                      }

                      abstract void primitiveOperation1();

                      abstract void primitiveOperation2();                                                                                        In this example, two of
                                                                         the primitive operations
                      void concreteOperation() {                    must be implemented by                          // implementation here                      concrete subclasses.
                      }
                  }
                         We also have a concrete operation
                              defined in the abstract class. This
                                 could be overridden by subclasses, or we
                                 could prevent overriding by declaring
                                concreteOperation() as final. More about
                                   this in a bit...


292      Chapter 8


---

## PDF page 331

the template method pattern


    Code Way Up Close


Now we’re going to look even closer at the types of method that can go in the abstract class:

  We’ve changed the
 templateMethod() to
  include a new method call.

 abstract class AbstractClass {

     final void templateMethod() {
         primitiveOperation1();
         primitiveOperation2();
         concreteOperation();
         hook();                              We still have our primitive
                                                            operation methods;     }                                                         these are abstract and
                                                       implemented by concrete
     abstract void primitiveOperation1();     subclasses.

     abstract void primitiveOperation2();
                                   A concrete operation is defined in the                                                                                                      final                                                                                   declared                                                                        one is                                                                                    class. This     final void concreteOperation() {           abstract                                                                                           It                                                                                                                 it.                                                                                    override                                                                             can’t                                                          so that subclasses         // implementation here                                               may be used in the template method     }                                                                    directly, or used by subclasses.
     void hook() {}

 }
                                  We can also have concrete methods that do nothing
    A concrete method, but            by default; we call these “hooks.” Subclasses are free
       it does nothing!                    to override these but don’t have to. We’re going to
                                             see how these are useful on the next page.


                                                               you are here 4      293


---

## PDF page 332

implement a hook

Hooked on                                        With a hook, I can                                                                 override the method or not.
Template Method...                                     It’s my choice. If I don’t, the
                                                              abstract class provides a default
                                                                implementation.A hook is a method that is declared in the
 abstract class, but only given an empty or default
 implementation. This gives subclasses the ability to
“hook into” the algorithm at various points, if they
 wish; a subclass is also free to ignore the hook.
 There are several uses of hooks; let’s take a look at
 one now. We’ll talk about a few other uses later:

    public abstract class CaffeineBeverageWithHook {

       final void prepareRecipe() {
            boilWater();
           brew();
                                                              We’ve added a little conditional            pourInCup();                                                         statement that bases its
           if (customerWantsCondiments()) {      success on a concrete method,
                addCondiments();                    customerWantsCondiments(). If the
           }                                           customer WANTS condiments, only then                                                  do we call addCondiments().       }

        abstract void brew();

        abstract void addCondiments();

       void boilWater() {
            System.out.println("Boiling water");
       }
       void pourInCup() {                                     Here we’ve defined a method                                                                           empty default                                                                                   (mostly)            System.out.println("Pouring into cup");         with a                                                                                   This method just                                                                             implementation.       }                                                                         returns true and does nothing else.
        boolean customerWantsCondiments() {
                                                                        This is a hook because the           return true;                                                                                    subclass can override this       }                                                                     method, but doesn’t have to.
   }

 294      Chapter 8


---

## PDF page 333

the template method pattern

Using the hook

To use the hook, we override it in our subclass. Here, the hook controls whether
the CaffeineBeverage class evaluates a certain part of the algorithm—that is,
whether it adds a condiment to the beverage.
How do we know whether the customer wants the condiment? Just ask!

    public class CoffeeWithHook extends CaffeineBeverageWithHook {
        public void brew() {
            System.out.println("Dripping Coffee through filter");
        }
        public void addCondiments() {                                                                                                   override                                                                                    Here’s where you            System.out.println("Adding Sugar and Milk");                                                                     the hook and provide your        }                                                                 own functionality.
        public boolean customerWantsCondiments() {
            String answer = getUserInput();
            if (answer.toLowerCase().startsWith("y")) {
                return true;                                       Get the user’s input on
            } else {                                                     the condiment decision
                return false;                                         and return true or false,
            }                                                                   depending on the input.
        }
        private String getUserInput() {
            String answer = null;
            System.out.print("Would you like milk and sugar with your coffee (y/n)? ");
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            try {
                answer = in.readLine();
            } catch (IOException ioe) {
                System.err.println("IO error trying to read your answer");
            }
            if (answer == null) {
                return "no";
            }                                                             This code asks if the user would like milk and            return answer;                                                                 sugar and gets the input from the command line.        }
    }

                                                                       you are here 4      295


---

## PDF page 334

test drive

Let’s run the Test Drive

Okay, the water’s boiling... Here’s the test code where we create a
hot tea and a hot coffee.

    public class BeverageTestDrive {
        public static void main(String[] args) {
                                                                              Create a tea.            TeaWithHook teaHook = new TeaWithHook();
            CoffeeWithHook coffeeHook = new CoffeeWithHook();       Create a coffee.

            System.out.println("\nMaking tea...");                                                                   And call prepareRecipe()            teaHook.prepareRecipe();                                                                             on both!
            System.out.println("\nMaking coffee...");
            coffeeHook.prepareRecipe();
        }
    }


And let’s give it a run...


           File Edit  Window Help send-more-honesttea
     %java BeverageTestDrive
     Making tea...
     Boiling water                        A steaming cup of tea, and yes,
     Steeping the tea                            of course we want that lemon!
     Pouring into cup
     Would you like lemon with your tea (y/n)? y
     Adding Lemon

     Making            coffee...                                                                                 coffee,                                                           of                                                                 cup                                                         hot                                             a nice     Boiling             water                           And                                                                                   waistline-                                                               the                                                            on                                                                   pass                                                 but we’ll     Dripping Coffee through filter                         condiments.                                                         expanding     Pouring into cup
     Would you like milk and sugar with your coffee (y/n)? n
     %

296      Chapter 8


---

## PDF page 335

the template method pattern


                      Now, I would have thought
                           that functionality like
                          asking the customer could
                          have been used by all
                                subclasses?


                                You know what? We agree with you. But you
                                     have to admit before you thought of that, it was
                                    a pretty cool example of how a hook can be used
                                           to conditionally control the flow of the algorithm
                                           in the abstract class. Right?
                                    We’re sure you can think of many other more
                                                  realistic scenarios where you could use the
                                       template method and hooks in your own code.


     When I’m creating a template method, how do I know when        Does a subclass have to implement all the abstractQ:                       Q:
 to use abstract methods and when to use hooks?               methods in the AbstractClass?

     Use abstract methods when your subclass MUST provide an            Yes, each concrete subclass defines the entire set of abstractA:                        A: implementation of the method or step in the algorithm. Use hooks       methods and provides a complete implementation of the undefined
when that part of the algorithm is optional. With hooks, a subclass       steps of the template method’s algorithm.
may choose to implement that hook, but it doesn’t have to.
                                                                                                                     It seems like I should keep my abstract methods small in                         Q:
     What are hooks really supposed to be used for?            number; otherwise, it will be a big job to implement them in theQ:
                                                                 subclass.
     There are a few uses of hooks. As we just said, a hook mayA: provide a way for a subclass to implement an optional part of an               That’s a good thing to keep in mind when you write template                          A:algorithm, or if it isn’t important to the subclass’s implementation, it      methods. Sometimes you can do this by not making the steps of
can skip it. Another use is to give the subclass a chance to react to      your algorithm too granular. But it’s obviously a tradeoff: the less
some step in the template method that is about to happen or just          granularity, the less flexibility.
happened. For instance, a hook method like justReorderedList()
allows the subclass to perform some activity (such as redisplaying an   Remember, too, that some steps will be optional, so you can
onscreen representation) after an internal list is reordered. As you’ve    implement these as hooks rather than abstract methods, easing the
seen, a hook can also provide a subclass with the ability to make a      burden on the subclasses of your abstract class.
decision for the abstract class.


                                                                       you are here 4      297


---

## PDF page 336

the hollywood principle

The Hollywood Principle                               You’ve heard me say it
                                                                    before, and I’ll say it again:
 We’ve got another design principle for you; it’s called the                 don’t call me, I’ll call you!
 Hollywood Principle:


                The Hollywood Principle
                       Don’t call us, we’ll call you.


 Easy to remember, right? But what has it got to do with OO
 design?
 The Hollywood Principle gives us a way to prevent
“dependency rot.” Dependency rot happens when you have
 high-level components depending on low-level components
 depending on high-level components depending on sideways
 components depending on low-level components, and so
 on. When rot sets in, no one can easily understand the way a
 system is designed.
 With the Hollywood Principle, we allow low-level components
 to hook themselves into a system, but the high-level
 components determine when they are needed, and how. In
 other words, the high-level components give the low-level
 components the “don’t call us, we’ll call you” treatment.


                                                                                                 high-level                                                                                               ...but the                                                                                           control                                                                            components
                                                      High-Level Component            when and how.
                     components            Low-level     in the           can participate
                                                           Another               computation...                  Low-Level
                                          Component                                                             Low-Level       A low-level                                                                                   component never                                                        Component              calls a high-level                                                                                        component                                                                                          directly.


 298      Chapter 8


---

## PDF page 337

the template method pattern

The Hollywood Principle and Template Method

The connection between the Hollywood Principle and the Template Method
Pattern is probably somewhat apparent: when we design with the Template
Method Pattern, we’re telling subclasses, “don’t call us, we’ll call you.” How?
Let’s take another look at our CaffeineBeverage design:

                       is our high-level CaffeineBeverage                          the                         over              has control           It                                                                                   Clients component.                             on                                   calls                                                                  of beverages will                     recipe, and            the                                                                                             depend                                                                 on                                                                     the algorithm for                             needed                         they’re                                                                                   CaffeineBeverage               only when      subclasses the                                                                                abstraction                                                                                   rather                    a method.                  of                                                                                    than                                                                       a     an implementation for                                                                           concrete                                                                          Tea                                                             CaffeineBeverage                                                                           or Coffee,                                                                                               which                                                                             reduces                                                                                       dependencies in the                                                             prepareRecipe()                         overall                                                                                      system.                                                                  boilWater()
                                                            pourInCup()
                                                              brew()
                                                         addCondiments()


                                              Coffee                                   Tea
                                       brew()                                        brew()
                                    addCondiments()                            addCondiments()
                                                                          Tea and Coffee never                                                                                                                     class                                                                                           abstract          The                                                                                         without being             provide                    subclasses are used simply to                                                  calldirectlythe                     implementation                                        details.                                                           first.                                                                                              “called”


                    What other patterns make use of the Hollywood Principle?


                                                others? any Observer; and Method Factory The

                                                                       you are here 4      299


---

## PDF page 338

who does what


                                                         The Hollywood Principle gives us a technique for creating designs    How does the Hollywood Principle relate to theQ:                                                                        that allow low-level structures to interoperate while preventing otherDependency Inversion Principle that we learned a few chapters                                                                     classes from becoming too dependent on them.back?

                                                                                      Is a low-level component disallowed from calling a     The Dependency Inversion Principle teaches us to avoid the   Q:A:                                                   method in a higher-level component?use of concrete classes and instead work as much as possible with
abstractions. The Hollywood Principle is a technique for building
frameworks or components so that lower-level components can be           Not really. In fact, a low-level component will often end up                          A:
hooked into the computation, but without creating dependencies          calling a method defined above it in the inheritance hierarchy purely
between the lower-level components and the higher-level layers. So,    through inheritance. But we want to avoid creating explicit circular
 they both have the goal of decoupling, but the Dependency Inversion    dependencies between the low-level component and the high-level
 Principle makes a much stronger and more general statement about     ones.
how to avoid dependencies in design.


              Match each pattern with its description:

           Pattern              Description

                                                   Encapsulate interchangeable
                 Template Method                                                    behaviors and use delegation to
                                                 decide which behavior to use.

                                                    Subclasses decide how
                    Strategy                                                             to implement steps in an
                                                      algorithm.

                                                    Subclasses decide which
                    Factory Method                                                    concrete classes to instantiate.


300      Chapter 8


---

## PDF page 339

the template method pattern

Template Methods in the Wild

The Template Method Pattern is a very common pattern and
you’re going to find lots of it in the wild. You’ve got to have
a keen eye, though, because there are many implementations
of the template methods that don’t quite look like the
textbook design of the pattern.
This pattern shows up so often because it’s a great design tool
for creating frameworks, where the framework controls how
something gets done, but leaves you (the person using the
framework) to specify your own details about what is actually
happening at each step of the framework’s algorithm.
Let’s take a little safari through a few uses in the wild (well,
okay, in the Java API)...


                                     In training, we study the classic
                                        patterns. However, when we are out in
                                  the real world, we must learn to recognize
                                 the patterns out of context. We must also
                                       learn to recognize variations of patterns,
                                  because in the real world a square hole is
                                            not always truly square.


                                                                       you are here 4      301


---

## PDF page 340

sorting with template method

Sorting with Template Method

What’s something we often need to do with arrays?
Sort them!                                                           We’ve pared down this
Recognizing that, the designers of the Java Arrays class              code a little to make
have provided us with a handy template method for                     it easier to explain. If
sorting. Let’s take a look at how this method operates:                 you’d like to see it all,                                                                grab the Java source
                                                               code and check it out... We actually have two methods here and they act together to provide the sort functionality.
                                                                        that creates a                                                                method                                                                                   array to                                                                        is just a helper                                                            sort(),                                                                                    destination                                                                the                                                                  as                                           method,                                           first                                                                it along                            The                                                               passes                                                                                   length of the                                              and                                                                   the                                             array                                                                            along                                      the                                of                                                                        passes                                                                      also                                  copy                                                         It                                                                                    element.                                                 method.                                                                               first                                                        at the                                        mergeSort()                                                            start                                the                                                  to                                                     sort                                             the                                                        tells                                    and                                   array
   public static void sort(Object[] a) {
       Object aux[] = (Object[])a.clone();
       mergeSort(aux, a, 0, a.length, 0);
   }
                                         The mergeSort() method contains the sort algorithm, and
                                                                relies on an implementation of the compareTo() method to
                                                  complete the algorithm. If you’re interested in the nitty-
                                                    gritty of how the sorting happens, you’ll want to check out
                                               the Java source code.
                                                                                   Think of this as the
                                                                                       template method.   private static void mergeSort(Object src[], Object dest[],
                int low, int high, int off)
   {
       // a lot of other code here
       for (int i=low; i<high; i++){
           for (int j=i; j>low &&
                ((Comparable)dest[j-1]).compareTo((Comparable)dest[j])>0; j--)
           {
               swap(dest, j, j-1);                                  compareTo() is the method we                                                                                       to “fill out”                                                                            to implement                                                                         need           }                  This is a concrete method, already                                                                                     method.                                                                                template                                                                       the       }                       defined in the Arrays class.
       // and a lot of other code here
   }

302      Chapter 8


---

## PDF page 341

the template method pattern

We’ve got some ducks to sort...

Let’s say you have an array of ducks that you’d like to sort. How do
you do it? Well, the sort() template method in Arrays gives us the
algorithm, but you need to tell it how to compare ducks, which you do by
implementing the compareTo() method... Make sense?

                           No, it doesn’t.
                       Aren’t we supposed to be
                       subclassing something? I thought                               We’ve got an array of
                    that was the point of Template                                  ducks we need to sort.
                   Method. An array doesn’t subclass
                      anything, so I don’t get how we’d
                            use sort().


                               Good point. Here’s the deal: the designers of sort() wanted
                                                                 it to be useful across all arrays, so they had to make sort() a
                                                    static method that could be used from anywhere. But that’s
                                            okay, since it works almost the same as if it were in a superclass.
                                   Now, here is one more detail: because sort() really isn’t defined
                                             in our superclass, the sort() method needs to know that you’ve
                                     implemented the compareTo() method, or else you don’t have
                                          the piece needed to complete the sort algorithm.
                                To handle this, the designers made use of the Comparable
                                                interface. All you have to do is implement this interface, which
                                        has one method (surprise): compareTo().

What is compareTo()?
The compareTo() method compares two objects and returns whether one is less than, greater than,
or equal to the other. sort() uses this as the basis of its comparison of objects in the array.

                                                                           I don’t
                                                                             know. That’s what            Am I greater                                                                       compareTo() tells us.                  than you?


                                                                       you are here 4      303


---

## PDF page 342

implementing comparable

Comparing Ducks and Ducks

Okay, so you know that if you want to sort Ducks,
you’re going to have to implement this compareTo()
method; by doing that, you’ll give the Arrays class
what it needs to complete the algorithm and sort
your ducks.
Here’s the duck implementation:
                                           Remember, we need to implement the Comparable                                                 interface since we aren’t really subclassing.
 public class Duck implements Comparable<Duck> {
     String name;
     int weight;                                  Our Ducks have a name and a weight.

     public Duck(String name, int weight) {
         this.name = name;
         this.weight = weight;
     }
                                                             We’re keepin’ it simple; all Ducks do is
     public String toString() {                      print their name and weight!
         return name + " weighs " + weight;
     }
                                                 Okay, here’s what sort() needs...

     public int compareTo(Duck otherDuck) {
                                                          compareTo() takes another Duck to compare THIS Duck to.
         if (this.weight < otherDuck.weight) {                                                                                         Here’s where we specify how Ducks
             return -1;                                                   compare. If THIS Duck weighs less
         } else if (this.weight == otherDuck.weight) {          than otherDuck, we return -1; if
                                                                           they are equal, we return 0; and             return 0;                                                                                          if THIS Duck weighs more, we         } else { // this.weight > otherDuck.weight                                                                                return 1.
             return 1;
         }
     }
 }


304      Chapter 8


---

## PDF page 343

the template method pattern

Let’s sort some Ducks

Here’s the test drive for sorting Ducks...
           public class DuckSortTestDrive {
               public static void main(String[] args) {
                   Duck[] ducks = {                                                                        of                                    new                                        Duck("Daffy",                                                      8),                                                                      an array                                                        We need                                                                                              good.                                                                                            look                                    new                                        Duck("Dewey",                                                      2),                                                                                  these                                                                              Ducks;                                    new Duck("Howard", 7),
                                    new Duck("Louie", 2),
                                    new Duck("Donald", 10),
                                    new Duck("Huey", 2)
                    };
Notice that we                                                                 Let’s print them to see                   System.out.println("Before sorting:"); call Arrays’ static                                                                  their names and weights.                   display(ducks);method sort(), and
pass it our Ducks.                   Arrays.sort(ducks);                                  It’s sort time!
                   System.out.println("\nAfter sorting:");                                                                           Let’s print them (again) to see                   display(ducks);                                                                               their names and weights.               }
               public static void display(Duck[] ducks) {
                   for (Duck d : ducks) {
                       System.out.println(d);
                   }
               }
           }                                                                                       File Edit  Window Help DonaldNeedsToGoOnADiet
                                                     %java DuckSortTestDrive
                                                  Before sorting:
                                                  Daffy weighs 8          Let the sorting commence!                                                  Dewey weighs 2      The unsorted Ducks
                                                  Howard weighs 7
                                                  Louie weighs 2
                                                  Donald weighs 10
                                                 Huey weighs 2
                                                  After sorting:
                                                  Dewey weighs 2       The sorted Ducks
                                                  Louie weighs 2
                                                 Huey weighs 2
                                                  Howard weighs 7
                                                  Daffy weighs 8
                                                  Donald weighs 10
                                                    %

                                                                       you are here 4      305


---

## PDF page 344

behind the scenes: sorting ducks

The making of the sorting duck machine           Behind
Let’s trace through how the Arrays sort() template method works.                 the Scenes
We’ll check out how the template method controls the algorithm,
and at certain points in the algorithm, how it asks our Ducks to
supply the implementation of a step...
                                                          for (int i=low; i<high; i++){
                                                                  ... compareTo() ...
                                                                  ... swap() ...
   1      First, we need an array of Ducks:                       }

             Duck[] ducks = {new Duck("Daffy", 8), ... };
                                                                   The sort() method controls
   2    Then we call the sort() template method in the Arrays                   the algorithm; no class can
              class and pass it our ducks:                                              change this. sort() counts
                                                                               on a Comparable class to
            Arrays.sort(ducks);                                              provide the implementation
                                                                        of compareTo().
         The sort() method (and its helper, mergeSort()) control
            the sort procedure.

   3    To sort an array, you need to compare two items one
           by one until the entire list is in sorted order.
        When it comes to comparing two ducks, the sort()
          method relies on the Duck’s compareTo() method
             to know how to do this. The compareTo() method
                 is called on the first duck and passed the duck to be
          compared to:
                                                                                                   Duck
            ducks[0].compareTo(ducks[1]);                                                                                                                               compareTo()
                                                                                                                                                              toString()
            First Duck                                    Duck to compare it to                                                                          No inheritance,
                                                                                                                   unlike a typical   4      If the Ducks are not in sorted order, they’re swapped with                                                                                               template method.            the concrete swap() method in Arrays:
            swap()                                                                                      Arrays
                                                                                                                                                                       sort()
                                                                                                                                 swap()
   5   The sort() method continues comparing and swapping Ducks
              until the array is in the correct order!


306      Chapter 8


---

## PDF page 345

the template method pattern


       Is this really the Template Method Pattern, or are you               This implementation of sorting actually seems more likeQ:                       Q:
 trying too hard?                                                  the Strategy Pattern than the Template Method Pattern. Why do
                                                  we consider it Template Method?
     The pattern calls for implementing an algorithm and lettingA:subclasses supply the implementation of the steps—and the Arrays           You’re probably thinking that because the Strategy Pattern uses                          A: sort() is clearly not doing that! But, as we know, patterns in the           object composition. You’re right in a way—we’re using the Arrays
 wild aren’t always just like the textbook patterns. They have to be        object to sort our array, so that’s similar to Strategy. But remember,
 modified to fit the context and implementation constraints.                  in Strategy, the class that you compose with implements the
                                                                               entire algorithm. The algorithm that Arrays implements for sort() is
The designers of the Arrays sort() method had a few constraints. In      incomplete; it needs a class to fill in the missing compareTo() method.
general, you can’t subclass a Java array and they wanted the sort to     So, in that way, it’s more like Template Method.
be used on all arrays (and each array is a different class). So they
defined a static method and deferred the comparison part of the             Are there other examples of template methods in the Java                         Q:
algorithm to the items being sorted.                              API?

So, while it’s not a textbook template method, this implementation is           Yes, you’ll find them in a few places. For example, java.io has a                          A: still in the spirit of the Template Method Pattern. Also, by eliminating      read() method in InputStream that subclasses must implement and is
 the requirement that you have to subclass Arrays to use this           used by the template method read(byte b[], int off, int len).
algorithm, they’ve made sorting in some ways more flexible and
 useful.


         We know that we should favor composition over inheritance, right? Well, the
             implementers of the sort() template method decided not to use inheritance and
              instead to implement sort() as a static method that is composed with a Comparable
                at runtime. How is this better? How is it worse? How would you approach this
            problem? Do Java arrays make this particularly tricky?


            2


             Think of another pattern that is a specialization of the template method. In
                 this specialization, primitive operations are used to create and return objects.
           What pattern is this?


                                                                       you are here 4      307


---

## PDF page 346

the paint hook

Swingin’ with Frames

Up next on our Template Method safari...keep your eye out for swinging JFrames!
If you haven’t encountered JFrame, it’s the most basic Swing container and inherits a
paint() method. By default, paint() does nothing because it’s a hook! By overriding paint(),
you can insert yourself into JFrame’s algorithm for displaying its area of the screen and
have your own graphic output incorporated into the JFrame. Here’s an embarrassingly
simple example of using a JFrame to override the paint() hook method:
                                                                 We’re extending JFrame, which contains a                                                        method update() that controls the algorithm                                                            for updating the screen. We can hook into that                                                                   algorithm by overriding the paint() hook method.
     public class MyFrame extends JFrame {
                                                                               Don’t look behind the
         public MyFrame(String title) {                                        curtain! Just some
             super(title);                                                                initialization here...
             this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
             this.setSize(300,300);
             this.setVisible(true);
         }                                                                 JFrame’s update algorithm calls paint(). By
         public void paint(Graphics graphics) {           default, paint() draws nothing...it’s a hook.                                                                      We’re overriding paint() and telling the             super.paint(graphics);                                                         JFrame to draw a message in the window.             String msg = "I rule!!";
             graphics.drawString(msg, 100, 100);
         }
         public static void main(String[] args) {
             MyFrame myFrame = new MyFrame("Head First Design Patterns");
         }
     }


                                                                  Here’s the message that gets
                                                             painted in the frame because we’ve
                                                         hooked into the paint() method.


308      Chapter 8


---

## PDF page 347

the template method pattern

Custom Lists with AbstractList

Our final stop on the safari: AbstractList.
The list collections in Java, like ArrayList and LinkedList,
extend the AbstractList class, which provides some of the                AbstractList
basic implementations for list behavior. If you want to                 subList()                                      get(3);
create your own custom list—say, a list that contains only             get(int)                                          size();
Strings—you can do that by extending AbstractList so                 size()
you get that basic list behavior for free.                                              iterator()
                                                                                    hashCode()
AbstractList has a template method, subList(), that relies                     // other methods
on two abstract methods, get() and size(). So when you
extend AbstractList to create your own custom list, you’ll
provide implementations for these methods.
                                                                                    MyList
Here’s an implementation of a custom list that contains                                                                                                                  get(int)
only String objects, and uses arrays for the underlying                                                                                                             size()
implementation:
                                                                We create a custom list by  public class MyStringList extends AbstractList<String> {                                                                                   extending AbstractList.         private String[] myList;
         MyStringList(String[] strings) {
               myList = strings;
        }                                                       We must implement the methods get()         public String get(int index) {                                                              and size(), which are both used by               return myList[index];                                                               the template method subList().        }
         public int size() {
               return myList.length;
        }
         public String set(int index, String item) {                                                        We also implement a method set()               String oldString = myList[index];                                                                          so we can modify the list.               myList[index] = item;
               return oldString;
        }
  }

Test the subList() template method in your MyStringList implementation like this:
  String[] ducks = { "Mallard Duck", "Redhead Duck", "Rubber Duck", "Decoy Duck"};
  MyStringList ducksList = new MyStringList(ducks);
  List ducksSubList = ducksList.subList(2, 3);                                                        Create a sublist of one item starting at
                                                             index 2...the Rubber Duck, of course.

                                                                       you are here 4      309


---

## PDF page 348

fireside chats: template method and strategy


                                            Tonight’s talk: Template Method and Strategy
                                     compare methods.


Template Method:                                       Strategy:                        Factory Method
Hey Strategy, what are you doing in my chapter?
I figured I’d get stuck with someone boring like
Factory Method.                                                              Hey, I heard that!


                                                        Nope, it’s me, although be careful—you and Factory
                                                   Method are related, aren’t you?
I was just kidding! But seriously, what are you doing
here? We haven’t heard from you in seven chapters!
                                                                           I’d heard you were on the final draft of your chapter
                                                     and I thought I’d swing by to see how it was going.
                                          We have a lot in common, so I thought I might be
                                                                 able to help...
You might want to remind the reader what you’re
all about, since it’s been so long.

                                                                             I don’t know, since Chapter 1, people have been
                                                               stopping me in the street saying, “Aren’t you that
                                                                        pattern...?” So I think they know who I am. But
                                                                        for your sake: I define a family of algorithms and
                                                  make them interchangeable. Since each algorithm is
                                                                 encapsulated, the client can use different algorithms
Hey, that does sound a lot like what I do. But my                       easily.
intent’s a little different from yours; my job is to
define the outline of an algorithm, but let my
subclasses do some of the work. That way, I can
have different implementations of an algorithm’s
individual steps, but keep control over the
algorithm’s structure. Seems like you have to give up
control of your algorithms.
                                                          I’m not sure I’d put it quite like that...and anyway,
                                                          I’m not stuck using inheritance for algorithm
                                                               implementations. I offer clients a choice of
                                                              algorithm implementation through object
                                                               composition.

310      Chapter 8


---

## PDF page 349

the template method pattern


Template Method:                                       Strategy:
I remember that. But I have more control over
my algorithm and I don’t duplicate code. In fact,
if every part of my algorithm is the same except
for, say, one line, then my classes are much more
efficient than yours. All my duplicated code gets put
into the superclass, so all the subclasses can share it.
                                                   You might be a little more efficient (just a little) and
                                                                  require fewer objects. And you might also be a little
                                                                                 less complicated in comparison to my delegation
                                                           model, but I’m more flexible because I use object
                                                               composition. With me, clients can change their
                                                                algorithms at runtime simply by using a different
                                                                     strategy object. Come on, they didn’t choose me for
                                                         Chapter 1 for nothing!
Yeah, well, I’m real happy for ya, but don’t forget
I’m the most used pattern around. Why? Because I
provide a fundamental method for code reuse that
allows subclasses to specify behavior. I’m sure you
can see that this is perfect for creating frameworks.                                                            Yeah, I guess...but what about dependency? You’re
                                                   way more dependent than me.
How’s that? My superclass is abstract.
                                                         But you have to depend on methods implemented
                                                                     in your subclasses, which are part of your algorithm.
                                                                             I don’t depend on anyone; I can do the entire
                                                              algorithm myself!
Like I said, Strategy, I’m real happy for you. Thanks
for stopping by, but I’ve got to get the rest of this
chapter done.
                                                          Okay, okay, don’t get touchy. I’ll let you work, but let
                                            me know if you need my special techniques anyway;
                                                          I’m always glad to help.
Got it. Don’t call us, we’ll call you...


                                                                       you are here 4      311


---

## PDF page 350

crossword puzzle

          Design Patterns Crossword
                            It’s that time again...

                                         1                          2        3

         4    5

                                                                                                        6

                                                  7


                                                                                      8

                       9                          10                                  11

                                     12


              13

                                                  14


                                                                         15

                                16


ACROSS                          DOWN
1. Huey, Louie, and Dewey all weigh __________ pounds.     1. Coffee and ______.
 2. The template method is usually defined in an _______       3. Factory Method is a __________ of Template Method.
 class.                                                             5. A template method defines the steps of an ________.
 4. In this chapter we gave you more _________.                6. Big-headed pattern.
 7. The steps in the algorithm that must be supplied by the      8. _______ algorithm steps are implemented by hook
 subclasses are usually declared ___________.              methods.
11. The JFrame hook method that we overrode to print “I       9. Our favorite coffee shop in Objectville.
 rule!!”                                                            10. The Arrays class implements its template method as
12. ___________ has a subList() template method.          a ______ method.
13. Type of sort used in Arrays.                              15. A method in the abstract superclass that does nothing
14. The Template Method Pattern uses _____________       or provides default behavior is called a ____________
 to defer implementation to other classes.                   method.
15. “Don’t call us, we’ll call you” is known as the
_________ Principle.


312      Chapter 8


---

## PDF page 351

the template method pattern

        Tools for your Design Toolbox

           We’ve added Template Method to your toolbox.                                                           A template method defines the
           With Template Method, you can reuse code like a                                                                                     steps of an algorithm, deferring to
            pro while keeping control of your algorithms.                                                                                  subclasses for the implementation
                                                                                                 of those steps.
                                                           The Template Method Pattern
                                                                                       gives us an important technique               Basics                                                    for code reuse.       OO
                                                           The                                                                                         template                                                                                            method’s                                                                                                                   abstract    Principles       Abstraction                                                                                         class                                                                    may define                                                                                                     concreteOO                              Encapsulation
           what varies.                                                            methods, abstract methods, and  Encapsulate                   Polymorphism                                          hooks.                  over inheritance.  Favor composition               Inheritance                               Abstract methods are
                interfaces, not                                                        implemented by subclasses.   Program to    implementations.                              designs                                      Hooks are methods that do                     coupled                 loosely     Strive for                 that interact.                                                          nothing or default behavior in             objects     between                                                                            the abstract class, but may be                               extension                                                         principle             should be open for                               Our newest                                                  your                  overridden in the subclass.      Classes                      modification.                                           that              for                                         you           closed     but                                       reminds                                                        running                                                           To                                                                                        prevent                                                                                            subclasses                                                                                                     from                                            are                   Do not                                              superclasses                   abstractions.                                            them call                                                                                changing                                                                                                 the                                                                                                      algorithm                                                                                                                                   in the            on                                                 let      Depend                                          so                               classes.                                                   when                 concrete            on                                 the show,                                                                                     template                                                                                      method,                                                                                                        declare                                                                                                                the                                               methods       depend                                                   subclass                                                        just like              template method as final.                          friends.                your                                                needed,        Talk only to your                                          they’re                                                      Hollywood.           The Hollywood Principle guides us        Don’t call us, we’ll call you.              they do in                                                                                                 to put decision making in high-
                                        And our newest                 level modules that can decide
                                                pattern lets classes        how and when to call low-level                                                                                modules.                                                        an                                                     implementing   Patterns                                   algorithms,OO                     of                       family                      one-to-many                                                             some                a                                                        defer               a                                                                                                       You’ll                                                                                see                                                                                                                    lots                                                                                                                of                                                                                           uses                                                                                                                         of                                                                                                               the                                                     algorithm              defines      -                         them                defines         -                             additional                              an                           that                       makes                          so                  and                 Attach           - Strategy                  -                  one,                               an                       objects   Observer                                    algorithm                                                                                Template                                                                                 Method                                                                                                         Pattern                                                                                                                                      in            each                              Providedynamically.                          the                                                      steps to subclasses.                              Define                   -                                     its                            lets             between              Factory                        object                                      all    Decorator                           of  encapsulates                 an                                         one                                              it.                 Strategy               to                            state,                                   use                                       has                                  but                                 families    dependency             Method      Abstract                           that                                        only                                                                                            real-world                                                                                            code,                                                                                                       but                                                                                                           (as                                                                                                                   with                                                                                                   any                   changes                                    object,                                       class                      creatingclients                         an                     a       responsibilities   interchangeable.             object        Factory               for               a                            updated                                 without        one                             flexibleEnsure               -                                 of                         creating                                           request                      and                          a                 providefrom    when         interface                 for                            objects                                        pointto                                 extending                                        class                                                                                              pattern)                                                                                                      don’t                                                                                               expect                                                                                                                                                                                                        it                                                                                                                                                        all                                                                                                                             to                                                                                               be                         for   vary                                      global              are                     a            interface        independentlyDecorators           Singleton                  depedentnotified                            which                               Encapsulates                 -                                             request                           a                       subclassing                          provide                       decide                                       classes.                                      you              to     dependents         related                  and                                         lets                                       letting                       concrete             orCommand                 subclasses                                Encapsulates                                                                                designed                                                                                                 “by                                                                                                    the                                                                                                        book.”                  -               instance           let                         Method       alternative                   their                           thereby                                              requestyou                            a                        object,                           it.Factory      automatically                                         different           specifying             Adapter                an                                 theletting                to               as                             towith                              thereby                                  Encapsulates               access                   -                                             the              instantiate.        functionality.                                  clients                                           you                          object,                                            different                                      and                                           Define                 an                           instantiation                            -                                                                                                      letting                 as                                                                       The                                                                                           Strategy                                                                                    and                                                                                                Template                                   with               Facade                 defer                                          requests,                 parameterize                                     clients                                 thereby                                  log                class        a                      Method                         or                                                           operation,                             object,                                        an                                               different                         queue                                        andin                   as                                            requests,                    parameterize                                      with                    anTemplate                                                                         Method                                                                                               Patterns                                                                                                   both                                                                                                       encapsulate                    requests,                                         algorithm                           or                                        clients                             anlog               subclasses.                                          and                            queue                                      operations.of                                    to subclasses.                  supportrequests,parameterizeundoableskeleton                                         operations.or logstepsrequests,                                                        redefine                         algorithms, the first by composition                            undoablequeuesome                     supportrequests,deferring                                            operations.lets subclasses                                                    without                      and the other by inheritance.                               undoableMethod                       supportTemplate                                               algorithm                                                      structure.                    Factory Method is a specialization                            certain steps of an                              the algorithm’s                             changing                                                          of Template Method.


                                                                     you are here 4      313


---

## PDF page 352

exercise solutions


                                          Draw the new class diagram now that we’ve moved
                                                   prepareRecipe() into the CaffeineBeverage class:


                                                     CaffeineBeverage
                                                     prepareRecipe()
                                                             boilWater()
                                                       pourInCup()
                                                         brew()
                                                    addCondiments()


                                           Coffee                         Tea
                                      brew()                               brew()
                                   addCondiments()                    addCondiments()


                     SOlUTion

               Match each pattern with its description:

           Pattern                Description

                                                       Encapsulate interchangable
                Template Method                     behaviors and use delegation to
                                                    decide which behavior to use.

                                                        Subclasses decide how to
                  Strategy                                                 implement steps in an algorithm.


                                                        Subclasses decide which
                     Factory Method                                                        concrete classes to create.


314      Chapter 8


---

## PDF page 353

the template method pattern

     Design Patterns Crossword Solution
                It’s that time again...


                                1                          2        3                   T W O         A  B  S  T  R  A  C  T
4    5 C  A  F  F  E  I N  E                           P
                                                                                               6    L              A                      E               S
                                         7   G                   A  B  S  T  R  A  C  T            T
   O                                             I                 R
                                                                             8   R                                  A    O         A
              9                          10                                  11    I    S               S                   L      P  A  I N  T
                           12   T    T      A  B  S  T  R  A  C  T  L  I  S  T           E
   H    A              A               Z     I          G
     13  M  E  R  G  E  S O  R  T              A    O          Y
                                         14         B                   I N H  E  R  I  T A N  C  E
        U                 C                   I    A
                                                               15        Z                         H O  L  L  Y W O O  D
                       16        Z     C O M  P O  S  I  T  I O N
                                O
                                          K


                                                               you are here 4      315
