# 3: the Decorator Pattern: Decorating Objects

_Extracted from PDF pages 117-146. Text only; images and diagrams are not embedded._


---

## PDF page 117

3 the Decorator Pattern
    DecoratingObjects


     I used to think real men
      subclassed everything. That was
       until I learned the power of
      extension at runtime, rather than
      at compile time. Now look at me!


       Just call this chapter “Design Eye for the Inheritance Guy.”
            We’ll re-examine the typical overuse of inheritance and you’ll learn how to decorate
          your classes at runtime using a form of object composition. Why? Once you know the
          techniques of decorating, you’ll be able to give your (or someone else’s) objects new
            responsibilities without making any code changes to the underlying classes.


                                                                            this is a new chapter      79


---

## PDF page 118

the starbuzz story

Welcome to Starbuzz Coffee

Starbuzz Coffee has made a name for itself as the fastestgrowing coffee shop around. If you’ve seen one on your local
corner, look across the street; you’ll see another one.
Because they’ve grown so quickly, they’re scrambling to update
their ordering systems to match their beverage offerings.
When they first went into business they designed their classes
like this...

                                 is an abstract class,                 Beverage                       by all beverages                   subclassed                 offered in the coffee shop.

                                            Beverage            The description instance variable
                                                                                                    is set in each subclass and holds a
                                                         description                      description of the beverage, like
   The cost() method is                           getDescription()              “Most Excellent Dark Roast”.
                                                                                method    abstract; subclassses                             cost()                   The getDescription()    need to define their                                                                          returns the description.   own implementation.                                            // Other useful methods...


            HouseBlend               DarkRoast                  Decaf                 Espresso
             cost()                              cost()                              cost()                             cost()


                        Each subclass implements cost() to return the cost of the beverage.


80      Chapter 3


---

## PDF page 119

the decorator pattern


In addition to your coffee, you can also ask for several
condiments like steamed milk, soy, and mocha (otherwise
known as chocolate), and have it all topped off with whipped
milk. Starbuzz charges a bit for each condiment, so they really
need to get them built into their order system.
 Here’s their first attempt...

                                                                                     Beverage

                                                                                                           description

                                                                                                          getDescription()
                                                                                                                cost()

                                                                                                                                                                         // Other useful methods...


                                                                                                                                       EspressoWithSteamedMilk
                                                                                 DarkRoastWithSteamedMilk                                           HouseBlendWithSteamedMilk                                                                                                                               andMocha
                                                                               andMocha           DecafWithSteamedMilk                                               andMocha                                                                                                      andMocha                cost()                                HouseBlendWithSteamedMilk
                                       andCaramelcost()                                             cost()                               cost()
                                      HouseBlendWithWhipandMocha                                                              EspressoWithSteamedMilk                                               cost()
                                                                  DarkRoastWithSteamedMilk              DecafWithSteamedMilk             andCaramel
                                                            cost()                          andCaramel                        andCaramel               cost()   EspressoWithWhipandMocha
                                 HouseBlendWithMocha                                                                                              cost()              DarkRoastWithWhipandMochacost()             DecafWithWhipandMocha
                                               cost()                HouseBlendWithSoyandMocha                                                                                cost()EspressoWithMocha
                                      HouseBlendWithSteamedMilk                                            andSoycost()            DarkRoastWithMochacost()                   DecafWithMochacost()                 cost()
                                                                                                                                          EspressoWithSteamedMilk                                                                                                                                                 DecafWithSoy                                                                                                                                                     cost()                                                   HouseBlendWithSoycost()                                                        cost()                                                                                                                                       andSoy                                                                                                                DecafWithSteamedMilk                                                                                                                                                                                                           cost()                                                                          DarkRoastWithSteamedMilk                               HouseBlendWithSteamedMilk                                                                       cost()                                                                                                            andSoy EspressoWithSteamedMilkcost()                                                                            andSoy
                                                                                                                           DarkRoastWithSoy                                              cost()                                    HouseBlendWithWhip                                                                                                  DecafWithSteamedMilkcost()                                                                                                                                                                                   cost()                                                            DarkRoastWithSteamedMilkcost()                                                                                                                                        DecafWithSoyandMocha                                                                                               DarkRoastWithSoy                                                                                DarkRoastWithSoyandMocha                                                                                                                                                                               cost()                                                  cost()                                                                                                                                DecafWithSoy                                                                                                                                         cost()                                                                                                            DecafWithSoyandMocha                                                HouseBlendWithSteamedMilkcost()                                                                                                                                     cost()
                                                     andWhip                          cost()                                                   cost()           EspressoWhipcost()
                                HouseBlendWithWhipandSoycost()                 DarkRoastWithWhip                    DecafWithWhipcost()                      cost()
                                                                                                 cost()                                              cost()                                    EspressoWithSteamedMilk
                                                                                                                                         andWhip                                                 cost()                                                                                                                           DecafWithSteamedMilk                                                                                     DarkRoastWithSteamedMilk
                                                                                      andWhip                                                                                                                      andWhipEspressoWithWhipandSoycost()
                                                              DarkRoastWithWhipandSoycost()             DecafWithWhipandSoycost()
                                                                                                                                                                                                 cost()
                                                                                            cost()                                              cost()


                                                                                         the                                                                                        computes                                                                         method                                                                                cost                                                                Each                            Whoa!                                                                                           the                                                                                                   along with                                                                                    coffee                                                                         the                                                                           cost of                          Can                               you say                                                                                                       in the order.                               “class explosion”?                           other condiments


                                                                        you are here 4      81


---

## PDF page 120

