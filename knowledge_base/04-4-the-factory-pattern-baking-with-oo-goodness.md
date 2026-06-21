# 4: the Factory Pattern: Baking with OO Goodness

_Extracted from PDF pages 147-206. Text only; images and diagrams are not embedded._


---

## PDF page 147

4 the Factory Pattern
BakingwithOOGoodness


Get ready to bake some loosely coupled OO designs. There is more
 to making objects than just using the new operator. You’ll learn that instantiation is an
 activity that shouldn’t always be done in public and can often lead to coupling problems.
And we don’t want that, do we? Find out how Factory Patterns can help save you from
 embarrassing dependencies.


                                                                          this is a new chapter      109


---

## PDF page 148

thinking about new


           Okay, it’s been three chapters and you
                still haven’t answered my question about
           new. We aren’t supposed to program to an
            implementation, but every time I use new,
             that’s exactly what I’m doing, right?


                   When you see “new,” think “concrete.”

                                    Yes, when you use the new operator you are certainly instantiating
                              a concrete class, so that’s definitely an implementation and not an
                                      interface. And you make a good observation: that tying your code to
                              a concrete class can make it more fragile and less flexible.

                                 Duck duck = new MallardDuck();

                            We                                   want                                                                                    create an                                                                       to                                        to use                                                           we have                                                   abstact types    But                                                                                                                 class!                                to                                      keep                                                                                  concrete                                         code                                                               of a                                                           flexible.                                                                             instance

                       When we have a whole set of related concrete classes, often we end up
                                   writing code like this:
                                 Duck duck;
                                 if (picnic) {                                                                                                      different                                     duck = new MallardDuck();    We have a bunch of                                 } else if (hunting) {              duck classes, and we don’t                                     duck = new DecoyDuck();       know until runtime which one                                                                                                          instantiate.                                 } else if (inBathTub) {           we need to
                                     duck = new RubberDuck();
                                 }
                            Here we’ve got several concrete classes being instantiated, and the
                                   decision of which to instantiate is made at runtime depending on
                           some set of conditions.
                       When you see code like this, you know that when it comes time for
                               changes or extensions, you’ll have to reopen this code and examine
                             what needs to be added (or deleted). Often this kind of code ends
                           up in several parts of the application, making maintenance and
                                updates more difficult and error-prone.

110      Chapter 4


---

## PDF page 149

the factory pattern


                         But you have to create an
                         object at some point, and Java
                          only gives us one way to create an
                          object, right? So what gives?


What’s wrong with “new”?

Technically there’s nothing wrong with the new operator.
After all, it’s a fundamental part of most modern objectoriented languages. The real culprit is our old friend
CHANGE and how change impacts our use of new.
By coding to an interface, you know you can insulate yourself
from many of the changes that might happen to a system
down the road. Why? If your code is written to an interface,
then it will work with any new classes implementing that
 interface through polymorphism. However, when you have
code that makes use of lots of concrete classes, you’re looking         Remember that                                                                                         designs for trouble because that code may have to be changed as new           should be “open forconcrete classes are added. So, in other words, your code will           extension but                                                                                   closed                                                           fornot be “closed for modification.” To extend your code with                                                                            modification.” Seenew concrete types, you’ll have to reopen it.                       Chapter 3 for a                                                                                          review.
So what can you do? It’s times like these that you can fall back
on OO design principles to look for clues. Remember, our first
 principle deals with change and guides us to identify the aspects
 that vary and separate them from what stays the same.


How might you take all the parts of your application that instantiate
concrete classes and separate or encapsulate them from the rest of
your application?


                                                        you are here 4      111


---

## PDF page 150

identify what varies

Identifying the aspects that vary

Let’s say you have a pizza shop, and as a cutting-edge pizza store owner in
Objectville you might end up writing some code like this:

         Pizza orderPizza() {
                Pizza pizza = new Pizza();

                pizza.prepare();                                                          For flexibility, we really want this                                                          to be an abstract class or interface,                pizza.bake();                                                          but unfortunately we can’t directly                pizza.cut();                                instantiate either of those.                pizza.box();
                return pizza;
         }