violating design principles


                             It’s pretty obvious that Starbuzz has created a maintenance
                   nightmare for themselves. What happens when the price of milk
                 goes up? What do they do when they add a new caramel topping?
                   Thinking beyond the maintenance problem, which of the design
                      principles that we’ve covered so far are they violating?

                                                    way! big a in them of two violating they’re Hint:


                                 This is stupid; why
                        do we need all these classes?
                            Can’t we just use instance variables
                       and inheritance in the superclass to
                       keep track of the condiments?


                           Well, let’s give it a try. Let’s start with the Beverage base class
                      and add instance variables to represent whether or not each
                         beverage has milk, soy, mocha, and whip...


                                          Beverage
                                                       New boolean values for                                                description
                                               milk                                   each condiment.
                                        soy
                                   mocha
                                         whip                                                Now we’ll implement cost() in Beverage (instead of
                                                                    keeping it abstract), so that it can calculate the                                                getDescription()                                                  cost()                             costs associated with the condiments for a particular
                                                                beverage instance. Subclasses will still override
                                               hasMilk()                             cost(), but they will also invoke the super version so                                                  setMilk()                                          hasSoy()                       that they can calculate the total cost of the basic
                                             setSoy()                          beverage plus the costs of the added condiments.
                                        hasMocha()
                                          setMocha()                                         hasWhip()                  These get and set the boolean                                                                           condiments.                                            setWhip()                                                                   values for the
                                                                           // Other useful methods..


82      Chapter 3


---

## PDF page 121

the decorator pattern


                                                            Beverage
   Now let’s add in the subclasses, one for                                                                          description
     each beverage on the menu:                          milk
                                                               soy
                                                      mocha
                                                               whip
                           calculate the                   getDescription()               cost() will The superclass                   while                    cost()              the condiments,  costs for all of                 cost()                        in the subclasses                  hasMilk()      overridden the                                    include                          to                                                                             setMilk()                   functionality           that     extend  will                                  type.                                                                 hasSoy()                        beverage                  specific       for that                                                                      setSoy()  costs
                                                              hasMocha()                        to compute                                                                 setMocha()    Each cost() method needs                             then                        and                    beverage                                                                    setWhip()    the cost of the                                       hasWhip()                     by calling the               condiments    add in the                      of cost().                           // Other useful methods..              implementation      superclass


                   HouseBlend               DarkRoast                  Decaf                 Espresso
                        cost()                              cost()                              cost()                             cost()


                                        Write the cost() methods for the following classes (pseudo-Java is okay):

public class Beverage {            public class DarkRoast extends Beverage {
    public double cost() {
                                       public DarkRoast() {
                                           description = "Most Excellent Dark Roast";
                                       }
                                       public double cost() {


    }
}
                                       }
                                   }


                                                                     you are here 4      83


---

## PDF page 122

impact of change


                    See, five classes
                        total. This is definitely
                   the way to go.


                                                   I’m not so sure; I can see some
                                                        potential problems with this approach
                                              by thinking about how the design might
                                               need to change in the future.


    What requirements or other factors might change that will impact this design?

      Price changes for condiments will force us to alter existing code.

    New condiments will force us to add new methods and alter the cost method in the superclass.
                                                                                                     in                                                                       As we saw                                                                                                          this is                                                                                                                1,    We may have new beverages. For some of these beverages (iced tea?), the condiments may                                                                                     Chapter                                                                                                                idea!     not be appropriate, yet the Tea subclass will still inherit methods like hasWhip().            a very bad

    What if a customer wants a double mocha?
     turn:Your


84      Chapter 3


---

## PDF page 123

the decorator pattern


          Guru and Student...
             Guru: It has been some time since our last meeting. Have you
             been deep in meditation on inheritance?
            Student: Yes, Guru. While inheritance is powerful, I have
             learned that it doesn’t always lead to the most flexible or
maintainable designs.
Guru: Ah yes, you have made some progress. So, tell me, my student, how
then will you achieve reuse if not through inheritance?
Student: Guru, I have learned there are ways of “inheriting” behavior at
runtime through composition and delegation.
Guru: Please, go on...
Student: When I inherit behavior by subclassing, that behavior is set statically
at compile time. In addition, all subclasses must inherit the same behavior. If,
however, I can extend an object’s behavior through composition, then I can
do this dynamically at runtime.
Guru: Very good; you are beginning to see the power of composition.
Student: Yes, it is possible for me to add multiple new responsibilities to
objects through this technique, including responsibilities that were not even
thought of by the designer of the superclass. And I don’t have to touch their
code!
Guru: What have you learned about the effect of composition on maintaining
your code?
Student: Well, that is what I was getting at. By dynamically composing
objects, I can add new functionality by writing new code rather than altering
existing code. Because I’m not changing existing code, the chances of
introducing bugs or causing unintended side effects in pre-existing code are
much reduced.
Guru: Very good. Enough for today. I would like for you to go and meditate
further on this topic... Remember, code should be closed (to change) like the
lotus flower in the evening, yet open (to extension) like the lotus flower in the
morning.


                                                         you are here 4      85


---

## PDF page 124

the open-closed principle

The Open-Closed Principle

    We're on to one of the most important design principles:


                                  Design Principle
                                           Classes should be open
                                                        for extension, but closed for
                                                 modification.


                           Come on in; we’re
                                     open. Feel free to extend our
               classes with any new behavior you like.  If your
        needs or requirements change (and we know they
           will), just go ahead and make your own extensions.

                                                           Sorry, we’re closed.
                                                       That’s right, we
                                                       spent a lot of time getting this
                                                  code correct and bug free, so we can’t let you
                                                                 alter the existing code. It must remain closed to
                                                         modification. If you don’t like it, you can speak to
                                                        the manager.


          Our goal is to allow classes to be easily extended to
           incorporate new behavior without modifying existing code.
          What do we get if we accomplish this? Designs that are
             resilient to change and flexible enough to take on new
             functionality to meet changing requirements.


86      Chapter 3


---

## PDF page 125

the decorator pattern


     Open for extension and closed                   Usually, you can’t. Making OO designQ:                A: for modification? That sounds very                flexible and open to extension without
contradictory. How can a design be both?       modifying existing code takes time and effort. In
                                                   general, we don’t have the luxury of tying down
      That’s a very good question. It certainly      every part of our designs (and it would probablyA:sounds contradictory at first. After all, the less     be wasteful). Following the Open-Closed
 modifiable something is, the harder it is to          Principle usually introduces new levels of
extend, right?                                       abstraction, which adds complexity to our code.
                                         You want to concentrate on those areas that are
As it turns out, though, there are some           most likely to change in your designs and apply
clever OO techniques for allowing systems         the principles there.
 to be extended, even if we can’t change the
 underlying code. Think about the Observer          How do I know which areas of change                  Q:
 Pattern (in Chapter 2)...by adding new            are more important?
Observers, we can extend the Subject at
any time, without adding code to the Subject.           That is partly a matter of experienceYou’ll see quite a few more ways of extending  A:in designing OO systems and also a matter
 behavior with other OO design techniques.          of knowing the domain you are working in.
                                              Looking at other examples will help you learn to
      Okay, I understand Observer, but           identify areas of change in your own designs.Q:
how do I generally design something to be
extensible yet closed for modification?

     Many of the patterns give us time-testedA:designs that protect your code from being    While it may seem like a contradiction,
 modified by supplying a means of extension. In this chapter you’ll see a good example of    there are techniques for allowing code to be
 using the Decorator Pattern to follow the Open-Closed Principle.               extended without direct modification.

     How can I make every part of myQ:
design follow the Open-Closed Principle?   Be careful when choosing the areas of code
                         that need to be extended; applying the
                       Open-Closed Principle EVERYWHERE is
                        wasteful and unnecessary, and can lead to
                         complex, hard-to-understand code.


                                                                        you are here 4      87


---

## PDF page 126

meet the decorator pattern


                                                                     Okay, enough of the
                                                               “Object-Oriented Design Club.” We
                                                             have real problems here! Remember us?
                                                          Starbuzz Coffee? Do you think you could use
                                                      some of those design principles to actually
Meet the Decorator Pattern                      help us?

Okay, we’ve seen that representing our beverage and condiments with
inheritance has not worked out very well—we get class explosions and rigid
designs, or we add functionality to the base class that isn’t appropriate for
some of the subclasses.
So, here’s what we’ll do instead: we’ll start with a beverage and “decorate”
it with the condiments at runtime. For example, if the customer wants a
Dark Roast with Mocha and Whip, then we’ll:


    1  Start with a DarkRoast object.

    2  Decorate it with a Mocha object.

    3  Decorate it with a Whip object.

    4  Call the cost() method and rely on delegation to
      add up the condiment costs.


Okay, but how do you “decorate” an object, and how does delegation
come into this? A hint: think of decorator objects as “wrappers.” Let’s see
how this works...


88      Chapter 3


---

## PDF page 127

the decorator pattern

Constructing a drink order with Decorators


     1  We start with our DarkRoast object.                                                                      DarkRoast                                                              that      and has                                                       Remember   Beverage                                                         from       computes                                                                        inherits       that                                                             method                                       a cost()                                                                                     drink.                                                    of the                                                                cost                               cost()             the
                 DarkRoast


     2  The customer wants Mocha, so we create a Mocha
         object and wrap it around the DarkRoast.                                                                                                          Its                                                                                                         is a decorator.                                                      The Mocha object                                                                                              it is decorating—                                                                        the object                                                                 type mirrors         (By “mirror,”                                                                                      Beverage.                                                           a                                                                                      case,                                                                              this                                                                            in                                                                              same type.)                                                                        the                                                                                it is                                                               mean                                                       we
                                                                                                    too,                                                                             method                                    cost()                         cost()                                                        a cost()                                                                         has                                                                                            treat                                                          Mocha                                                                      we can                                                                   So,                    D                              arkRoast                                                                                   polymorphism                                                                                         as                                                                     through                                                          and                                                                         Mocha                                                                                            in                                                                           wrapped                                                                      Beverage                                                                          Mocha is a             Mocha                   any                                                                                       (because                                                                       too                                               a Beverage,                                                           of Beverage).                                                                     subtype

     3  The customer also wants Whip, so we create a Whip
         decorator and wrap Mocha with it.


                                                                  Whip is a decorator, so it also                                 cost()     cost()   cost()                                                                          mirrors DarkRoast’s type and                         DarkRoast
                                                                                 includes a cost() method.                     Mocha
        Whip
                             So, a DarkRoast wrapped in Mocha and Whip is still
                         a Beverage and we can do anything with it we can do
                          with a DarkRoast, including call its cost() method.

                                                                        you are here 4      89


---

## PDF page 128

decorator characteristics


     4 Now it’s time to compute the cost for the customer. We do this by
         calling cost() on the outermost decorator, Whip, and Whip is going to
        delegate computing the cost to the objects it decorates. And so on.
         Let’s see how this works:
                                                                                                              (You’ll see how in
                                                                a few pages.)
                          2 Whip calls cost() on Mocha.
          1 First, we call cost() on the                       3  Mocha calls cost() on
                     outermost decorator, Whip.                                    DarkRoast.


                                   cost()      cost()     cost()                                ast                   $1.29   .10        .20       .99 DarkRo
                      Mocha                                                           4  DarkRoast returns
                                                                                                            its cost, 99 cents.         Whip
             6  Whip adds its total, 10 cents,
                      to the result from Mocha, and       5 Mocha adds its cost, 20 cents,
                       returns the final result—$1.29.            to the result from DarkRoast,
                                                         and returns the new total, $1.19.

    Okay, here’s what we know about Decorators, so far...
          Decorators have the same supertype as the objects they decorate.
         You can use one or more decorators to wrap an object.
         Given that the decorator has the same supertype as the object it decorates, we can
             pass around a decorated object in place of the original (wrapped) object.              point!                                                             Key         The decorator adds its own behavior before and/or after delegating to the object it
              decorates to do the rest of the job.
          Objects can be decorated at any time, so we can decorate objects dynamically at
              runtime with as many decorators as we like.

   Now let’s see how this all really works by looking at the
    Decorator Pattern definition and writing some code.

90      Chapter 3


---

## PDF page 129

the decorator pattern

The Decorator Pattern defined

Let’s first take a look at the Decorator Pattern description:


          The Decorator Pattern attaches additional
                 responsibilities to an object dynamically.
              Decorators provide a flexible alternative to
               subclassing for extending functionality.