But you need more than one type of pizza...
So then you’d add some code that determines the appropriate type of pizza and
then goes about making the pizza:
         Pizza orderPizza(String type) {                 We’re now passing in                                                            the type of pizza to                Pizza pizza;                                                                   orderPizza.
                if (type.equals("cheese")) {
                    pizza = new CheesePizza();
                } else if (type.equals("greek") {
                    pizza = new GreekPizza();                                                                 Based on the type of pizza, we
                                                                              instantiate the correct concrete class                } else if (type.equals("pepperoni") {                                                               and assign it to the pizza instance
                    pizza = new PepperoniPizza();            variable. Note that each pizza here has                }                                             to implement the Pizza interface.
                pizza.prepare();               Once we have a Pizza, we prepare it
                pizza.bake();                     (you know, roll the dough, put on the
                                                                  sauce, and add the toppings), then we                pizza.cut();                                                       bake it, cut it, and box it!                pizza.box();
                                                  Each Pizza subtype (CheesePizza,                return pizza;                                                        GreekPizza, etc.) knows how to prepare         }                                                                       itself.


112      Chapter 4


---

## PDF page 151

the factory pattern

But the pressure is on to add more pizza types

You realize that all of your competitors have added a couple of trendy pizzas to their
menus: the Clam Pizza and the Veggie Pizza. Obviously you need to keep up with the
competition, so you’ll add these items to your menu. And you haven’t been selling many
Greek pizzas lately, so you decide to take that off the menu:


                     Pizza orderPizza(String type) {
    codeis                  Pizza pizza;This      for      closed           Ifthe NOT  modification.changes       Store    we        if (type.equals("cheese")) {  Pizza            offerings,     pizza      code   its         this      toopen                   pizza = new CheesePizza();   have       it.       modify               } else if (type.equals("greek") {   and                                                                                     This is what varies.
                                pizza = new GreekPizza();                 As the pizza                                                                                                   changes                                                                                                       selection                           } else if (type.equals("pepperoni") {            over time, you’ll have                                                                                                           this code                                                                                     modify                                pizza = new PepperoniPizza();              to                                                                                         over and over.                           } else if (type.equals("clam") {
                                pizza = new ClamPizza();
                           } else if (type.equals("veggie") {
                                pizza = new VeggiePizza();
                           }
                                                                         This is what we expect to                           pizza.prepare();                                                                           stay the same. For the most
                           pizza.bake();                         part, preparing, cooking, and
                                                                              packaging a pizza has remained                           pizza.cut();                                                                    the same for years and years.
                           pizza.box();                           So, we don’t expect this code
                                                                     to change, just the pizzas it                           return pizza;                                                                             operates on.
                    }


Clearly, dealing with which concrete class is instantiated is really messing up our
orderPizza() method and preventing it from being closed for modification. But now that we
know what is varying and what isn’t, it’s probably time to encapsulate it.


                                                                       you are here 4      113


---

## PDF page 152

encapsulate object creation

Encapsulating object creation

So now we know we’d be better off moving the object
creation out of the orderPizza() method. But how? Well, what            if (type.equals("cheese")) {
we’re going to do is take the creation code and move it out                    pizza = new CheesePizza();
into another object that is only going to be concerned with                 } else if (type.equals("pepperoni") {
creating pizzas.                                                              pizza = new PepperoniPizza();
                                                                          } else if (type.equals("clam") {
                                                                             pizza = new ClamPizza();
                                                                          } else if (type.equals("veggie") {
                                                                             pizza = new VeggiePizza();
                                                                        }
  Pizza orderPizza(String type) {
         Pizza pizza;                                               First we pull the object                                                 creation code out of the
                                              orderPizza() method.

                                                                                             that         pizza.prepare();                                                                                                  object                                                                                                       in an                                                                                code                                                                          that                                                                                    place                                                           we                                                         Then                                                                                                     create                                                                                       to                                                                               how                                                                                    about                                                                            worry                                                                       to         pizza.bake();                                                                                 going                                                                             only                                                                                         is                                                                             a pizza                                                                                             needs                                                                                         object                                                                              other                                                                          any                                                                         If                                                                             pizzas.                                                                                                               to.                                                                                     come                                                                                   to                                                                                         object                                                                           the                                                                                                         is         pizza.cut();         What’s                                                                                    this                                                                        created,                                            going to go         pizza.box();                          here?
         return pizza;
  }

We’ve got a name for this new object: we
call it a Factory.
                          y
                         r
                          to                     SiFactories        handle the details                             of object creation.                                  Once                                      we have                             ac                      mplePizzaFa SimplePizzaFactory,                    our orderPizza()                               method                                       becomes                                                 a
client of that object. Anytime it needs a pizza, it asks the pizza
factory to make one. Gone are the days when the orderPizza()
method needs to know about Greek versus Clam pizzas. Now
the orderPizza() method just cares that it gets a pizza that
implements the Pizza interface so that it can call prepare(),
bake(), cut(), and box().
We’ve still got a few details to fill in here; for instance, what does
the orderPizza() method replace its creation code with? Let’s
implement a simple factory for the pizza store and find out...

114      Chapter 4


---

## PDF page 153

the factory pattern

Building a simple pizza factory

We’ll start with the factory itself. What we’re going to do is define a class that
encapsulates the object creation for all pizzas. Here it is...
                                                It                      the SimplePizzaFactory.                        class,             new           our      Here’s                                                      a                                                                           define                                pizzas for its clients.                        creating                   in life:                                                                                         in                                                                    First we             job     has one                                                                      method                                                                      createPizza()                                                                           This is the                                                          the factory.      will use          public class SimplePizzaFactory {                             all clients                                                           method                                                                   new objects.                                                        to instantiate              public Pizza createPizza(String type) {
                  Pizza pizza = null;
                  if (type.equals("cheese")) {
                      pizza = new CheesePizza();                  } else if (type.equals("pepperoni")) {          Here’s the code we                                                                                 plucked out of the                      pizza = new PepperoniPizza();                          method.                                                                              orderPizza()                  } else if (type.equals("clam")) {
                      pizza = new ClamPizza();
                  } else if (type.equals("veggie")) {
                      pizza = new VeggiePizza();
                  }
                  return pizza;
              }                                                            This code is still parameterized by the type of the          }                                                                   pizza, just like our original orderPizza() method was.


                                                                And, don’t forget, we’re also just about to remove the concrete      What’s the advantage of this? It looks like we’re justQ:                                                                        instantiations from our client code.pushing the problem off to another object.

                                                                                      I’ve seen a similar design where a factory like this is     One thing to remember is that the SimplePizzaFactory may   Q:A:                                                            defined as a static method. What’s the difference?have many clients. We’ve only seen the orderPizza() method;
 however, there may be a PizzaShopMenu class that uses the factory
 to get pizzas for their current description and price. We might also             Defining a simple factory as a static method is a common                          A:
have a HomeDelivery class that handles pizzas in a different way        technique and is often called a static factory. Why use a static
 than our PizzaShop class but is also a client of the factory.            method? Because you don’t need to instantiate an object to make
                                                              use of the create method. But it also has the disadvantage that you
So, by encapsulating the pizza creating in one class, we now have       can’t subclass and change the behavior of the create method.
only one place to make modifications when the implementation
changes.

                                                                       you are here 4      115


---

## PDF page 154

simple factory

Reworking the PizzaStore class

Now it’s time to fix up our client code. What we want to do is rely on the
factory to create the pizzas for us. Here are the changes:
                                                   First we give PizzaStore a
                                                 reference to a SimplePizzaFactory.
      public class PizzaStore {
          SimplePizzaFactory factory;
                                                                       PizzaStore gets the factory passed          public PizzaStore(SimplePizzaFactory factory) {                                                                   to it in the constructor.
              this.factory = factory;
          }

          public Pizza orderPizza(String type) {
              Pizza pizza;
              pizza = factory.createPizza(type);             And the orderPizza() method uses the
                                                                           factory to create its pizzas by simply
              pizza.prepare();                                            passing on the type of the order.
              pizza.bake();
              pizza.cut();                                           Notice that we’ve replaced the new              pizza.box();                                             operator with a createPizza method
                                                      in the factory object. No more
              return pizza;           concrete instantiations here!
          }

          // other methods here
     }


    We know that object composition allows us to change behavior dynamically at runtime (among
       other things) because we can swap in and out implementations. How might we be able to use
       that in the PizzaStore? What factory implementations might we be able to swap in and out?


                                                                                                                        too). Haven, New forget not
                                         (let’s factories pizza style California and Chicago, York, New thinking we’re but you, about know don’t We


116      Chapter 4


---

## PDF page 155

the factory pattern

The Simple Factory defined
                                                                                                                                                                            HeadFirst    Pattern
The Simple Factory isn’t actually a Design Pattern; it’s more of a programming idiom.                        HonorableMention   HonorableBut it is commonly used, so we’ll give it a Head First Pattern Honorable Mention.
Some developers do mistake this idiom for the Factory Pattern, but the next time that             Mention
 happens you can subtly show you know your stuff; just don’t strut as you educate them
on the distinction.
 Just because Simple Factory isn’t a REAL pattern doesn’t mean we shouldn’t check out
how it’s put together. Let’s take a look at the class diagram of our new Pizza Store:

                                             This is the factory where we create
                                                    pizzas; it should be the only part        This is the product of                                        of our application that refers to        the factory: pizza!
                                              concrete Pizza classes.
                                                                                            We’ve defined Pizza                    PizzaStore                         SimplePizzaFactory                                Pizza               as an abstract class
                orderPizza()                                     createPizza()                                       prepare()                    with some helpful                                                                                               that                                                                                                                 bake()                        implementations
                                                                                                                                     cut()                      can be overridden.
                                                                                                                     box()                                                                 is            client of the        The create method This is the                                                            statically.         PizzaStore              often declared factory.          through the now goes                 to get  SimplePizzaFactory                                       CheesePizza                                            PepperoniPizza        of pizza.   instances
     These are our concrete products. Each                         VeggiePizza                  ClamPizza      product needs to implement the Pizza      interface* (which in this case means     “extend the abstract Pizza class”) and     be concrete. As long as that’s the case,      it can be created by the factory and     handed back to the client.


Think of Simple Factory as a warm-up. Next, we’ll explore two heavy-duty patterns
 that are both factories. But don’t worry, there’s more pizza to come!
*Just another reminder: in design patterns, the phrase “implement an interface” does NOT always mean
“write a class that implements a Java interface, by using the ‘implements' keyword in the class declaration.”
 In the general use of the phrase, a concrete class implementing a method from a supertype (which could be a
 abstract class OR interface) is still considered to be “implementing the interface” of that supertype.

                                                                       you are here 4      117


---

## PDF page 156

pizza franchise

Franchising the pizza store

Your Objectville Pizza Store has done so well that you’ve trounced
the competition and now everyone wants a Pizza Store in their
own neighborhood. As the franchiser, you want to ensure the
quality of the franchise operations and so you want them to use
your time-tested code.                                                         Yes, different areas of the US serve
But what about regional differences? Each franchise might want to          very different styles of pizza—from
offer different styles of pizzas (New York, Chicago, and California,         the deep-dish pizzas of Chicago, to the
to name a few), depending on where the franchise store is located           thin crust of New York, to the crackerand the tastes of the local pizza connoisseurs.                                      like pizza of California (some would say
                                                                      topped with fruits and nuts).


You want all the franchise pizza stores                                          One franchise wants ato leverage your PizzaStore code, so the                                              factory that makes NY-stylepizzas are prepared in the same way.                                                        pizzas: thin crust, tasty sauce,
                                                                            and just a little cheese.
                N   y                   YPizzaFactor

       PizzaStore                                                  Another franchise                                                                                    wants a factory that
                                                                                     makes Chicago-style
                                                        ory         pizzas; their customers                C                                                                                                             thick                                                                                                 with                                                                                                  pizzas                      t           like                 hi
                                                                                               and                     cagoPizzaFac                                                                                                                    sauce,                                                                                                          rich                                                                                                      crust,
                                                                                            tons of cheese.

We’ve seen one approach...

If we take out SimplePizzaFactory and create three different
factories—NYPizzaFactory, ChicagoPizzaFactory, and
CaliforniaPizzaFactory—then we can just compose the PizzaStore
with the appropriate factory and a franchise is good to go. That’s
one approach.
Let’s see what that would look like...


118      Chapter 4


---

## PDF page 157

the factory pattern

                                                                    Here we create a factory for
                                                                       making NY-style pizzas.
NYPizzaFactory nyFactory = new NYPizzaFactory();
PizzaStore nyStore = new PizzaStore(nyFactory);            Then we create a PizzaStore and pass
nyStore.orderPizza("Veggie");                                            it a reference to the NY factory.
                                                                                         ...and when we make pizzas, we
                                                                    get NY-style pizzas.

ChicagoPizzaFactory chicagoFactory = new ChicagoPizzaFactory();
PizzaStore chicagoStore = new PizzaStore(chicagoFactory);
chicagoStore.orderPizza("Veggie");

                                                    Likewise for the Chicago pizza stores: we
                                                   create a factory for Chicago pizzas and
                                                   create a store that is composed with a
                                                  Chicago factory. When we make pizzas, we
                                                get the Chicago-style ones.

But you’d like a little more quality control...
                                                                             I’ve been making pizzaSo you test-marketed the SimpleFactory idea, and what you                                                                 for years so I thought I’d addfound was that the franchises were using your factory to                                                  my own “improvements” to thecreate pizzas, but starting to employ their own home-grown                                                                 PizzaStore procedures...procedures for the rest of the process: they’d bake things
a little differently, they’d forget to cut the pizza, and they’d
use third-party boxes.
Rethinking the problem a bit, you see that what you’d really
like to do is create a framework that ties the store and the
pizza creation together, yet still allows things to remain
flexible.
In our early code, before the SimplePizzaFactory, we had
the pizza-making code tied to the PizzaStore, but it wasn’t
flexible. So, how can we have our pizza and eat it too?

                                  Not what you want in a good                                                 franchise. You do NOT want to                                       know what he puts on his pizzas.


                                                                       you are here 4      119


---

## PDF page 158

let the subclasses decide

A framework for the pizza store

There is a way to localize all the pizza-making activities to the PizzaStore
class, and to give the franchises freedom to have their own regional style.
What we’re going to do is put the createPizza() method back into PizzaStore,
but this time as an abstract method, and then create a PizzaStore subclass
for each regional style.
First, let’s look at the changes to the PizzaStore:
                PizzaStore is now abstract (see why below).

       public abstract class PizzaStore {


              public Pizza orderPizza(String type) {
                     Pizza pizza;                                                       Now createPizza is back to being a
                                                                                            call to a method in the PizzaStore
                     pizza = createPizza(type);             rather than on a factory object.

                     pizza.prepare();
                     pizza.bake();
                     pizza.cut();                                                                                 All this looks just the same...                     pizza.box();

                     return pizza;
              }
                                                        Now we’ve moved our factory                                                                            object to this method.              abstract Pizza createPizza(String type);
       }
                               Our “factory method” is now                                    abstract in PizzaStore.

Now we’ve got a store waiting for subclasses; we’re going to have a
subclass for each regional type (NYPizzaStore, ChicagoPizzaStore,
CaliforniaPizzaStore) and each subclass is going to make the decision about
what makes up a pizza. Let’s take a look at how this is going to work.

120      Chapter 4


---

## PDF page 159

the factory pattern

Allowing the subclasses to decide

Remember, the Pizza Store already has a well-honed order system in the orderPizza()
method and you want to ensure that it’s consistent across all franchises.
What varies among the regional Pizza Stores is the style of pizzas they make—New York
pizza has thin crust, Chicago pizza has thick, and so on—and we are going to push all
these variations into the createPizza() method and make it responsible for creating the
right kind of pizza. The way we do this is by letting each subclass of Pizza Store define
what the createPizza() method looks like. So, we’ll have a number of concrete subclasses
of Pizza Store, each with its own pizza variations, all fitting within the Pizza Store
framework and still making use of the well-tuned orderPizza() method.
                                                                 Each subclass provides an implementation
                                                               of the createPizza() method, overriding
                                                                          PizzaStore              the abstract createPizza() method in
                                                                                    createPizza()                  Pizza Store, while all subclasses make use                                                                                    orderPizza()                 of the orderPizza() method defined
                                                                                           in Pizza Store. We could make the
                                                                          orderPizza() method final if we really
                                                                   wanted to enforce this.

                                                   NYStylePizzaStore                      ChicagoStylePizzaStore     Similarly, by using the
                                                            createPizza()                                       createPizza()            Chicago subclass, we get an  If a franchise wants NY-style  pizzas for its customers, it                                                          implementation of createPizza()
   uses the NY subclass, which has                                              is                with Chicago ingredients.                                                     createPizza()                      method,          Remember:     own createPizza()   its                                                                  so                                                             Store,                                                           in Pizza          NY-style pizzas.               abstract   creating                                         MUST                                                          subtypes                                                        all pizza store
                                          implement the method.


                                                                    public Pizza createPizza(type) {
      public Pizza createPizza(type) {                                   if (type.equals("cheese")) {
         if (type.equals("cheese")) {                                       pizza = new ChicagoStyleCheesePizza();
             pizza = new NYStyleCheesePizza();                          } else if (type.equals("pepperoni") {
         } else if (type.equals("pepperoni") {                              pizza = new ChicagoStylePepperoniPizza();
             pizza = new NYStylePepperoniPizza();                       } else if (type.equals("clam") {
         } else if (type.equals("clam") {                                   pizza = new ChicagoStyleClamPizza();
             pizza = new NYStyleClamPizza();                            } else if (type.equals("veggie") {
         } else if (type.equals("veggie") {                                 pizza = new ChicagoStyleVeggiePizza();
             pizza = new NYStyleVeggiePizza();                          }
         }                                                         }
     }

                                                                       you are here 4      121


---

## PDF page 160

how do subclasses decide?


                 I don’t get it. The PizzaStore
                  subclasses are just subclasses. How
                  are they deciding anything? I don’t
                 see any logical decision-making code in
                   NYStylePizzaStore....


                              Well, think about it from the point of view of the PizzaStore’s orderPizza() method: it is
                             defined in the abstract PizzaStore, but concrete types are only created in the subclasses.
                                                                   PizzaStore                                    is defined in the abstract                                                                    orderPizza()                                                                        not the subclasses. So, the                                                                           createPizza()                                                                     PizzaStore,                                                                                                                                   is actually                                                                                                           subclass                                                                                     which                                                                                     idea                                                                           has no                                                                           orderPizza()                                                            method                                                                                     the pizzas.                                                                                       making                                                                          and                                                                          code                                                                          running the

                        Now, to take this a little further, the orderPizza() method does a lot of things with a
                            Pizza object (like prepare, bake, cut, box), but because Pizza is abstract, orderPizza() has
                       no idea what real concrete classes are involved. In other words, it’s decoupled!


                                                          PizzaStore                                   pizza = createPizza();
                                                                                                                            pizza.prepare();                                                               createPizza()
                                                                                                                           pizza.bake();                                                               orderPizza()
                                                                                                                                     pizza.cut();
                                                                                                                              pizza.box();
                                                                        to actually get a                                                                                calls createPizza()                                                   orderPizza()                                                                                                  it get?                                                                                pizza will                                                                of                                                                           kind                                                   pizza object. But which                                                                                               it doesn’t                                                                                       decide;                                                                              can’t                                                           method                                        The orderPizza()                                             know how. So who does decide?

                    When orderPizza() calls createPizza(), one of your subclasses will be called into action to
                              create a pizza. Which kind of pizza will be made? Well, that’s decided by the choice of
                             pizza store you order from, NYStylePizzaStore or ChicagoStylePizzaStore.


                                                               NYStylePizzaStore                   ChicagoStylePizzaStore
                                                                            createPizza()                                    createPizza()


                             So, is there a real-time decision that subclasses make? No, but from the perspective of
                               orderPizza(), if you chose a NYStylePizzaStore, that subclass gets to determine which
                             pizza is made. So the subclasses aren’t really “deciding”—it was you who decided by
                           choosing which store you wanted—but they do determine which kind of pizza gets made.

122      Chapter 4


---

## PDF page 161

the factory pattern

Let’s make a Pizza Store

Being a franchise has its benefits. You get all the PizzaStore
functionality for free. All the regional stores need to do is subclass
PizzaStore and supply a createPizza() method that implements
their style of pizza. We’ll take care of the big three pizza styles for
the franchisees.
Here’s the New York regional style:

                returns a Pizza, and   createPizza()                                                              The                                                                         NYPizzaStore                             for                                                                                             extends                        responsible                  is fully        subclass  the                                                                              PizzaStore,                                                                                            so                                                                                                       it inherits                                                                                            the                         it instantiates.                Pizza        concrete   which                                                                             orderPizza()                                                                              method                                                                                            (among                                                                                                                  others).


         public class NYPizzaStore extends PizzaStore {
            Pizza createPizza(String item) {                   We’ve got to implement
                                                                             createPizza(), since it is                if (item.equals("cheese")) {                                                                          abstract in PizzaStore.                    return new NYStyleCheesePizza();
                } else if (item.equals("veggie")) {
                    return new NYStyleVeggiePizza();
                } else if (item.equals("clam")) {                                                                                    Here’s where we create our
                    return new NYStyleClamPizza();            concrete classes. For each type of
                } else if (item.equals("pepperoni")) {       Pizza we create the NY style.
                    return new NYStylePepperoniPizza();
                } else return null;
            }
        }                 * Note that the orderPizza() method in the
                                      superclass has no clue which Pizza we are creating;
                                       it just knows it can prepare, bake, cut, and box it!


Once we’ve got our PizzaStore subclasses built, it will be time
to see about ordering up a pizza or two. But before we do that,
why don’t you take a crack at building the Chicago-style and
California-style pizza stores on the next page?

                                                                       you are here 4      123


---

## PDF page 162

factory method


              We’ve knocked out the NYPizzaStore; just two more to go and we’ll be ready to franchise! Write
              the Chicago-style and California-style PizzaStore implementations here:


124      Chapter 4


---

## PDF page 163

the factory pattern

Declaring a factory method

With just a couple of transformations to the PizzaStore class, we’ve gone from
having an object handle the instantiation of our concrete classes to a set of
subclasses that are now taking on that responsibility. Let’s take a closer look:
                                                      The subclasses of                                                                                 handle object public abstract class PizzaStore {                           PizzaStore                                                                          for us in the                                                                               instantiation                                                                               method.                                                                        createPizza()
    public Pizza orderPizza(String type) {
        Pizza pizza;                                                                    NYStylePizzaStore
        pizza = createPizza(type);                                                    createPizza()
        pizza.prepare();                                                                                ChicagoStylePizzaStore
        pizza.bake();                                                                                                          createPizza()
        pizza.cut();
        pizza.box();
        return pizza;
    }
                                                                                       All the responsibility for
    protected abstract Pizza createPizza(String type);          instantiating Pizzas has
                                                                          been moved into a method    // other methods here                                                                     that acts as a factory.}


        Code Up Close

       A               factory                 method                            handles                                      object                                             creation                                           and                                                        encapsulates                                                                                                          it in                                                                 a                                                                                  method may             subclass.                   This                         decouples                                    the                                              client                                        code in                                                     the                                                            superclass from                                                                       the                                                A factory                                                                                                  (or             object creation code in the subclass.                                   be parameterized                                                                                 not) to select among                                                                                                          variations of a                                                                                                 several
                                                                                         product.              abstract Product factoryMethod(String type)
     A          factory                                                                                                           client (the                                                                                 the               method          is                      A factory method returns      A factory method isolates          abstract                                                                                            orderPizza())                  so the                                                                                                           like                                                                                             superclass,                                                                  the                                       that                                                                                in                                 Product                             a                                                                    is typically         code         subclasses                are                                                                        of concrete                   counted                                                                    what kind                                        methods                                                                        knowing      on                                        within                                 used                                                        from         to handle                   object                                                                                        created.                                                                                                is actually                                                         superclass.                                        the                                                  in                                defined                                                               Product        creation.


                                                                       you are here 4      125


---

## PDF page 164

ordering a pizza

Let’s see how it works: ordering pizzas with
the pizza factory method


               I like NY-style pizza...you                    I like Chicago-style deep dish
               know, thin, crispy crust with                        pizza with thick crust and
                 a little cheese and really                              tons of cheese.
                      good sauce.


                                                                          Joel                                  Ethan


          Ethan needs to order
             his pizza from a NY                                                  Joel needs to order his
           pizza store.                                                         pizza from a Chicago
                                                                               pizza store. Same pizza
                                                                                  ordering method, but
                                                                                 different kind of pizza!

So how do they order?

        1    First, Joel and Ethan need an instance of a PizzaStore. Joel needs to instantiate a
              ChicagoPizzaStore and Ethan needs a NYPizzaStore.
        2   With a PizzaStore in hand, both Ethan and Joel call the orderPizza() method and pass
                in the type of pizza they want (cheese, veggie, and so on).
        3  To create the pizzas, the createPizza() method is called, which is defined in the
             two subclasses NYPizzaStore and ChicagoPizzaStore. As we defined them, the
              NYPizzaStore instantiates a NY-style pizza, and the ChicagoPizzaStore instantiates a
               Chicago-style pizza. In either case, the Pizza is returned to the orderPizza() method.
        4  The orderPizza() method has no idea what kind of pizza was created, but it knows it is
              a pizza and it prepares, bakes, cuts, and boxes it for Ethan and Joel.


126      Chapter 4


---

## PDF page 165

the factory pattern

Let’s check out how these pizzas are
                                               Behindreally made to order...
                                                      the Scenes


           Let’s follow Ethan’s order: first we need a NYPizzaStore:   1

            PizzaStore nyPizzaStore = new NYPizzaStore();
                                                             Creates a instance of                                                           NYPizzaStore.

       Now that we have a store, we can take an order:        e                               or   2                            nyPizzaSt
           nyPizzaStore.orderPizza("cheese");
                                                             method is called on                                          The orderPizza()                                                                            instance (the method                                                the nyPizzaStore                                                                PizzaStore runs).                                                    defined inside
   3   Themethod:orderPizza() method then calls the createPizza()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         createPizza("cheese")
           Pizza pizza  = createPizza("cheese");
                                            Remember, createPizza(), the factory
                                              method, is implemented in the subclass. In this
                                                  case it returns a NY-style cheese Pizza.
                                                               Pizza
   4     Finally,orderPizza()we havemethodthe unpreparedfinishes preparingpizza init:hand and the

           pizza.prepare();
           pizza.bake();                                                         All of these methods are           pizza.cut();                      defined in the specific pizza           pizza.box();                      returned from the factory                                             method createPizza(), defined                                                the NYPizzaStore.   The orderPizza() method gets                       in    back a Pizza, without knowing    exactly what concrete class it is.

                                                                       you are here 4      127


---

## PDF page 166

the pizza classes

We’re just missing one thing: Pizzas!
Our Pizza Store isn’t going to be very popular
without some pizzas, so let’s implement them
                           an abstract                           with                       start                                         concrete                       We’ll                          and all the                                class,                                                this.                  Pizza                              from                                will derive                     pizzas
                                                    Each Pizza has a name, a type of dough, public abstract class Pizza {                                                  a type of sauce, and a set of toppings.    String name;
    String dough;
    String sauce;
    List<String> toppings = new ArrayList<String>();
    void prepare() {
        System.out.println("Preparing " + name);
        System.out.println("Tossing dough...");
        System.out.println("Adding sauce...");                                                                             Preparation follows a        System.out.println("Adding toppings: ");                                                                      number of steps in a        for (String topping : toppings) {                                                                                  particular sequence.            System.out.println("   " + topping);
        }
    }                                                                The abstract class provides
                                                                           some basic defaults for    void bake() {                                                                                           baking, cutting, and boxing.        System.out.println("Bake for 25 minutes at 350");
    }
    void cut() {
        System.out.println("Cutting the pizza into diagonal slices");
    }
    void box() {
        System.out.println("Place pizza in official PizzaStore box");
    }
                                  REMEMBER: we don’t provide import and package statements in the    public String getName() {                                              code listings. Get the complete source code from the wickedlysmart        return name;                                                  website at https://wickedlysmart.com/head-first-design-patterns    }
}
                                                    If you lose this URL, you can always quickly find it in the Intro section.

128      Chapter 4


---

## PDF page 167

the factory pattern


Now we just need some concrete subclasses...how about defining
New York and Chicago-style cheese pizzas?

                                                             The NY Pizza has its own       public class NYStyleCheesePizza extends Pizza {                                                                               marinara-style sauce and thin crust.
           public NYStyleCheesePizza() {
               name = "NY Style Sauce and Cheese Pizza";
               dough = "Thin Crust Dough";
               sauce = "Marinara Sauce";

               toppings.add("Grated Reggiano Cheese");
           }                                                            And one topping, Reggiano cheese!
       }


                                                                  The Chicago Pizza uses plum       public class ChicagoStyleCheesePizza extends Pizza {                                                                                tomatoes as a sauce along
                                                                                with extra-thick crust.
           public ChicagoStyleCheesePizza() {
               name = "Chicago Style Deep Dish Cheese Pizza";
               dough = "Extra Thick Crust Dough";
               sauce = "Plum Tomato Sauce";
                                                                    The Chicago-style deep               toppings.add("Shredded Mozzarella Cheese");                                                                                             dish pizza has lots of           }                                                                        mozzarella cheese!
           void cut() {
               System.out.println("Cutting the pizza into square slices");
           }
       }
               The Chicago-style pizza also overrides the cut()
                method so that the pieces are cut into squares.

                                                                       you are here 4      129


---

## PDF page 168

make some pizzas

You’ve waited long enough. Time for some pizzas!
                                                           we create two                                                                           First                                                                                                 stores. public class PizzaTestDrive {                                        different

    public static void main(String[] args) {
        PizzaStore nyStore = new NYPizzaStore();                      We use one store to
        PizzaStore chicagoStore = new ChicagoPizzaStore();              make Ethan’s order...

        Pizza pizza = nyStore.orderPizza("cheese");
        System.out.println("Ethan ordered a " + pizza.getName() + "\n");

        pizza = chicagoStore.orderPizza("cheese");
        System.out.println("Joel ordered a " + pizza.getName() + "\n");
    }
}                                                                                            ...and the other for Joel’s.


          File Edit  Window Help YouWantMootzOnThatPizza?
    %java PizzaTestDrive
    Preparing NY Style Sauce and Cheese Pizza
    Tossing dough...
    Adding sauce...
    Adding toppings:
       Grated Reggiano cheese                                                              Both pizzas get prepared,    Bake for 25 minutes at 350                                                                   the toppings get added, and    Cutting the pizza into diagonal slices    Place pizza in official PizzaStore box                   the pizzas are baked, cut,    Ethan ordered a NY Style Sauce and Cheese Pizza        and boxed. Our superclass                                                                            never had to know the
    Preparing Chicago Style Deep Dish Cheese Pizza             details; the subclass handled                                                                                                     instantiating    Tossing dough...                                                                  all that just by
    Adding sauce...                                              the right pizza.    Adding toppings:
       Shredded Mozzarella Cheese
    Bake for 25 minutes at 350
    Cutting the pizza into square slices
    Place pizza in official PizzaStore box
    Joel ordered a Chicago Style Deep Dish Cheese Pizza


130      Chapter 4


---

## PDF page 169

the factory pattern

It’s finally time to meet the Factory Method Pattern

All factory patterns encapsulate object creation. The Factory Method Pattern encapsulates object
 creation by letting subclasses decide what objects to create. Let’s check out these class diagrams to see
who the players are in this pattern:

The Creator classes

       This is our abstract                                        Often the creator contains code       creator class. It defines                                       that depends on an abstract product,                                                                                   The      an abstract factory                               PizzaStore                  which is produced by a subclass.      method that the                                                   creator never really knows which                                                                            createPizza()        subclasses                implement to                                                                           orderPizza()                       concrete product was produced.      produce products.

                                                                                        Since each franchise gets its
                                                                        own subclass of PizzaStore,
                                       NYPizzaStore                                     ChicagoPizzaStore         it’s free to create its own
                                             createPizza()                                                      createPizza()               style of pizza by implementing   The                                                                                        createPizza().    isourcreatePizza()         factory    method                                         that produce    produces     method.It              Classes            products.                                             are called                                        products                                                      creators.                                        concrete

The Product classes
                                                                             Factories produce products,
                                                                 and in the PizzaStore, our
                                                                          Pizza                  product is a Pizza.

These are the concrete
products — all the pizzas that
are produced by our stores.       NYStyleCheesePizza                    ChicagoStyleCheesePizza
                                              NYStylePepperoniPizza                   ChicagoStylePepperoniPizza
                                                    NYStyleClamPizza                      ChicagoStyleClamPizza
                                                         NYStyleVeggiePizza                     ChicagoStyleVeggiePizza


                                                                       you are here 4      131


---

## PDF page 170

creators and products

View Creators and Products in Parallel

For every concrete Creator, there’s typically a whole set of products that
it creates. Chicago pizza creators create different types of Chicago-style
pizza, New York pizza creators create different types of New York–style
pizza, and so on. In fact, we can view our sets of Creator classes and their
corresponding Product classes as parallel hierarchies.
Let’s look at the two parallel class hierarchies and see how they relate:


                                                 Notice how these
                                                             class hierarchies are
                                                               parallel: both have
                                                 abstract classes that
                                                  are extended by
         The Product classes        concrete classes, which  The Creator classes
                                             know about specific
                                                   implementations for
                                NY and Chicago pizza.                   PizzaStore                                      Pizza

                                                                                                                                           createPizza()
                                                                                                                                           orderPizza()


     NYStyleCheesePizza                    ChicagoStyleCheesePizza                             NYPizzaStore                  ChicagoPizzaStore
         NYStylePepperoniPizza                   ChicagoStylePepperoniPizza                      createPizza()                              createPizza()
                NYStyleClamPizza                      ChicagoStyleClamPizza
                    NYStyleVeggiePizza                     ChicagoStyleVeggiePizza
                                                                   the                                                             to                                                 the                                              to                                                                                        ChicagoPizzaStoreall                                                       NYPizzaStoreall                                                how                                                    The                                                                 howpizzas.                                    The                          about                                                        aboutpizzas.   encapsulates                                                               encapsulates                                                                                 knowledgeChicago-style                                                         knowledgeNY-style                                                               make                                             make

                                                                                                 this knowledge.                                                                                         encapsulating                                                                                is the key to                                                    method                                      The factory


132      Chapter 4


---

## PDF page 171

the factory pattern
        Design Puzzle


We need another kind of pizza for those crazy Californians (crazy in a good way,
of course). Draw another parallel set of classes that you’d need to add a new
California region to our PizzaStore.


                                                                  PizzaStore

                                                                          createPizza()
                                                                          orderPizza()
                                                                                                    here...                                                                        drawing                                                             Your


                                NYPizzaStore                ChicagoPizzaStore
                                   createPizza()                          createPizza()


    NYStyleCheesePizza                    ChicagoStyleCheesePizza
       NYStylePepperoniPizza                   ChicagoStylePepperoniPizza
              NYStyleClamPizza                      ChicagoStyleClamPizza
                  NYStyleVeggiePizza                     ChicagoStyleVeggiePizza


Okay, now write the five most bizarre things you can think of to put on a pizza.
Then, you’ll be ready to go into business making pizza in California!


                                                                       you are here 4      133


---

## PDF page 172

factory method defined

 Factory Method Pattern defined

  It’s time to roll out the official definition of the Factory Method Pattern:


            The Factory Method Pattern defines an interface
                    for creating an object, but lets subclasses decide which
                     class to instantiate. Factory Method lets a class defer
                   instantiation to subclasses.

 As with every factory, the Factory Method Pattern gives us a way to encapsulate the
  instantiations of concrete types. Looking at the class diagram below, you can see that the
 abstract Creator class gives you an interface with a method for creating objects, also known
 as the “factory              method.”                   Any other                               methods                                       implemented                                                              in the                                                                   abstract                                                                   Creator                                                                                are                  what written         to operate               on products                           produced                                    by the                                                 factory method.                                                   Only                                                                         subclasses                                                                                    actually                                                                          them                                                                             ask    we implement the factory method and create products.                                      could    but                                                                 You                                                                                          means,                                                                                               understand                                                                                      do! As in the official definition, you’ll often hear developers say, “the Factory Method pattern                                                                                        “decides”                                                                    now                                                                                    they                                                                        you  lets subclasses decide which class to instantiate.” Because the Creator class is written without  bet      than                                                                                 better knowledge of the actual products that will be created, we say “decide” not because the       this
 pattern allows subclasses themselves to decide, but rather, because the decision actually comes
 down to which subclass is used to create the product.
                                                                                                     contains                                                                      Creator is a class that                                                                                                                         all of the                                                                                    for                                                                 the implementations   products,                                                                      to manipulate                                                                    methods             method.                                                                                        factory                                                                          for the                                                                       except

                                                   Product                                Creator
                                                                     The abstract factoryMethod()                                                                                             factoryMethod()                                                                                           anOperation()                         is what all Creator subclasses          must implementAll products                 so that the                                                     must implement.         interfacethe same                   products            use the      that classes                   interface, can refer to the         concrete class. not the
                                                                              ConcreteCreator
                                               ConcreteProduct                      ConcreteCreator         implements the
                                                                                             factoryMethod()                                                                                factoryMethod(), which is
                                                                            the method that actually
                                                                                    produces products.
                                   ConcreteCreator is responsible for creating
                                    one or more concrete products. It is the
                                         only class that has the knowledge of how
                                   to create these products.

 134      Chapter 4


---

## PDF page 173

the factory pattern


      What’s the advantage of the Factory Method         We implemented what is known as theQ:                    A: Pattern when you only have one ConcreteCreator?        parameterized factory method. It can make more than one
                                                               object based on a parameter passed in, as you noticed.
     The Factory Method Pattern is useful if you’ve only      Often, however, a factory just produces one object and isA:got one concrete creator because you are decoupling the      not parameterized. Both are valid forms of the pattern.
 implementation of the product from its use. If you add
additional products or change a product’s implementation,         Your parameterized types don’t seem “type-                      Q:
 it will not affect your Creator (because the Creator is not       safe.” I’m just passing in a String! What if I asked for a
 tightly coupled to any ConcreteProduct).                  “CalmPizza”?

     Would it be correct to say that our NY and              You are certainly correct, and that would cause whatQ:                    A:Chicago stores are implemented using Simple          we call in the business a “runtime error.” There are several
Factory? They look just like it.                              other more sophisticated techniques that can be used to
                                              make parameters more “type safe”—in other words, to
      They’re similar, but used in different ways. Even        ensure errors in parameters can be caught at compile time.A:though the implementation of each concrete store looks       For instance, you can create objects that represent the
a lot like the SimplePizzaFactory, remember that the         parameter types, use static constants, or use enums.
concrete stores are extending a class that has defined
createPizza() as an abstract method. It is up to each                I’m still a bit confused about the difference                      Q:
store to define the behavior of the createPizza() method.     between Simple Factory and Factory Method. They
 In Simple Factory, the factory is another object that is         look very similar, except that in Factory Method, the
composed with the PizzaStore.                            class that returns the pizza is a subclass. Can you
                                                        explain?
      Are the factory method and the Creator classQ:
always abstract?                                                You’re right that the subclasses do look a lot like                      A:                                                       Simple Factory; however, think of Simple Factory as a
     No, you can define a default factory method to          one-shot deal, while with Factory Method you are creatingA:produce some concrete product. Then you always           a framework that lets the subclasses decide which
have a means of creating products even if there are no       implementation will be used. For example, the orderPizza()
subclasses of the Creator class.                         method in the Factory Method Pattern provides a general
                                                      framework for creating pizzas that relies on a factory
                                                   method to actually create the concrete classes that go     Each store can make four different kinds ofQ:                                                               into making a pizza. By subclassing the PizzaStore class,pizzas based on the type passed in. Do all concrete                                                     you decide what concrete products go into making thecreators make multiple products, or do they                                                            pizza that orderPizza() returns. Compare that with Simplesometimes just make one?                                                                Factory, which gives you a way to encapsulate object
                                                                  creation, but doesn’t give you the flexibility of Factory
                                                   Method because there is no way to vary the products
                                                              you’re creating.


                                                                you are here 4      135


---

## PDF page 174

master and student


                      Guru and Student...
                         Guru: Tell me about your training.
                         Student: Guru, I have taken my study of “encapsulate what
                           varies” further.
                     Guru: Go on...
                      Student: I have learned that one can encapsulate the code
                           that creates objects. When you have code that instantiates
                        concrete classes, this is an area of frequent change. I’ve learned
                    a technique called “factories” that allows you to encapsulate this
                        behavior of instantiation.
                     Guru: And these “factories,” of what benefit are they?
                      Student: There are many. By placing all my creation code in one
                          object or method, I avoid duplication in my code and provide one
                        place to perform maintenance. That also means clients depend
                         only upon interfaces rather than the concrete classes required to
                            instantiate objects. As I have learned in my studies, this allows me
                           to program to an interface, not an implementation, and that makes
                 my code more flexible and extensible in the future.
                     Guru: Yes, your OO instincts are growing. Do you have any
                        questions for your guru today?
                      Student: Guru, I know that by encapsulating object creation I am
                       coding to abstractions and decoupling my client code from actual
                        implementations. But my factory code must still use concrete
                        classes to instantiate real objects. Am I not pulling the wool over
                 my own eyes?
                     Guru: Object creation is a reality of life; we must create objects or
                  we will never create a single Java application. But, with knowledge
                           of this reality, we can design our code so that we have corralled
                             this creation code like the sheep whose wool you would pull
                       over your eyes. Once corralled, we can protect and care for the
                          creation code. If we let our creation code run wild, then we will
                       never collect its “wool.”
                      Student: Guru, I see the truth in this.
                     Guru: As I knew you would. Now, please go and meditate on
                          object dependencies.


136      Chapter 4


---

## PDF page 175

the factory pattern


                                Let’s pretend you’ve never heard of an OO factory. Here’s a “very dependent”
                            version of PizzaStore that doesn’t use a factory. We need you to make a count
                             of the number of concrete pizza classes this class is dependent on. If you
                       added California-style pizzas to this PizzaStore, how many classes would it be
                       dependent on then?

public class DependentPizzaStore {
    public Pizza createPizza(String style, String type) {
        Pizza pizza = null;
        if (style.equals("NY")) {
            if (type.equals("cheese")) {
                pizza = new NYStyleCheesePizza();            } else if (type.equals("veggie")) {                Handles all the
                pizza = new NYStyleVeggiePizza();            NY-style pizzas
            } else if (type.equals("clam")) {
                pizza = new NYStyleClamPizza();
            } else if (type.equals("pepperoni")) {
                pizza = new NYStylePepperoniPizza();
            }
        } else if (style.equals("Chicago")) {
            if (type.equals("cheese")) {                pizza = new ChicagoStyleCheesePizza();          Handles all the            } else if (type.equals("veggie")) {                   Chicago-style pizzas
                pizza = new ChicagoStyleVeggiePizza();
            } else if (type.equals("clam")) {
                pizza = new ChicagoStyleClamPizza();
            } else if (type.equals("pepperoni")) {
                pizza = new ChicagoStylePepperoniPizza();
            }
        } else {
            System.out.println("Error: invalid type of pizza");
            return null;
        }
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }
}
        You can write your                                                    number with
         answers here:                       number                                   California, too


                                                               you are here 4      137


---

## PDF page 176

object dependencies

Looking at object dependencies

When you directly instantiate an object, you are depending on its
concrete class. Take a look at our very dependent PizzaStore one
page back. It creates all the pizza objects right in the PizzaStore class
instead of delegating to a factory.
If we draw a diagram representing that version of the PizzaStore
and all the objects it depends on, here’s what it looks like:


                                       This version of the
                                     PizzaStore depends on all
                                       those pizza objects, because
                                                     it’s creating them directly.
          If the                                                  Because any change to the concrete                  implementation                        of                                 these                                                                                             the            classes                                                                                              affects                                                                         of pizzas                                                                       implementations                  changes,                      then we                          may          have            to                                                                                            PizzaStore                                                                                that the                                                                     PizzaStore, we say                modify in                           PizzaStore.                                                                    “depends on” the pizza implementations.

                e
              PizzaStor

                  C             Pizza
                                  hi                         ie                    c                                    zza        N                    ag        Y                    ePi                      oStyleVegg            s         StyleChee                                       Ch            izzaP                                           ic   i                        a  n                a        g                         o  o
                               zz           N                  i            Y                        StylePepper
                C                                                                zza                           ieP            StyleVegg                               hi                     Pi                  c      N                      za                   m       Y                   ag       S                    oStyleCla        tyl   iPiz         ePeppeonr           N  a   C               ePizza                z       hi            Y                        s                     c                            Piz                      ag            StyleClam                        oStyleChee     Every new kind of pizza
     we add creates another
      dependency for PizzaStore.


138      Chapter 4


---

## PDF page 177

the factory pattern

The Dependency Inversion Principle

It should be pretty clear that reducing dependencies to
concrete classes in our code is a “good thing.” In fact, we’ve
got an OO design principle that formalizes this notion; it even                                                                  you can                                                                  phrasehas a big, formal name: Dependency Inversion Principle.       Yet another                                                          the execs in                                                                  impress                                                       use to                                                                             raise willHere’s the general principle:                                                           Your                                                the room!      the cost                                                               offset                                                      than                                                 more                                                         and you’ll                                                                 book,                                           of this                                                         of                                                                   admiration                                                           gain the                                                                              developers.              Design Principle                     your fellow
               Depend upon abstractions. Do
                  not depend upon concrete classes.


At first, this principle sounds a lot like “Program to an
interface, not an implementation,” right? It is similar;
however, the Dependency Inversion Principle makes an even
stronger statement about abstraction. It suggests that our         A “high-level” component is a class
high-level components should not depend on our low-level           with behavior defined in terms of
components; rather, they should both depend on abstractions.          other, “low-level” components.
But what the heck does that mean?                               For example, PizzaStore is a
Well, let’s start by looking again at the pizza store diagram              high-level component because
on the previous page. PizzaStore is our “high-level                        its behavior is defined in terms
component” and the pizza implementations are our “low-           of pizzas — it creates all the
level components,” and clearly PizzaStore is dependent on            different pizza objects, and
the concrete pizza classes.                                               prepares, bakes, cuts, and boxes
                                                                  them, while the pizzas it uses are
Now, this principle tells us we should instead write our code             low-level components.so that we are depending on abstractions, not concrete
classes. That goes for both our high-level modules and our
low-level modules.
But how do we do this? Let’s think about how we’d apply this
principle to our very dependent PizzaStore implementation...


                                                            you are here 4      139


---

## PDF page 178

dependency inversion principle


         Applying the Principle

              Now, the main problem with the very dependent PizzaStore is that it depends
              on every type of pizza because it actually instantiates concrete types in its
                  orderPizza() method.
               While we’ve created an abstraction, Pizza, we’re nevertheless creating concrete
                  Pizzas in this code, so we don’t get a lot of leverage out of this abstraction.
           How can we get those instantiations out of the orderPizza() method? Well, as we
                know, the Factory Method Pattern allows us to do just that.
                 So, after we’ve applied the Factory Method Pattern, our diagram looks like this:

                                                             now depends only                                                            PizzaStore                        PizzaStore      on Pizza, the abstract class.
                     Pizza is an abstract                              class...an                                                                                  pizza classes depend on                                  abstraction.                      The concrete                                                                                                 too, because                                                                                     abstraction                                                               the Pizza                                                                                                    interface                                                                            the Pizza                                                                 they implement                                                                                                  “interface”                               Pizza                              we’re using                                                                       (remember,                                                                                in the general sense) in the Pizza
                                                                       abstract class.


                N                                                               zza      N
                               zza                     sePi                 YStyleChee                            YStyleClamPi

                   N                    Y                                                                            zza N                                                          zzia                        Pi
                                                    ieP                        oni                         YStyleVegg                                                                                                Pizza                                                                                                                                              izza                    StylePepper                                                  Ch
                                  niP                                                        icago                  eggie              ChicagoStyleV                               StylePeppero
                                                                        zza C                                                                                                                                                                                ePizza
                            s                       Pi
                            ee                       am                   ChicagoStyleCl                                             hicagoStyleCh


                 After applying Factory Method, you’ll notice that our high-level component, the
                  PizzaStore, and our low-level components, the pizzas, both depend on Pizza, the
                  abstraction. Factory Method is not the only technique for adhering to the Dependency
                 Inversion Principle, but it is one of the more powerful ones.


140      Chapter 4


---

## PDF page 179

the factory pattern


     Okay, I get
the dependency part,
but why is it called
dependency inversion?


                  Where’s the “inversion” in Dependency
                    Inversion Principle?

                    The “inversion” in the name Dependency Inversion
                            Principle is there because it inverts the way you typically
                        might think about your OO design. Look at the diagram
                      on the previous page. Notice that the low-level components
                    now depend on a higher-level abstraction. Likewise, the
                             high-level component is also tied to the same abstraction.
                          So, the top-to-bottom dependency chart we drew a couple
                             of pages back has inverted itself, with both high-level and
                            low-level modules now depending on the abstraction.
                             Let’s also walk through the thinking behind the typical
                          design process and see how introducing the principle can
                             invert the way we think about the design...


                                                                  you are here 4      141


---

## PDF page 180

invert your thinking

Inverting your thinking...
                                                           Okay, so you need to implement a Pizza Store.
                                                           What’s the first thought that pops into your head?
                 Hmmm, Pizza Stores
                      prepare, bake, and box pizzas.
                    So, my store needs to be able to
                make a bunch of different pizzas:
                   CheesePizza, VeggiePizza, ClamPizza,
                            and so on...
                                                                 Right, you start at the top and follow things
                                                 down to the concrete classes. But, as you’ve seen,
                                                         you don’t want your pizza store to know about
                                                                 the concrete pizza types, because then it’ll be
                                                          dependent on all those concrete classes!
                                                      Now, let’s “invert” your thinking...instead of
                                                                         starting at the top, start at the Pizzas and think
                                                            about what you can abstract.
                        Well, a CheesePizza and a
                       VeggiePizza and a ClamPizza are
                                all just Pizzas, so they should
                      share a Pizza interface.


                                                                Right! You are thinking about the abstraction Pizza.
                                                    So now, go back and think about the design of the
                                                               Pizza Store again.


                      Since I now have a Pizza
                      abstraction, I can design my
                     Pizza Store and not worry about
                  the concrete pizza classes.


                                                                   Close. But to do that you’ll have to rely on a
                                                                     factory to get those concrete classes out of
                                                            your Pizza Store. Once you’ve done that, your
                                                                         different concrete pizza types depend only on an
                                                                      abstraction, and so does your store. We’ve taken
                                                          a design where the store depended on concrete
                                                                           classes and inverted those dependencies (along
                                                               with your thinking).

142      Chapter 4


---

## PDF page 181

the factory pattern

A few guidelines to help you follow
the Principle...

The     following guidelines                     can                           help you avoid OO designs that violate                                                                            athe Dependency                 Inversion                            Principle:                                                                   If you use new, you’ll be holding                                                                                                                       class. Use                                                                      to a concrete                                                                          reference                                                      a factory to get around that!    No variable should hold a reference to a concrete class.
                                                                 If you derive from a concrete class, you’re                                                                  depending on a concrete class. Derive from an    No class should derive from a concrete class.                 abstraction, like an interface or an abstract class.
                                                                     If you override an                                                                                          implemented                                                                   then                                                                                                 method,                                                                           your                                                                                  base                                                                                                      class                                                                                              wasn’t                                                                                                                    really                                                                                          an    No         method                  should override an implemented method of any                                                                             abstraction                                                                         to                                                                                    start                                                                                                  with.                                                                                        Those        of its            base classes.                                                                                               methods                                                                        implemented                                                                                             in                                                                             the                                                                                          base                                                                                                                class                                                                                               are                                                               be                                                                                          meant                                                                                               to                                                                           shared                                                                     by                                                                                                             all                                                                                    your                                                                                                               subclasses.

                                      But wait, aren’t these
                                              guidelines impossible to
                                            follow? If I follow these,
                                                                  I’ll never be able to write
                                        a single program!


You’re exactly right! Like many of our principles, this is a guideline
you should strive for, rather than a rule you should follow all the time.
Clearly, every single Java program ever written violates these guidelines!
But, if you internalize these guidelines and have them in the back of
your mind when you design, you’ll know when you are violating the
principle and you’ll have a good reason for doing so. For instance, if you
have a class that isn’t likely to change, and you know it, then it’s not the
end of the world if you instantiate a concrete class in your code. Think
about it; we instantiate String objects all the time without thinking twice.
Does that violate the principle? Yes. Is that okay? Yes. Why? Because
String is very unlikely to change.
If, on the other hand, a class you write is likely to change, you have some
good techniques like Factory Method to encapsulate that change.


                                                                       you are here 4      143


---

## PDF page 182

families of ingredients
                                                             Dough                    PepperoniMeanwhile, back at the Pizza Store...

 The design for the Pizza Store is really shaping up: it’s got a
 flexible framework and it does a good job of adhering to design
 principles.
 Now, the key to Objectville Pizza’s success has always been fresh,
 quality ingredients, and what you’ve discovered is that with the
 new framework your franchises have been following your procedures,
 but a few franchises have been substituting inferior ingredients in
 their pizzas to lower costs and increase their margins. You know
 you’ve got to do something, because in the long term this is going
 to hurt the Objectville brand!
                                                                                                             Veggies                                                                 baking,         Sauce                                                                      is, the                                      That                                                  the                              Cheese                                         the cutting,                                              and so on...                                                     boxing,
Ensuring consistency in your ingredients
So how are you going to ensure each franchise is using quality ingredients?
You’re going to build a factory that produces them and ships them to your
franchises!
Now there’s only one problem with this plan: the franchises are located in
different regions and what is red sauce in New York is not red sauce in Chicago.
So, you have one set of ingredients that needs to be shipped to New York and a
different set that needs to be shipped to Chicago. Let’s take a closer look:


                                                    We’ve got the
                                               same product            Chicago                           New York                                                          families (dough,
                                                          sauce, cheese,        PizzaMenu              veggies, meats)      PizzaMenu      Cheese Pizza                                                                                   Cheese Pizza        Plum Tomato Sauce, Mozzarella, Parmesan,            but different
         Oregano                                                    implementations            Marinara Sauce, Reggiano, Garlic
                                                                                               Pizza              Pizza       Veggie                                                 based on region.         VeggieMarinara                       Sauce, Mozzarella, Parmesan,                                                                                                              Sauce, Reggiano, Mushrooms,        Plum Tomato
          Eggplant, Spinach, Black Olives                                                                Onions, Red Peppers
      Clam Pizza                                                            Clam Pizza
         Plum Tomato Sauce, Mozzarella, Parmesan, Clams                                        Marinara Sauce, Reggiano, Fresh Clams
       Pepperoni Pizza                                                               Pepperoni Pizza
         Plum Tomato Sauce, Mozzarella, Parmesan,                                             Marinara Sauce, Reggiano, Mushrooms,
          Eggplant, Spinach, Black Olives, Pepperoni                                                     Onions, Red Peppers, Pepperoni


144      Chapter 4


---

## PDF page 183

the factory pattern

Families of ingredients...

New York uses one set of ingredients andChicago another. Given the popularity of             Chicago
Objectville Pizza, it won’t be long before
you also need to ship another set of regional                                            FrozenClams
ingredients to California, and what’s next?
Austin?
                                                                           PlumTomatoSauce                        ThickCrustDough
For this to work, you’re going to have to figure
out how to handle families of ingredients.

                                                                                                        MozzarellaCheese


      New York                                                                     are made from the same                                                                 Pizzas                                                                                      different                                                         All Objectville’s                                                                each region has a                                                        but                           FreshClams                                                       components,                                                                              components.                                                     of those                                                        implementation

              MarinaraSauce                ThinCrustDough
                                             California                            ReggianoCheese
                                                                                            FreshClams


                                                                            BruschettaSauce                        VeryThinCrustDough

       Each family consists of a type of dough,                                    GoatCheese
       a type of sauce, a type of cheese, and a
        seafood topping (along with a few more we
         haven’t shown, like veggies and spices).
                                                                                                                          families, with                                                                                                 ingredient                                                                             of ingredients.                                                           In total, these three regions make upfamily                                                            a complete                                                                      implementing                                                     each region

                                                                       you are here 4      145


---

## PDF page 184

ingredient factories

Building the ingredient factories

Now we’re going to build a factory to create our ingredients; the
factory will be responsible for creating each ingredient in the
ingredient family. In other words, the factory will need to create
dough, sauce, cheese, and so on... You’ll see how we are going to
handle the regional differences shortly.
Let’s start by defining an interface for the factory that is going to
create all our ingredients:


      public interface PizzaIngredientFactory {
          public Dough createDough();                              we define a                                                                                 ingredient                                                                                                interface.          public Sauce createSauce();                   For each                                                                                   in our                                                               method                                                                  create          public Cheese createCheese();
          public Veggies[] createVeggies();
          public Pepperoni createPepperoni();
          public Clams createClam();

     }
             Lots of new classes here,
               one per ingredient.


With that interface, here’s what we’re going to do:

      1     Build a factory for each region. To do this, you’ll create a subclass of
              PizzaIngredientFactory that implements each create method.

      2    Implement a set of ingredient classes to be used with the factory, like
             ReggianoCheese, RedPeppers, and ThickCrustDough. These classes can be
              shared among regions where appropriate.
      3    Then we still need to hook all this up by working our new ingredient
                factories into our old PizzaStore code.


146      Chapter 4


---

## PDF page 185

the factory pattern

Building the New York ingredient factory

Okay, here’s the implementation for the New York ingredient factory. This
factory specializes in Marinara Sauce, Reggiano Cheese, Fresh Clams, etc.                                                              The NY ingredient factory
                                                                                implements the interface for all
                                                                                     ingredient factories.

public class NYPizzaIngredientFactory implements PizzaIngredientFactory {

    public Dough createDough() {
        return new ThinCrustDough();
    }                                                                    the                                                                                 in                                                                         ingredient                                                  For each                                                                             create                                                          we                                                                              family,    public Sauce createSauce() {                     ingredient                                                                                      version.                                                   the New York        return new MarinaraSauce();
    }

    public Cheese createCheese() {
        return new ReggianoCheese();
    }

    public Veggies[] createVeggies() {
        Veggies veggies[] = { new Garlic(), new Onion(), new Mushroom(), new RedPepper() };
        return veggies;                                                                       For veggies, we return an array of    }                                                                                          Veggies. Here we’ve hardcoded the
                                                                                              veggies. We could make this more
    public Pepperoni createPepperoni() {                               sophisticated, but that doesn’t really
                                                                  add anything to learning the factory        return new SlicedPepperoni();                                                                                pattern, so we’ll keep it simple.    }

    public Clams createClam() {
        return new FreshClams();                 The best sliced pepperoni.
    }                                                       This is shared between New
                                                          York and Chicago. Make sure}                                                             you use it on the next page
            New York is on the coast; it                   when you get to implement
               gets fresh clams. Chicago has                   the Chicago factory yourself.
              to settle for frozen.

                                                                       you are here 4      147


---

## PDF page 186

build a factory


                                         Write the ChicagoPizzaIngredientFactory. You can reference
                                        the classes below in your implementation:


                                                                                        EggPlant
                                                Spinach
                                                                                                                    ThickCrustDough
                            BlackOlives                        SlicedPepperoni
                                                                                       PlumTomatoSauce

                                      FrozenClams
                                                                           MozzarellaCheese


148      Chapter 4


---

## PDF page 187

the factory pattern

Reworking the pizzas...

We’ve got our factories all fired up and ready to produce quality ingredients; now we
just need to rework our Pizzas so they only use factory-produced ingredients. We’ll
start with our abstract Pizza class:

    public abstract class Pizza {
        String name;                                            Each pizza holds a set of ingredients
                                              that are used in its preparation.
        Dough dough;
        Sauce sauce;
        Veggies veggies[];
        Cheese cheese;
        Pepperoni pepperoni;                       We’ve now made the prepare method abstract.
        Clams clam;                                 This is where we are going to collect the
                                                               ingredients needed for the pizza, which of
        abstract void prepare();                  course will come from the ingredient factory.
        void bake() {
            System.out.println("Bake for 25 minutes at 350");
        }
        void cut() {
            System.out.println("Cutting the pizza into diagonal slices");
        }
        void box() {
            System.out.println("Place pizza in official PizzaStore box");
        }
        void setName(String name) {                                                                                        same, with                                                                        the                                                                           remain            this.name = name;                                                Our other methods                                                                                method.                                                                              prepare                                                         of the        }                                                   the exception
        String getName() {
            return name;
        }
        public String toString() {
            // code to print pizza here
        }
    }


                                                                       you are here 4      149


---

## PDF page 188

decoupling ingredients

Reworking the pizzas, continued...

Now that you’ve got an abstract Pizza class to work from, it’s time to
create the New York– and Chicago-style Pizzas—only this time around,
they’ll get their ingredients straight from the factory. The franchisees’ days
of skimping on ingredients are over!
When we wrote the Factory Method code, we had a NYCheesePizza and
a ChicagoCheesePizza class. If you look at the two classes, the only thing
that differs is the use of regional ingredients. The pizzas are made just
the same (dough + sauce + cheese). The same goes for the other pizzas:
Veggie, Clam, and so on. They all follow the same preparation steps; they
just have different ingredients.
So, what you’ll see is that we really don’t need two classes for each pizza;
the ingredient factory is going to handle the regional differences for us.
Here’s the CheesePizza:
                                                                         To make a pizza now, we   public class CheesePizza extends Pizza {                                                                                 need a factory to provide       PizzaIngredientFactory ingredientFactory;                                                                             the ingredients. So each                                                                                 Pizza class gets a factory                                                                                                              constructor,       public CheesePizza(PizzaIngredientFactory ingredientFactory) {   passed into its                                                                            and it’s stored in an           this.ingredientFactory = ingredientFactory;                                                                                                instance variable.       }

       void prepare() {
           System.out.println("Preparing " + name);                                                                                 Here’s where the magic happens!           dough = ingredientFactory.createDough();
           sauce = ingredientFactory.createSauce();
           cheese = ingredientFactory.createCheese();
       }
   }                                  The prepare() method steps through creating
                                    a cheese pizza, and each time it needs an                                                ingredient, it asks the factory to produce it.


150      Chapter 4


---

## PDF page 189

the factory pattern


        Code Up Close

         The Pizza code uses the factory it has been composed with to produce the ingredients used in the
             pizza. The ingredients produced depend on which factory we’re using. The Pizza class doesn’t care;
                   it knows how to make pizzas. Now, it’s decoupled from the differences in regional ingredients and can
           be easily reused when there are factories for the Austin, the Nashville, and beyond.

              sauce = ingredientFactory.createSauce();
        We’re              setting                                                                                                        sauce                  the                                                                                     the                                                                                          returns                                                        factory.                                              ingredient                                                                      method                                       our                                                     is                                This       Pizza                                                                       createSauce()               instance                                                  The                                                                          a NY                                                                                                                         is                                                                                                  this                                                       care                                                                                    If                                                  doesn’t                                                    class                                                                                              region.                                  Pizza                          The                                                                                     in its         variable                                                                                         is used                                                                                                                     sauce.             to refer                                                          that                    to                                                                                             marinara                                                                                  get                                                              long                                                        as                                                      used,                                                                  is                                                                            then we                                      factory      the                                 which                                                                              factory,             specific                                                                      ingredient                   sauce       used in this pizza.         as it’s an ingredient factory.


Let’s check out the ClamPizza as well:
                                                                       ClamPizza also stashes
    public class ClamPizza extends Pizza {                       an ingredient factory.
        PizzaIngredientFactory ingredientFactory;

        public ClamPizza(PizzaIngredientFactory ingredientFactory) {
            this.ingredientFactory = ingredientFactory;
        }

        void prepare() {
            System.out.println("Preparing " + name);
            dough = ingredientFactory.createDough();                                                                    To make a clam pizza, the prepare()            sauce = ingredientFactory.createSauce();                                                                   method collects the right            cheese = ingredientFactory.createCheese();                                                                                    ingredients from its local factory.
            clam = ingredientFactory.createClam();
        }
   }
                             If it’s a New York factory,
                          the clams will be fresh; if it’s
                               Chicago, they’ll be frozen.

                                                                       you are here 4      151


---

## PDF page 190

use the right ingredient factory

Revisiting our pizza stores

We’re almost there; we just need to make a quick trip to our franchise stores to make
sure they are using the correct Pizzas. We also need to give them a reference to their
local ingredient factories:
                                                                                                   is composed with                                                                             Store        factory.public class NYPizzaStore extends PizzaStore {               The NY                                                                                              ingredient                                                                              pizza                                             NY                                                 a                                                                                           produce the                                                                         to                                                                                  used                                                                    be                                                                                                 will    protected Pizza createPizza(String item) {                                                                       This                                                                                     NY-style                                                                            for all        Pizza pizza = null;                                                 ingredients
        PizzaIngredientFactory ingredientFactory =                  pizzas.
            new NYPizzaIngredientFactory();
                                                                 We now pass each pizza the        if (item.equals("cheese")) {                                                                                 factory that should be used to
                                                                                 produce its ingredients.            pizza = new CheesePizza(ingredientFactory);
            pizza.setName("New York Style Cheese Pizza");
        } else if (item.equals("veggie")) {                        Look back one page and make
                                                                                         sure you understand how the
            pizza = new VeggiePizza(ingredientFactory);              pizza and the factory work
            pizza.setName("New York Style Veggie Pizza");            together!
        } else if (item.equals("clam")) {
            pizza = new ClamPizza(ingredientFactory);
            pizza.setName("New York Style Clam Pizza");
                                                                          For each type of Pizza, we
        } else if (item.equals("pepperoni")) {                                                                                         instantiate a new Pizza and
                                                                                              give it the factory it needs to                                                                           get its ingredients.            pizza = new PepperoniPizza(ingredientFactory);
            pizza.setName("New York Style Pepperoni Pizza");
        }
        return pizza;
    }
}

                                               Compare this version of the createPizza()
                                                  method to the one in the Factory Method
                                                         implementation earlier in the chapter.


152      Chapter 4


---

## PDF page 191

the factory pattern

What have we done?

That was quite a series of code changes;
what exactly did we do?
                                           An Abstract Factory provides an interface for
We provided a means of creating a family                                                    a family of products. What’s a family? In our
of ingredients for pizzas by introducing                  case, it’s all the things we need to make a pizza:
a new type of factory called an Abstract               dough, sauce, cheese, meats, and veggies.
Factory.
An Abstract Factory gives us an interface
for creating a family of products. By                                                     thewriting code that uses this interface, we                                                   Defines
decouple our code from the actual factory                                                        interface.
that creates the products. That allows us
to implement a variety of factories that
produce products meant for different
contexts—such as different regions,                                    ObjectvilleAbstract IngredientFactory
different operating systems, or different
look and feels.
Because our code is decoupled from the
actual products, we can substitute different
factories to get different behaviors
(like getting marinara instead of plum
tomatoes).

                                                 New York                        Chicago
                                       implementations                             Provides                                     From the abstract factory, we                         for products.                                         derive one or more concrete
                                                                                             factories that produce the same
                                                                                     products, but with different
                                                                                 implementations.
                                                                             made with                                                                                 Pizza                                                                                                produced                                                                                                   ingredients                                                                                                          factory.                                                                      by concrete
                   PizzaStore

                               We then write our code so that it uses the
                                                factory to create products. By passing in
                                           a variety of factories, we get a variety of
                                          implementations of those products. But our
                                                    client code stays the same.


                                                                       you are here 4      153


---

## PDF page 192

order some more pizza

More pizza for Ethan and Joel...
                                                                 BehindEthan and Joel can’t get enough Objectville Pizza! What
                                                                          the Scenesthey don’t know is that now their orders are making use of
the new ingredient factories. So now when they order...


                                                                                         I’m stickin’ with
                                            I’m still lovin’ NY style.                        Chicago.


The first part of the order process hasn’t changed at all.
Let’s follow Ethan’s order again:


 1   First we need a NYPizzaStore:

      PizzaStore nyPizzaStore = new NYPizzaStore();
                                                       Creates an instance
                                              of NYPizzaStore.
                              e
                                nyPizzaStor    Now that we have a store, we can take an order: 2
      nyPizzaStore.orderPizza("cheese");
                                                       method is called                                     The orderPizza()                                          on the nyPizzaStore instance.
                                                                                createPizza("cheese")    The orderPizza() method first calls the 3
      createPizza() method:
      Pizza pizza  = createPizza("cheese");                            (See on the next page.)


154      Chapter 4


---

## PDF page 193

the factory pattern

From here things change, because we
are using an ingredient factory                                                                 Behind
                                                                          the Scenes
 4  When the createPizza() method is called, that’s    when our ingredient factory gets involved:
                                                                     factory is chosen and                                            The ingredient              and then                                                                            in the PizzaStore                                                             instantiated            of each pizza.                                                                          constructor                                                          passed into the

       Pizza pizza = new CheesePizza(nyIngredientFactory);         holds
                                         Creates a instance              y
                                   r                                  of Pizza that is               o
                                        composed                                                           act                                                with                                    F                                                  the           nyIngredient                               New                                          York                                                       ingredient                                           factory.
                                                 Pizza

 5  Next we need to prepare the pizza. Once the     prepare() method is called, the factory is asked to
     prepare ingredients:                                                                                                                                                                                                prepare()                                                          crust                                               Thin
          void prepare() {
              dough = factory.createDough();                                                          Marinara
              sauce = factory.createSauce();
              cheese = factory.createCheese();
                                                              Reggiano         }
    For Ethan’s pizza the New York     ingredient factory is used, and so                      ingredients.    we get the NY


 6   Finally, we have the prepared pizza in hand and the
      orderPizza() method bakes, cuts, and boxes the pizza.


                                                                       you are here 4      155


---

## PDF page 194

abstract factory defined

Abstract Factory Pattern defined

We’re adding yet another factory pattern to our pattern family, one that lets us create families
of products. Let’s check out the official definition for this pattern:

              The Abstract Factory Pattern provides an interface
                       for creating families of related or dependent objects
                   without specifying their concrete classes.


We’ve certainly seen that Abstract Factory allows a client to use an abstract interface to
create a set of related products without knowing (or caring) about the concrete products that
are actually produced. In this way, the client is decoupled from any of the specifics of the
concrete products. Let’s look at the class diagram to see how this all holds together:
                                                                The Client is written against the
                                                                                abstract factory and then composed
                                                                         at runtime with an actual factory.
   The Abstract Factory defines the                                                                                               Client     interface that all Concrete factories
     must implement, which consists of a set
    of methods for producing products.              This is the product                                                             family. Each concrete
                                                    factory can produce an
                                   <<interface>>                     entire set of products.         <<interface>>
                                  AbstractFactory                                                             AbstractProductA
                                  CreateProductA()
                                  CreateProductB()


                                                                                           ProductA2                    ProductA1


              ConcreteFactory1                 ConcreteFactory2
             CreateProductA()                       CreateProductA()
             CreateProductB()                       CreateProductB()
                                                                                                                     <<interface>>
                                                                                                            AbstractProductB
         The concrete factories implement
           the different product families. To
                                                                                            ProductB2                    ProductB1            create a product, the client uses
            one of these factories, so it never
            has to instantiate a product object.


156      Chapter 4


---

## PDF page 195

the factory pattern


                                                                 The clients of the Abstract
 That’s a fairly complicated class                                Factory are the two
 diagram; let’s look at it all in terms                                  instances of our PizzaStore,
 of our PizzaStore:                                                 NYPizzaStore and
                                                                                  ChicagoStylePizzaStore.


                                                                                                                  NYPizzaStore

                                                                                                                                               createPizza()

The abstract
PizzaIngredientFactory is the
 interface that defines how to
 make a family of related products—                                                                        <<interface>>
                                                                                                   Dough everything we need to make a pizza.


                                                                                             ThickCrustDough            ThinCrustDough
                                    <<interface>>
                                PizzaIngredientFactory
                              createDough()
                               createSauce()                                                                                   <<interface>>
                              createCheese()                                                                         Sauce
                                createVeggies()
                               createPepperoni()
                                                                                       PlumTomatoSauce             MarinaraSauce                               createClam()


       NYPizzaIngredientFactory             ChicagoPizzaIngredientFactory
                                                                                                                          <<interface>>
     createDough()                                 createDough()                                                         Cheese
     createSauce()                                  createSauce()
     createCheese()                                createCheese()
                                                                                                       Mozzarella Cheese           ReggianoCheese     createVeggies()                                 createVeggies()
     createPepperoni()                               createPepperoni()
     createClam()                                   createClam()

                                                                                                                          <<interface>>
                                                                                                        Clams
  The job of the                                                                        FrozenClams                FreshClams   concrete pizza
   factories is to make
   pizza ingredients. Each
   factory knows how
   to create the right                                   Each factory produces a different    objects for its region.                                         implementation for the family of products.


                                                                       you are here 4      157


---

## PDF page 196

interview with factory patterns


                              I noticed that each method in the
                               Abstract Factory actually looks like
                                a factory method (createDough(),
                                  createSauce(), etc.). Each method is
                                declared abstract and the subclasses
                                 override it to create some object. Isn’t
                                that a factory method?


                                 Is that a factory method lurking inside the
                            Abstract Factory?

                             Good catch! Yes, often the methods of an Abstract Factory are
                                   implemented as factory methods. It makes sense, right? The job of an
                                       Abstract Factory is to define an interface for creating a set of products.
                                 Each method in that interface is responsible for creating a concrete
                                        product, and we implement a subclass of the Abstract Factory to
                                       supply those implementations. So, factory methods are a natural way to
                                   implement your product methods in your abstract factories.


                   Patterns Exposed
                             This week’s interview:
                         Factory Method and Abstract Factory, on each other

            HeadFirst: Wow, an interview with two patterns at once! This is a first for us.
           Factory Method: Yeah, I’m not so sure I like being lumped in with Abstract Factory,
            you know. Just because we’re both factory patterns doesn’t mean we shouldn’t get our own
               interviews.
            HeadFirst: Don’t be miffed, we wanted to interview you together so we could help clear up
             any confusion about who’s who for the readers. You do have similarities, and I’ve heard that
              people sometimes get you confused.
           Abstract Factory: It’s true, there have been times I’ve been mistaken for Factory Method,
            and I know you’ve had similar issues, Factory Method. We’re both really good at decoupling
               applications from specific implementations; we just do it in different ways. So I can see why
              people might sometimes get us confused.
           Factory Method: Well, it still ticks me off. After all, I use classes to create and you use objects;
                 that’s totally different!

158      Chapter 4


---

## PDF page 197

the factory pattern


HeadFirst: Can you explain more about that, Factory    Factory Method: <snicker>
Method?                                              Abstract Factory: What are you snickering at, Factory
Factory Method: Sure. Both Abstract Factory and      Method?
I create objects—that’s our job. But I do it through                                              Factory Method: Oh, come on, that’s a big deal!inheritance...                                                 Changing your interface means you have to go in and
Abstract Factory: ...and I do it through object          change the interface of every subclass! That sounds like a
composition.                                                        lot of work.
Factory Method: Right. So that means, to create       Abstract Factory: Yeah, but I need a big interface
objects using Factory Method, you need to extend a class    because I am used to creating entire families of products.
and provide an implementation for a factory method.       You’re only creating one product, so you don’t really need
                                                    a big interface, you just need one method.HeadFirst: And that factory method does what?
                                                HeadFirst: Abstract Factory, I heard that you often useFactory Method: It creates objects, of course! I mean,                                                             factory methods to implement your concrete factories?the whole point of the Factory Method Pattern is that
you’re using a subclass to do your creation for you. In that  Abstract Factory: Yes, I’ll admit it, my concrete
way, clients only need to know the abstract type they are     factories often implement a factory method to create
using; the subclass worries about the concrete type. So, in    their products. In my case, they are used purely to create
other words, I keep clients decoupled from the concrete      products...
types.                                              Factory Method: ...while in my case I usually
Abstract Factory: And I do too, only I do it in a        implement code in the abstract creator that makes use of
different way.                                             the concrete types the subclasses create.
HeadFirst: Go on, Abstract Factory...you said           HeadFirst: It sounds like you both are good at what you
something about object composition?                       do. I’m sure people like having a choice; after all, factories
                                                          are so useful, they’ll want to use them in all kinds ofAbstract Factory: I provide an abstract type for                                                                 different situations. You both encapsulate object creationcreating a family of products. Subclasses of this type                                                              to keep applications loosely coupled and less dependentdefine how those products are produced. To use the                                               on implementations, which is really great, whether you’refactory, you instantiate one and pass it into some code                                                          using Factory Method or Abstract Factory. May I allowthat is written against the abstract type. So, like Factory                                                  you each a parting word?Method, my clients are decoupled from the actual
concrete products they use.                          Abstract Factory: Thanks. Remember me, Abstract
                                                              Factory, and use me whenever you have families ofHeadFirst: Oh, I see, so another advantage is that you                                                        products you need to create and you want to make suregroup together a set of related products.                                                      your clients create products that belong together.
Abstract Factory: That’s right.                                              Factory Method: And I’m Factory Method; use me to
HeadFirst: What happens if you need to extend that set   decouple your client code from the concrete classes you
of related products to, say, add another one? Doesn’t that   need to instantiate, or if you don’t know ahead of time all
require changing your interface?                           the concrete classes you are going to need. To use me, just
                                                             subclass me and implement my factory method!Abstract Factory: That’s true; my interface has to
change if new products are added, which I know people
don’t like to do....


                                                                      you are here 4      159


---

## PDF page 198

patterns compared

Factory Method and Abstract Factory compared
                                                                      PizzaStore is implemented as a Factory                                                            Method because we want to be able to                     Provides an abstract                                  create a product that varies by region.                     interface for                                     With the Factory Method, each region                      creating one product.                     PizzaStore            gets its own concrete factory that
                                                                      knows how to make pizzas that are
                                                                                          createPizza()                 appropriate for the area.
    Each subclass decides which                class to instantiate.     concrete
       New York Store                 NYPizzaStore                                     ChicagoPizzaStore
                                                           createPizza()                                                      createPizza()                 Chicago Store
    The Factory Method                      The Factory Method


                                                This is the product of the
                                                 PizzaStore. Clients only                                                                  The ChicagoPizzaStore         The NYPizzaStore subclass              rely on this abstract type.             instantiates only NY-style pizzas.                                              subclass instantiates only                                                                                     Chicago-style pizzas.


                                                                               Pizza


                        NYStyleCheesePizza                     Subclasses are                      ChicagoStyleCheesePizza
                                                                                                                  ChicagoStylePepperoniPizza                            NYStylePepperoniPizza               instantiated by the
                                                                                                                      ChicagoStyleClamPizza                                  NYStyleClamPizza                                                Factory Methods.
                                       NYStyleVeggiePizza                                                                   ChicagoStyleVeggiePizza
                                      New York               Chicago
         The createPizza() method is parameterized by pizza
            type, so we can return many types of pizza products.

160      Chapter 4


---

## PDF page 199

the factory pattern

                                                                                                              is implemented as an                                                                  PizzaIngredientFactory                                                             Abstract Factory because we need to createEach                                                                                                     ingredients).                                                        <<interface>>                    families of products (the                                                                                                              using its                                                                                               ingredients                                                    PizzaIngredientFactory                                                                           subclass implements the
                                                     createDough()                                                       own regional suppliers.Provides an abstract                      createSauce()interface for creating a                createCheese()
                                                        createVeggies()family of products.
                                                       createPepperoni()                                                                Each concrete subclass creates
                                                      createClam()                             a family of products.

New York
                          NYPizzaIngredientFactory                   ChicagoPizzaIngredientFactory         Chicago

                          createDough()                                        createDough()
                          createSauce()                                        createSauce()
                         createCheese()                                      createCheese()                                                                    Methods to create
                           createVeggies()                                        createVeggies()                       products in an Abstract                           createPepperoni()                                                                                 createPepperoni()
                          createClam()                                                                                createClam()                       Factory are often
                                                                              implemented with a
                                                                            Factory Method...
  ...for instance, the subclass                                       ... or the type of clams.
  decides the type of dough...


                      <<interface>>                                                                       <<interface>>
                    Dough                                                                 Clams


     ThinCrustDough             ThickCrustDough                                   FreshClams                FrozenClams

                                      Each ingredient
                           <<interface>>                                                                                                                           <<interface>>                                               represents a                          Sauce                                                                            Cheese                                          product that is
                                           produced by a
          MarinaraSauce            PlumTomatoSauce      Factory Method               ReggianoCheese             MozzarellaCheese
                                                  in the Abstract
                                              Factory.

   The product subclasses create parallel sets of product families.
    Here we have a New York ingredient family and a Chicago family.

                                                                     you are here 4      161


---

## PDF page 200

your design toolbox


          Tools for your Design Toolbox

               In this chapter, we added two more tools to your toolbox:                                                                All factories encapsulate object
                Factory Method and Abstract Factory. Both patterns                                                                                                     creation.
                encapsulate object creation and allow you to decouple your
              code from concrete types.                                 Simple Factory, while not a
                                                                              bona fide design pattern, is a
                                                                                          simple way to decouple your
                                                                                                           clients from concrete classes.
                 Basics                                Factory Method relies on        OO
                                Abstraction                                                    inheritance: object creation is                                                                                        delegated to subclasses, which        Principles  OO                      Encapsulation                                         implement the factory method                what varies.                                                                                                       to create objects.         Encapsulate                 Polymorphism                        over inheritance.                                                                Abstract Factory relies on        Favor composition              Inheritance                          not              to interfaces,                                                                     object composition: object         Program           implementations.                                                                          creation is implemented in                                     designs                                                methods exposed in the factory                            coupled                        loosely           Strive for                       that interact.             We have a new principle that              interface.                    objects           between                                      extension            guides us to keep things                                                                All factory patterns promote                    be open for                    should             Classes                    for modification.                abstract whenever possible.              loose coupling by reducing the           but closed                       Do not                                               dependency of your application                 on abstractions.            Depend                                       classes.                                                 on concrete classes.                 on concrete             depend
                                                               The intent of Factory Method
                                        Both of these new                      isinstantiationto allow a classto its subclasses.to defer                                                              encapsulate                                                 patterns
                                                  object creation                                      algorithms,     Patterns                                                      more                                                                                                                        is                                                                                                          to                                                                                                  create                                                                                                                  families                                                                                                                             of                                                                                                                          related                          family OO                                                          The intent of Abstract Factory               a                                                      lead to                                           and                       ofone-to-many                 defines                a        -                   defines          -                          makes                                                                     flexible                                                                                               objects                                                                                                       without                                                                                                      having                                                                                                                                to                              that   Strategy                    and                            themadditionalso                   Attach             -                                                      decoupled,               each                          objects     Observer                                       algorithm                    -                                     dynamically.Provides                                        its                betweenone,                               lets     encapsulates                                         all                                                                              depend                                                                                    on                                                                                                                            their                                                                                                         concrete                           object      Decorator                                of                 Factory                    an                    Strategy                            thestate,                                                 it.       dependency                                                           designs.                                         families                      changesto                              that         Abstract                             creating      interchangeable.               object           responsibilities                                flexible                               updateduse                                clientsfor                 a                                                                                                classes.           one                        and                                      without      when                   fromprovide                interface                                    extending          an                      notified           independently                                 objectsfor                are     vary         Decorators                      dependentsubclassing       dependents                orto                                            classes.             related                                                                                                                                        The                                                                                Dependency                                                                                                                 Inversion                           concrete           alternative                       their         automatically               specifying                                                                                                     Principle                                                                                                guides                                                                                                us                                                                                                                            to                                                                                                               avoid            functionality.                           - Defines an                     Method                                   an object, but                                dependencies on concrete                 Factory                                      creating                         interface for                                         which class to                                     types and to strive for                                    decide                        let subclasses                                   Method lets                                        abstractions.                                  Factory                                       to the                            instantiate.                                          instantiation                               Factories are a powerful                             defer                a class
                               subclasses.                                                        technique for coding to
                                                                                                   abstractions, not concrete
                                                                                                classes.


162      Chapter 4


---

## PDF page 201

the factory pattern

          Design Patterns Crossword
                             It’s been a long chapter. Grab a slice of Pizza and relax while doing
                        this crossword; all of the solution words are from this chapter.


                                                                1    2

                                                                                                                                    3

                                                                                                             4


                                                  5                 6                                            7


                                                                    8


                                                                9                                                          10


                                                  11


                                                           12


                                                                13                                           14


                                                                15

ACROSS                          DOWN
1. In Factory Method, each franchise is a ________.        2.We used ___________ in Simple Factory and Abstract
 4. In Factory Method, who decides which class to              Factory, and inheritance in Factory Method.
 instantiate?                                                      3. Abstract Factory creates a ___________ of products.
 6. Role of PizzaStore in the Factory Method Pattern.           5. Not a REAL factory pattern, but handy nonetheless.
 7. All New York–style pizzas use this kind of cheese.          10. Ethan likes this kind of pizza.
 8. In Abstract Factory, each ingredient factory is a
_______.
 9. When you use new, you are programming to an
___________.
11. createPizza() is a ____________.
12. Joel likes this kind of pizza.
13. In Factory Method, the PizzaStore and the concrete
 Pizzas all depend on this abstraction.
14. When a class instantiates an object from a concrete
 class, it's ___________ on that object.
15. All factory patterns allow us to __________ object
 creation.

                                                                       you are here 4      163


---

## PDF page 202

exercise solutions


              We’ve knocked out the NYPizzaStore; just two more to go and we’ll be ready to franchise! Write
               the Chicago-style and California-style PizzaStore implementations here:

                                                         New                                                                                    like the                                                             exactly                                                are almost                             of these stores                        Both                                                           of pizzas.                                                                      kinds                                                         different                                                  just create                                        store...they                           York

            public class ChicagoPizzaStore extends PizzaStore {
                protected Pizza createPizza(String item) {                                                                                              pizza                    if (item.equals("cheese")) {                    For the Chicago                        return new ChicagoStyleCheesePizza();        store, we just have to                   } else if (item.equals("veggie")) {             make sure we create                                                                                                                     pizzas...                        return new ChicagoStyleVeggiePizza();        Chicago-style
                   } else if (item.equals("clam")) {
                        return new ChicagoStyleClamPizza();
                   } else if (item.equals("pepperoni")) {
                        return new ChicagoStylePepperoniPizza();
                   } else return null;
               }
           }

            public class CaliforniaPizzaStore extends PizzaStore {
                protected Pizza createPizza(String item) {                                                                                                         California                    if (item.equals("cheese")) {                                ... and for the                        return new CaliforniaStyleCheesePizza();    pizza store, we create                                                                                                           pizzas.                   } else if (item.equals("veggie")) {                 California-style
                        return new CaliforniaStyleVeggiePizza();
                   } else if (item.equals("clam")) {
                        return new CaliforniaStyleClamPizza();
                   } else if (item.equals("pepperoni")) {
                        return new CaliforniaStylePepperoniPizza();
                   } else return null;
               }
           }


164      Chapter 4


---

## PDF page 203

the factory pattern

       Design Puzzle Solution


 We need another kind of pizza for those crazy Californians (crazy in a good way,
 of course). Draw another parallel set of classes that you’d need to add a new
 California region to our PizzaStore.


                                                                   PizzaStore

                                                                          createPizza()                                                                                         you need to                                                                          orderPizza()                                    Here’s everything                                                                                              pizza store,                                                                 add a California                                                                                           pizza store class,                                                                       the concrete            pizzas.                                                                                                   California-style                                                                      and the


                                NYPizzaStore                ChicagoPizzaStore              CaliforniaPizzaStore
                                    createPizza()                          createPizza()                          createPizza()


    NYStyleCheesePizza                    ChicagoStyleCheesePizza                           CaliforniaStyleCheesePizza
        NYStylePepperoniPizza                   ChicagoStylePepperoniPizza                         CaliforniaStylePepperoniPizza
              NYStyleClamPizza                      ChicagoStyleClamPizza                              CaliforniaStyleClamPizza
                   NYStyleVeggiePizza                     ChicagoStyleVeggiePizza                             CaliforniaStyleVeggiePizza


 Okay, now write the five silliest things you can think of to put on a pizza.
 Then, you’ll be ready to go into business making pizza in California!
Here             Mashed potatoes with roasted garlicare our
 suggestions...  BBQ sauce
              Artichoke hearts
            M&M’s
               Peanuts

                                                                       you are here 4      165


---

## PDF page 204

exercise solutions


                                        Let’s pretend you’ve never heard of an OO factory. Here’s a “very dependent”
                                  version of PizzaStore that doesn’t use a factory. We need for you to make a
                               count of the number of concrete pizza classes this class is dependent on. If
                             you added California-style pizzas to PizzaStore, how many classes would it be
                             dependent on then? Here’s our solution.


      public class DependentPizzaStore {
         public Pizza createPizza(String style, String type) {
             Pizza pizza = null;
             if (style.equals("NY")) {
                 if (type.equals("cheese")) {
                     pizza = new NYStyleCheesePizza();                 } else if (type.equals("veggie")) {                Handles all the
                     pizza = new NYStyleVeggiePizza();            NY-style pizzas
                 } else if (type.equals("clam")) {
                     pizza = new NYStyleClamPizza();
                 } else if (type.equals("pepperoni")) {
                     pizza = new NYStylePepperoniPizza();
                 }
             } else if (style.equals("Chicago")) {
                 if (type.equals("cheese")) {                     pizza = new ChicagoStyleCheesePizza();          Handles all the                 } else if (type.equals("veggie")) {                   Chicago-style pizzas
                     pizza = new ChicagoStyleVeggiePizza();
                 } else if (type.equals("clam")) {
                     pizza = new ChicagoStyleClamPizza();
                 } else if (type.equals("pepperoni")) {
                     pizza = new ChicagoStylePepperoniPizza();
                 }
             } else {
                 System.out.println("Error: invalid type of pizza");
                 return null;
             }
             pizza.prepare();
             pizza.bake();
             pizza.cut();
             pizza.box();
             return pizza;
         }
     }

              You can write your                                               number with                                                                                   too                answers here:            8   number            12     California


166      Chapter 4


---

## PDF page 205

the factory pattern


 Go ahead and write the ChicagoPizzaIngredientFactory; you can reference the
  classes below in your implementation:

     public class ChicagoPizzaIngredientFactory
         implements PizzaIngredientFactory
     {
         public Dough createDough() {
             return new ThickCrustDough();
         }
         public Sauce createSauce() {
             return new PlumTomatoSauce();
         }
         public Cheese createCheese() {
             return new MozzarellaCheese();
         }
         public Veggies[] createVeggies() {
             Veggies veggies[] = { new BlackOlives(),
                                   new Spinach(),
                                   new Eggplant() };
             return veggies;
         }
         public Pepperoni createPepperoni() {
             return new SlicedPepperoni();
         }
         public Clams createClam() {
             return new FrozenClams();
         }
     }
                                                              EggPlant
                      Spinach
                                                                                          ThickCrustDough
BlackOlives                        SlicedPepperoni
                                                               PlumTomatoSauce

             FrozenClams
                                                 MozzarellaCheese


                                                          you are here 4      167


---

## PDF page 206

crossword puzzle solution

        Design Patterns Crossword Solution
                      It’s been a long chapter. Grab a slice of Pizza and relax while doing this
                crossword; all of the solution words are from this chapter. Here’s the solution.


                                  1    2                        C O N  C  R  E  T  E  C  R  E  A  T O  R
                                                                                                      3                         B                                         F
                                                                                4                        J                       S U  B  C  L  A  S  S
                          E                            M
                     5                 6                                            7             S           C  R  E  A  T O  R           R  E  G  G  I  A N O
                I          T                                             L
                                       8          M           C O N  C  R  E  T  E  F  A  C  T O  R  Y
                 P        O
                                  9                                                          10                L         I M  P  L  E M  E N  T A  T  I O N
              E             P                                 Y
                     11              F  A  C  T O  R  Y M  E  T H O  D         S
            A          S                               T
                              12              C     C H  I  C  A  G O  S  T  Y  L  E        Y
             T          T                                      L
                                  13                                           14           O         P  I  Z  Z A              D  E  P  E N  D  E N  T
              R        O
                                  15              Y        E N  C  A  P  S U  L  A  T  E


168      Chapter 4