While that describes the role of the Decorator Pattern, it doesn’t give us a lot
of insight into how we’d apply the pattern to our own implementation. Let’s
take a look at the class diagram, which is a little more revealing (on the next
page we’ll look at the same structure applied to the beverage problem).
                                                           Each component can be used on its
                                                           own or wrapped by a decorator.
                                              Component
                                                                          component
                                                     methodA()
                                                     methodB()
 The ConcreteComponent                                // other methods                                     Each decorator HAS-A
  is the object we’re going                                                               (wraps) a component, which
 to dynamically add new                                                            means the decorator has an
  behavior to. It extends                                                                     instance variable that holds a
  Component.                  ConcreteComponent                  Decorator                           reference to a component.
                                      methodA()                        Component wrappedObj
                                      methodB()                                                                          methodA()                                           the                                                                        // other methods                                                           implement                                                                          methodB()                            Decorators                                                                                  or abstract                                                                                                                                          // other methods                        same interface       they                                                                                        component                                                                                                class as the                                                                                                decorate.                                                                             are going to


                                                     ConcreteDecoratorA           ConcreteDecoratorB
                                                           methodA()                          Object newState
                                                           methodB()
                                                              newBehavior()     The ConcreteDecorator                                                methodA()                                                                                            methodB()              Decorators can extend the
                                                                                                              // other methods       inherits (from the                                                                                                                                                                           // other methods           state of the component.      Decorator class) an instance
        variable for the thing it
       decorates (the Component
      the Decorator wraps).                       Decorators can add new methods; however, new
                                                      behavior is typically added by doing computation
                                                    before or after an existing method in the component.

                                                                        you are here 4      91


---

## PDF page 130

decorating beverages

Decorating our Beverages

Let’s rework our Starbuzz beverages using the Decorator Pattern...


             acts as our     Beverage             component class.     abstract                                               Beverage                                   component
                                                          description

                                                          getDescription()
                                                             cost()
                                                                                            // other useful methods


      HouseBlend               DarkRoast                                CondimentDecorator
   cost()                              cost()                                               Beverage beverage                Here's the reference to
                                                                                                   getDescription()               the Beverage that the                   Espresso                  Decaf
                                                                             Decorators will be wrapping.                    cost()                              cost()


                                                                     Milk                 Mocha                  Soy                  WhipThe four concrete
                                                                           cost()                              cost()                              cost()                             cost() components, one per
                                                                       getDescription()                  getDescription()                  getDescription()                 getDescription() coffee type.

                                           And here are our condiment decorators; notice
                                                  they need to implement not only cost() but also
                                                         getDescription(). We’ll see why in a moment...


                   Before going further, think about how you’d implement the cost()
                 method of the coffees and the condiments. Also think about how
                    you’d implement the getDescription() method of the condiments.


92      Chapter 3


---

## PDF page 131

the decorator pattern

Cubicle Conversation

Some confusion over Inheritance versus Composition


                     Okay, I’m a little confused...I
                   thought we weren’t going to use   Mary
                   inheritance in this pattern? I thought
                we were going to rely on composition
                                   instead?

                 Sue: What do you mean?
               Mary: Look at the class diagram. The CondimentDecorator is extending the Beverage class.
                     That’s inheritance, right?
                 Sue: True. I think the point is that it’s vital that the decorators have the same type as the objects
                     they are going to decorate. So here we’re using inheritance to achieve the type matching, but we
                       aren’t using inheritance to get behavior.
               Mary: Okay, I can see how decorators need the same “interface” as the components they wrap
                   because they need to stand in place of the component. But where does the behavior come in?
                 Sue: When we compose a decorator with a component, we are adding new behavior. We are
                     acquiring new behavior not by inheriting it from a superclass, but by composing objects together.
               Mary: Okay, so we’re subclassing the abstract class Beverage in order to have the correct type,
                    not to inherit its behavior. The behavior comes in through the composition of decorators with the
                    base components as well as other decorators.
                 Sue: That’s right.
               Mary: Oh, I get it! And because we are using object composition, we get a whole lot more
                          flexibility about how to mix and match condiments and beverages. Very slick.
                 Sue: Yes, if we rely on inheritance, then our behavior can only be determined statically at
                   compile time. In other words, we get only whatever behavior the superclass gives us or that we
                      override. With composition, we can mix and match decorators any way we like...at runtime.
               Mary: I get it—we can implement new decorators at any time to add new behavior. If we relied
                 on inheritance, we’d have to go in and change existing code anytime we wanted new behavior.
                 Sue: Exactly.
               Mary: I just have one more question: if all we need to inherit is the type of the component, how
                come we didn’t use an interface instead of an abstract class for the Beverage class?
                 Sue: Well, remember, when we got this code, Starbuzz already had an abstract Beverage class.
                      Traditionally the Decorator Pattern does specify an abstract component, but in Java, obviously,
                we could use an interface. But we always try to avoid altering existing code, so don’t “fix” it if the
                      abstract class will work just fine.


                                                                        you are here 4      93


---

## PDF page 132

decorator training

New barista training                                                                             Okay, I need for you to
                                                                    make me a double mocha Make a picture for what happens when the order is for a                                                                              soy latte with whip.“double mocha soy latte with whip” beverage. Use the menu to
 get the correct prices, and draw your picture using the same
 format we used earlier (from a few pages back):
                  2 Whip calls cost() on Mocha.
                                         3  Mocha calls cost() on
  1 First, we call cost() on the                                 DarkRoast.      outermost decorator, Whip.                                      was for                                             This picture                                                      mocha                                                       roast                                a “dark                                                          beverage.                                             cost()                                  cost()                       cost()                                                whip”                                      .99 D                           .20                                     arkRoast        $1.29   .10
                 Mocha                                                 4  DarkRoast returns
                                                                                          its cost, 99 cents.      Whip
   6  Whip adds its total, 10 cents,
       to the result from Mocha, and       5 Mocha adds its cost, 20
        returns the final result—$1.29.               cents, to the result from
                                               DarkRoast, and returns
                                             the new total, $1.19.
                                                             Starbuzz Coffee
                                     Draw your picture here.                         Coffees                                                                   House Blend  .89                                                                  Dark Roast   .99                                                                  Decaf                                                                              1.05                                                                   Espresso                                                                              1.99
                                                                   Condiments
                                                                   Steamed Milk  .10                                                                  Mocha                                                                             .20                                                                Soy                                                                             .15                                                                 Whip                                                                             .10


  CoffeeS  z     ta  z     r  u     b
  b     u  r     z  a     z  t
  SeeffoC     makea              can  latte            you  soy        HINT:             mocha                        combining                            shots             by                  two          “doublewhip”                   Soy,         with         Whip!                and             HouseBlend,              Mocha,        of


 94      Chapter 3


---

## PDF page 133

the decorator pattern

Writing the Starbuzz code

It’s time to whip this design into some real code.
Let’s start with the Beverage class, which doesn’t
need to change from Starbuzz’s original design.
Let’s take a look:

                                                                                       abstract          public abstract class Beverage {                       Beverage is an                                                                                    methods              String description = "Unknown Beverage";           class with the two                                                                                                            cost().                                                                             and                                                                                getDescription()
              public String getDescription() {                                                                             getDescription is already                  return description;                                                                          implemented for us, but we
             }                                                       need to implement cost()
                                                                                                in the subclasses.
              public abstract double cost();
         }


Beverage is simple enough. Let’s implement the abstract
class for the Condiments (the Decorator) as well:
                                                                             be                                                                                    First, we need to                                                                   a Beverage,                                                                                    with                                                                                 interchangeable              class.                                                                             the Beverage                                                                       so we extend

          public abstract class CondimentDecorator extends Beverage {
              Beverage beverage;
              public abstract String getDescription();
         }
                                                                                We’re also going to require           Here's the Beverage that each                                                                       that the condiment         Decorator will be wrapping.                                                                               decorators all reimplement the         Notice we are using the                                                                                  getDescription() method. Again,         Beverage supertype to refer to                                                                                                    we’ll see why in a sec...         the Beverage so the Decorator
         can wrap any beverage.


                                                                        you are here 4      95


---

## PDF page 134

implementing the beverages

Coding beverages

Now that we’ve got our base classes out of the way, let’s implement
some beverages. We’ll start with Espresso. Remember, we need to
set a description for the specific beverage and also implement the
cost() method.
                                                                          the Beverage                                                                        extend                                                                       First we                                                                                              beverage.                                                                                        class, since this is a
           public class Espresso extends Beverage {

               public Espresso() {                                                             To take care of the description, we set                   description = "Espresso";                                                                             this in the constructor for the class.
               }                                              Remember, the description instance
                                                                                variable is inherited from Beverage.
               public double cost() {
                   return 1.99;                                                                      We don’t                                                                                              Espresso.               }                                                                           cost of an                                                               the                                                    to compute                                                                                              this class, we just                                                                                            in                                                    need                                          we                                                                           condiments           }                                                         Finally,                                                                              in                                                                 adding                                                        about                                                                                                  $1.99.                                                  worry                                            to                                                                                   Espresso:                                           need                                                              an                                                        of                                                                       price                                                      the                                                      return                                            to                                            need

           public class HouseBlend extends Beverage {
               public HouseBlend() {
                   description = "House Blend Coffee";
               }                                               Coffee                                                     Starbuzz
                                                           Coffees      .89               public double cost() {                             Blend                                                          House       .99                                                               Roast                   return .89;                              Dark        1.05                                                           Decaf       1.99               }          Okay, here’s another Beverage. All we           Espresso           }              do is set the appropriate description,                               “House Blend Coffee,” and then return           Condiments   .10                                                                 Milk                             the correct cost: 89¢.                      Steamed      .20
                                                            Mocha       .15
                                                         Soy         .10
                                                           Whip                 You can create the other two Beverage classses
                 (DarkRoast and Decaf) in exactly the same way.


96      Chapter 3


---

## PDF page 135

the decorator pattern

Coding condiments

If you look back at the Decorator Pattern class diagram, you’ll see
we’ve now written our abstract component (Beverage), we have
our concrete components (HouseBlend), and we have our abstract
decorator (CondimentDecorator). Now it’s time to implement the
concrete decorators. Here’s Mocha:
             Mocha is a decorator, so we               CondimentDecorator                                          Remember,               extend CondimentDecorator.                                                       Beverage.                       Mocha with a                                            extends              We’re going to instantiate                                                                   to a Beverage.                                                                       reference                                                                                    the                                                                                                     inherits                                                                 Remember, this class                                                                                               hold the                                                                                to  public class Mocha extends CondimentDecorator {                                                                                                  variable                                                                                      instance                                                                   Beverage                                                             we are wrapping.                                                                       beverage      public Mocha(Beverage beverage) {                                               variable to the                                                                                         instance                                                    We set this                                                                                                Here, we’re                                                                                         wrapping.          this.beverage = beverage;                                                                       object we are                                                                                             we’re wrapping to                                                                                  beverage      }                                                                      passing the                                                                                             constructor.                                                              the decorator’s
      public String getDescription() {
          return beverage.getDescription() + ", Mocha";
      }
                                                             We want our description to include not
      public double cost() {                                           only the beverage-say “Dark Roast”-
                                                                     but also each item decorating the          return beverage.cost() + .20;                                                                           beverage (for instance, “Dark Roast,      }                                                                       Mocha”). So we first delegate to the
  }                                                                        object we are decorating to get its
                                                                                   description, then append “, Mocha” to                                        beverage                                  our                           of                             cost                      the                                                                    that description.            to compute         need     we                                     the                                  to Now                                           call                            the                we delegate                First,                                         the      Mocha.                                   compute  with                                can                                  it                        that                        so              decorating         we’re  object             add the cost of Mocha to the result.          we   cost; then,
                                       On the next page we’ll actually instantiate the beverage and
                                          wrap it with all its condiments (decorators), but first...


                                Write and compile the code for the other Soy and Whip
                              condiments. You’ll need them to finish and test the application.


                                                                        you are here 4      97


---

## PDF page 136

testing the beverages

Serving some coffees

Congratulations. It’s time to sit back, order a few coffees, and marvel
at the flexible design you created with the Decorator Pattern.
Here’s some test code to make orders:

   public class StarbuzzCoffee {
                                                                               no condiments,                                                                                                espresso,                                                                     up an                                                              Order       public static void main(String args[]) {                                                                                           description and cost.                                                                                           its                                                              and print           Beverage beverage = new Espresso();
           System.out.println(beverage.getDescription()
                  + " $" + beverage.cost());                            object.                                                                DarkRoast                                                 Make a
           Beverage beverage2 = new DarkRoast();                                                       Wrap it with a Mocha.
           beverage2 = new Mocha(beverage2);
                                                       Wrap it in a second Mocha.           beverage2 = new Mocha(beverage2);
           beverage2 = new Whip(beverage2);          Wrap it in a Whip.
           System.out.println(beverage2.getDescription()
                  + " $" + beverage2.cost());

           Beverage beverage3 = new HouseBlend();                                                                                           Finally, give us a HouseBlend           beverage3 = new Soy(beverage3);                                                                        with Soy, Mocha, and Whip.
           beverage3 = new Mocha(beverage3);
           beverage3 = new Whip(beverage3);
           System.out.println(beverage3.getDescription()
                  + " $" + beverage3.cost());
      }
  }                                                                We’re going to see a much better way of creating
                                                               decorated objects when we cover the Factory and
Now, let’s get those orders in:                            Builder Design Patterns. Please note that the
                                                                      Builder Pattern is covered in the Appendix.


                                      File Edit Window Help CloudsInMyCoffee
               % java StarbuzzCoffee
               Espresso $1.99
               Dark  FileRoastEdit WindowCoffee,Help CloudsInMyCoffeeMocha, Mocha, Whip $1.49
               House Blend Coffee, Soy, Mocha, Whip $1.34
               %


98      Chapter 3


---

## PDF page 137

the decorator pattern


      I’m a little worried about code              Wouldn’t it be easy for some client        Can decorators know about theQ:               Q:               Q:
 that might test for a specific concrete        of a beverage to end up with a decorator     other decorations in the chain? Say I
component—say, HouseBlend—and do       that isn’t the outermost decorator? Like     wanted my getDescription() method to
something, like issue a discount. Once           if I had a DarkRoast with Mocha, Soy,         print “Whip, Double Mocha” instead of
 I’ve wrapped the HouseBlend with         and Whip, it would be easy to write code    “Mocha, Whip, Mocha.” That would require
decorators, this isn’t going to work           that somehow ended up with a reference     that my outermost decorator know all the
anymore.                                     to Soy instead of Whip, which means it      decorators it is wrapping.
                                      would not include Whip in the order.
      That is exactly right. If you have code                                                       Decorators are meant to add behaviorA:                                 A: that relies on the concrete component’s            You could certainly argue that you          to the object they wrap. When you need to                 A: type, decorators will break that code. As       have to manage more objects with the         peek at multiple layers into the decorator
 long as you only write code against the         Decorator Pattern and so there is an            chain, you are starting to push the decorator
abstract component type, the use of            increased chance that coding errors will        beyond its true intent. Nevertheless,
decorators will remain transparent to your       introduce the kinds of problems you suggest.   such things are possible. Imagine a
code. However, once you start writing code     However, we typically create decorators        CondimentPrettyPrint decorator that parses
against concrete components, you’ll want to    by using other patterns like Factory and         the final decription and can print “Mocha,
 rethink your application design and your use     Builder. Once we’ve covered these patterns,    Whip, Mocha” as “Whip, Double Mocha.”
 of decorators.                                         you’ll see that the creation of the concrete      Note that getDescription() could return an
                                        component with its decorator is “well             ArrayList of descriptions to make this easier.
                                             encapsulated” and doesn’t lead to these
                                               kinds of problems.


                             Our friends at Starbuzz have introduced sizes to their menu. You can now order a
                                   coffee in tall, grande, and venti sizes (translation: small, medium, and large). Starbuzz
                            saw this as an intrinsic part of the coffee class, so they’ve added two methods to
                                the Beverage class: setSize() and getSize(). They’d also like for the condiments to be
                              charged according to size, so for instance, Soy costs 10¢, 15¢, and 20¢, respectively, for
                                                 tall, grande, and venti coffees. The updated Beverage class is shown below.

                        How would you alter the decorator classes to handle this change in requirements?
        public abstract class Beverage {
              public enum Size { TALL, GRANDE, VENTI };
              Size size = Size.TALL;
              String description = "Unknown Beverage";
              public String getDescription() {
                     return description;
              }
              public void setSize(Size size) {
                     this.size = size;
              }
              public Size getSize() {
                     return this.size;
              }
              public abstract double cost();
       }


                                                                        you are here 4      99


---

## PDF page 138

decorators in java i/o

Real-World Decorators: Java I/O

The large number of classes in the java.io package is...overwhelming. Don’t feel alone
if you said “whoa” the first (and second and third) time you looked at this API.
But now that you know the Decorator Pattern, the I/O classes should make more
sense since the java.io package is largely based on Decorator. Here’s a typical set of
objects that use decorators to add functionality to reading data from a file:

                                                           A text file for reading.


                                              FileInputStream
        B             m          u          f    a           feredInputStre        Zi      p      I                                                                                  component                                                                                         is the       nputStream                                                                    FileInputStream     The                                                                              decorated.                                                                          being                                                                                                  several                                                                     that’s                                                                                                 supplies                                                                                  library     FileInputStream,                                                           Java I/O                                                                                          including                                                                     components,       ZipInputStream is also a                                                            a few                                                                               is           StringBufferInputStream,and        concrete                                    BufferedInputStream                 decorator.                             It                                                            a base                                                                                  us                                                                                             give                                                                   ByteArrayInputStream,       adds                                                                              these            the                                       concrete decorator.                               a                    ability                      to                         read                                                                                                    bytes.                                                                                  read                                                                       to                                                     adds                                                                        others. All of                                                                               which        zip             file                                    BufferedInputStream                 entries                        as                             it                           reads                                                                from                                                                 component       data from a zip file.            buffering behavior to a
                                        FileInputStream: it buffers
                                        input to improve performance.


100      Chapter 3


---

## PDF page 139

the decorator pattern

Decorating the java.io classes

BufferedInputStream and ZipInputStream both extend FilterInputStream, which
extends InputStream. InputStream acts as the abstract decorator class:
                                                                                  component.                                                               our abstract                                                                    Here’s
                                                                                             FilterInputStream
                                                               InputStream                                                      is an abstract
                                                                                               decorator.


          FileInputStream              StringBufferInputStream          ByteArrayInputStream                FilterInputStream


                               PushbackInputStream             BufferedInputStream              DataInputStream                 InflatorInputStream

 These InputStreams act as the concrete                                                                               ZipInputStream
 components that we will wrap with
 decorators. There are a few more we                                 And finally, here are all our concrete decorators.
 didn’t show, like ObjectInputStream.


You can see that this isn’t so different from the Starbuzz design. You should
now be in a good position to look over the java.io API docs and compose
decorators on the various input streams.
You’ll see that the output streams have the same design. And you’ve probably
already found that the Reader/Writer streams (for character-based data)
closely mirror the design of the streams classes (with a few differences and
inconsistencies, but close enough to figure out what’s going on).
Java I/O also points out one of the downsides of the Decorator Pattern:
designs using this pattern often result in a large number of small classes
that can be overwhelming to a developer trying to use the Decorator-based
API. But now that you know how Decorator works, you can keep things in
perspective and when you’re using someone else’s Decorator-heavy API, you
can work through how their classes are organized so that you can easily use
wrapping to get the behavior you’re after.


                                                                       you are here 4      101


---

## PDF page 140

write your own i/o decorator

 Writing your own Java I/O Decorator

 Okay, you know the Decorator Pattern, and you’ve seen the
 I/O class diagram. You should be ready to write your own input
 decorator.                                               No problem. I
                                                                           just have to extend the
 How about this: write a decorator that converts all uppercase              FilterInputStream class and
 characters to lowercase in the input stream. In other words, if              override the read() methods.
 we read in “I know the Decorator Pattern therefore I RULE!”
 then your decorator converts this to “i know the decorator
 pattern therefore i rule!”

                                 First, extend the FilterInputStream, the              import                             abstract decorator for all InputStreams.     forget toDon’t       (not shown).java.io...

 public class LowerCaseInputStream extends FilterInputStream {

     public LowerCaseInputStream(InputStream in) {
         super(in);
     }

     public int read() throws IOException {
         int c = in.read();
         return (c == -1 ? c : Character.toLowerCase((char)c));
     }

     public int read(byte[] b, int offset, int len) throws IOException {
         int result = in.read(b, offset, len);
         for (int i = offset; i < offset+result; i++) {            Now we need to implement two
                                                                                read methods. They take a             b[i] = (byte)Character.toLowerCase((char)b[i]);                                                                              byte (or an array of bytes)         }                                                                            and convert each byte (that
         return result;                                                           represents a character) to
     }                                                                                 lowercase if it’s an uppercase
 }                                                                                      character.
      REMEMBER: we don’t provide import and package statements
            in the code listings. Get the complete source code from
         https://wickedlysmart.com/head-first-design-patterns.

 102      Chapter 3


---

## PDF page 141

the decorator pattern

Test out your new Java I/O Decorator

Write some quick code to test the I/O decorator:
  public class InputTest {
      public static void main(String[] args) throws IOException {
          int c;                                                                                        and decorate                                                                Set up the FileInputStream                                                                                    BufferedInputStream                                                                                                it, first with a          try {                                                                 and then our brand new
              InputStream in =                                  LowerCaseInputStream filter.
                  new LowerCaseInputStream(
                      new BufferedInputStream(
                          new FileInputStream("test.txt")));

              while((c = in.read()) >= 0) {
                  System.out.print((char)c);              I know the Decorator Pattern therefore I RULE!
              }

              in.close();
          } catch (IOException e) {                                              test.txt file
              e.printStackTrace();
          }                                        Just use the stream to read                You need to      }                                         characters until the end of                make this file.
  }                                              file and print as we go.


Give it a spin:


      File Edit Window Help DecoratorsRule
  % java InputTest
  i know the decorator pattern therefore i rule!
  %


                                                                       you are here 4      103


---

## PDF page 142

decorator interview

                         Patterns Exposed
                                      This week’s interview:
                                Confessions of a Decorator


       Head First: Welcome, Decorator Pattern. We’ve heard that you’ve been a bit down on
            yourself lately?
         Decorator: Yes, I know the world sees me as the glamorous design pattern, but you know, I’ve
           got my share of problems just like everyone.
          HeadFirst: Can you perhaps share some of your troubles with us?
         Decorator: Sure. Well, you know I’ve got the power to add flexibility to designs, that much is
             for sure, but I also have a dark side. You see, I can sometimes add a lot of small classes to a design,
          and this occasionally results in a design that’s less than straightforward for others to understand.
          HeadFirst: Can you give us an example?
         Decorator: Take the Java I/O libraries. These are notoriously difficult for people to
           understand at first. But if they just saw the classes as a set of wrappers around an InputStream,
                life would be much easier.
          HeadFirst: That doesn’t sound so bad. You’re still a great pattern, and improving this is just a
           matter of public education, right?
         Decorator: There’s more, I’m afraid. I’ve got typing problems: you see, people sometimes
            take a piece of client code that relies on specific types and introduce decorators without
            thinking through everything. Now, one great thing about me is that you can usually insert decorators
              transparently and the client never has to know it’s dealing with a decorator. But like I said, some code is
          dependent on specific types and when you start introducing decorators, boom! Bad things
          happen.
          HeadFirst: Well, I think everyone understands that you have to be careful when inserting
            decorators. I don’t think this is a reason to be too down on yourself.
         Decorator: I know, I try not to be. I also have the problem that introducing decorators can
            increase the complexity of the code needed to instantiate the component. Once you’ve got
            decorators, you’ve got to not only instantiate the component, but also wrap it with who knows
        how many decorators.
          HeadFirst: I’ll be interviewing the Factory and Builder patterns next week—I hear they can
          be very helpful with this?
         Decorator: That’s true; I should talk to those guys more often.
          HeadFirst: Well, we all think you’re a great pattern for creating flexible designs and staying
            true to the Open-Closed Principle, so keep your chin up and think positively!
         Decorator: I’ll do my best, thank you.


104      Chapter 3


---

## PDF page 143

the decorator pattern


          Tools for your Design Toolbox
                                                            Inheritance is one form of
               You’ve got another chapter under your belt and a new                                                                                         extension, but not necessarily the
                 principle and pattern in the toolbox.                                                                                      best way to achieve flexibility in
                                                                                    our designs.
                                                            In our designs we should allow
                                                                                     behavior to be extended without
                                                                                       the need to modify existing code.                 Basics        OO
                               Abstraction                              Compositioncan often be usedand delegationto add new
                                                                                    behaviors at runtime.     Principles     Encapsulation OO
                        varies.      Polymorphism                           The Decorator Pattern provides            what                                                                         an alternative to subclassing for    Encapsulate                    over inheritance.Inheritance                                         extending behavior.           composition    Favor                                                           The Decorator Pattern involves          to interfaces, not     Program                                                             a set of decorator classes that
                                                                                    are used to wrap concrete      implementations.                                designs                       coupled                                                  components.           for loosely      Strive                             interact.               objects that      between                                                  Decorator classes mirror the type                       for          We now have the Open-             of the components they decorate.                    open              should be                                              Closed Principle to guide            (In fact, they are the same type       Classes                                                       to strive             but closed for                  us. We’re going                                                                             as the components they decorate,       extension                                          to design our system so             either through inheritance or        modification.                       that the closed parts              interface implementation.)                                              are isolated from our
                                                            Decorators change the behavior of                                         new extensions.
                                                                                                        their components by adding new
                                                                                                    functionality before and/or after (or   Patterns                                                                           even in place of) method calls toOO                     ofaalgorithms,one-to-many                   defines                       family          -                                                                                       the                                                                                 component.             a                              that              defines      -                          them                         objects     Observer                                  additionalso                       makes Strategy                  and                between                     Attach              -                  one,                                                                                                                                 You                                                                               can wrap                                                                                    a                                                                                       component with            each                               state,                                    algorithm                                         alldynamically.its      dependency                      changes                             object  encapsulates       Decorator                          thean                            letsto                                                                           any                                                                           number                                                                                                               of                                                                                                        decorators.               objectStrategy                              updatedit.          one                        and      when                           that              responsibilities                                  flexibleuse   interchangeable.                   a                      notifiedclients                are                from                      provide                                                                                               extending                                                                                   Decorators                                                                                               are                                                                                                                        typically       dependents                              for        independently           Decorators   vary                  to subclassing                                             transparent to the client of the         automatically             alternative                                                                           component—that is, unless              functionality.                                                                                       the client is relying on the
                                                                               component’s concrete type.
                                                                designs         Decorators can result in many                                          for creating                                      pattern                                                           Principle. Or was it            small objects in our design, and                And here’s our first                                                              we’ve                             the Open-Closed                                                  pattern                                                                                overuse can be complex.                            satisfy                   that                                           another                                     there                                          Is                                                         well?                        the first?                                              as                         really                                                  principle                                        this                                  follows                     used that
                                                                     you are here 4      105


---

## PDF page 144

exercise solutions


                                                               Write the cost() methods for the following classes
                                                             (pseudo-Java is okay). Here’s our solution:

              public class Beverage {
             // declare instance variables for milkCost,
             // soyCost, mochaCost, and whipCost, and
             // getters and setters for milk, soy, mocha
             // and whip.
              public double cost() {
                     double condimentCost = 0.0;
                     if (hasMilk()) {
                         condimentCost += milkCost;
                     }
                     if (hasSoy()) {
                         condimentCost += soyCost;
                     }
                     if (hasMocha()) {
                         condimentCost += mochaCost;
                     }
                     if (hasWhip()) {
                         condimentCost += whipCost;
                     }
                     return condimentCost;
                 }
             }

              public class DarkRoast extends Beverage {
                 public DarkRoast() {
                     description = "Most Excellent Dark Roast";
                 }
                 public double cost() {
                     return 1.99 + super.cost();
                 }
             }


106      Chapter 3


---

## PDF page 145

the decorator pattern


                                                              “double mocha soy latte with whip”

             New barista training

                     2 Whip calls cost() on Mocha.
                                      3 Mocha calls cost() on another Mocha.
                    First, we call cost() on the                    4  Next, Mocha calls cost() on Soy.
        1 outermost decorator, Whip.                          5  Last topping! Soy calls
                                                                                            cost() on HouseBlend.
                                                                                                method                                                                                                                cost()                                                            6  HouseBlend’s zz Cub                                                                                                   off                                                                                                              pops  off                                                                                              returns .89 andr
a e                                                                       the stack.                          cost()                                   cost()                                         cost()                                                cost()                                                        cost()tS e                                                                                                                                          .15                                                                                                        adds         $1.54   .10                                 .20                                                                                                            cost() method                                               .89                                        .15                           .20                                                   end       7  Soy’s                              H                                                                                                             then                                              ouseBl                                                                                                 the result,                                                                                    and returns                         Soy            M                                                                                                  pops off the stack.                        ocha           M
                                                                                                    method                      ocha                      8 The second Mocha’s cost()    W                                                                                                      the result,       hip                                          adds .20 and returns
                                                                                     then pops off the stack.
10 Finally, the result returns to Whip’s                                                    9 The first Mocha’s cost() method adds    cost(), which adds .10, giving us a                                                                  .20 and returns the result, then pops    final cost of $1.54.                                                                       off the stack.


                                                                 you are here 4      107


---

## PDF page 146

exercise solutions


                                  Our friends at Starbuzz have introduced sizes to their menu. You can now order
                                     a coffee in tall, grande, and venti sizes (translation: small, medium, and large).
                                      Starbuzz saw this as an intrinsic part of the coffee class, so they’ve added two
                                 methods to the Beverage class: setSize() and getSize(). They’d also like for the
                                   condiments to be charged according to size, so for instance, Soy costs 10¢, 15¢,
                                 and 20¢, respectively, for tall, grande, and venti coffees.

                           How would you alter the decorator classes to handle this change in
                                     requirements? Here’s our solution.

       public abstract class CondimentDecorator extends Beverage {
           public Beverage beverage;
           public abstract String getDescription();                               getSize(), for                                                                             method,                                                    We added a                                                                                                 returns                                                                           that simply                                                                            decorators           public Size getSize() {                          the                                                                                            beverage.                                                                                size of the                                                              the               return beverage.getSize();
          }
      }

       public class Soy extends CondimentDecorator {
           public Soy(Beverage beverage) {
               this.beverage = beverage;
          }

           public String getDescription() {
               return beverage.getDescription() + ", Soy";
          }
                                                                          Here we get the size (which           public double cost() {                                                                              propagates all the way to the               double cost = beverage.cost();                                                                             concrete beverage) and then
              if (beverage.getSize() == Size.TALL) {         add the appropriate cost.
                  cost += .10;
              } else if (beverage.getSize() == Size.GRANDE) {
                  cost += .15;
              } else if (beverage.getSize() == Size.VENTI) {
                  cost += .20;
              }
               return cost;
          }
      }


108      Chapter 3
