# 7: the Adapter and Facade Patterns: Being Adaptive

_Extracted from PDF pages 275-314. Text only; images and diagrams are not embedded._


---

## PDF page 275

7 the Adapter and Facade Patterns
      BeingAdaptive


    Do you think the                                                 That’s the beauty of
readers are really getting the                                       our profession: we can
impression we’re watching a                                   make things look like
horse race rather than sitting                                      something they’re not!
in a photo studio?


                                                              Wrapped in this coat,   You mean it’s not                                                                           I’m a different man!   supposed to be a
    football match?


      In this chapter we’re going to attempt such impossible feats
     as putting a square peg in a round hole. Sound impossible? Not when
      we have Design Patterns. Remember the Decorator Pattern? We wrapped objects to
        give them new responsibilities. Now we’re going to wrap some objects with a different
       purpose: to make their interfaces look like something they’re not. Why would we do that?
      So we can adapt a design expecting one interface to a class that implements a different
         interface. That’s not all; while we’re at it, we’re going to look at another pattern that wraps
        objects to simplify their interface.


                                                                               this is a new chapter      237


---

## PDF page 276

adapters everywhere

Adapters all around us
You’ll have no trouble understanding what an OO adapter is
because the real world is full of them. How’s this for an example:
Have you ever needed to use a US-made laptop in Great Britain?
Then you’ve probably needed an AC power adapter...


         British Wall Outlet

                        AC Power Adapter
                                           US Standard AC Plug


                                                     The US laptop expects
                                                               another interface.
                           exposes                    outlet                 wall         power.          British      getting    The       for          interface     one
                                The adapter converts one
                                         interface into another.


You know what the adapter does: it sits in between the plug of your laptop and the
British AC outlet; its job is to adapt the British outlet so that you can plug your laptop
into it     and           receive                 power.                  Or look                                     at it this way: the adapter changes the interface of the                                                                                                   real-world                                                                                     otheroutlet       into         one                that                  your laptop                                 expects.                                                               How many                                                                                                   think of?                                                                                       you                                                                                  can                                                                                adaptersSome AC adapters are simple—they only change the shape of the outlet so that it
matches your plug, and they pass the AC current straight through—but other adapters
are more complex internally and may need to step the power up or down to match your
devices’ needs.
Okay, that’s the real world; what about object-oriented adapters? Well, our OO adapters
play the same role as their real-world counterparts: they take an interface and adapt it
to one that a client is expecting.


238      Chapter 7


---

## PDF page 277

the adapter and facade patterns

Object-oriented adapters

Say you’ve got an existing software system that you need to work a new vendor class library
into, but the new vendor designed their interfaces differently than the last vendor:


                        Your                    Vendor
                              Existing                    Class
                        System

                                             Their interface doesn’t match the one you’ve written                                               your code against. This isn’t going to work!


Okay, you don’t want to solve the problem by changing your existing code (and you can’t
change the vendor’s code). So what do you do? Well, you can write a class that adapts the
new vendor interface into the one you’re expecting.


                  Your                Adapter            Vendor
                      Existing                                      Class
                 System


             The                    adapter                              implements                                     the                                                          ...and talks to the vendor interface                  interface                          your                                     classes expect...                                           to service your requests.

The adapter acts as the middleman by receiving requests from the client and converting
them into requests that make sense on the vendor classes.
                                                                            of a solution                                                                                        think                                                                               you                                                                  Can                         Your                                       Adapter     Vendor                                                                  YOU to                                                                                                   require                                                                                       doesn’t                                                                       that                               Existing                                                            Class                         System                                            write ANY additional code                                                                       to integrate the new vendor
                                                                                           classes? How about making the
                                                                            vendor supply the adapter class?
                No code changes.   New code.     No code changes.

                                                                       you are here 4      239


---

## PDF page 278

turkey adapter

If it walks like a duck and quacks like a duck,
then it must might be a duck turkey wrapped
with a duck adapter...


It’s time to see an adapter in action. Remember our ducks from Chapter 1?
Let’s review a slightly simplified version of the Duck interfaces and classes:

                                                           our                                                            around,                                              This time                                                      Duck                                          a         public interface Duck {                                                       implement                                                 ducks                                                                       allows             public void quack();                 that                                                     interface                                                      and fly.                                                        quack             public void fly();             Ducks to
        }


Here’s a subclass of Duck, the MallardDuck:

         public class MallardDuck implements Duck {
             public void quack() {                                                                                   MallardDuck                 System.out.println("Quack");                                                                                 implementations:                                                                     Simple                                                                                   it is doing.            }                                                     out what                                                                      just prints
             public void fly() {
                 System.out.println("I'm flying");
            }
        }


Now it’s time to meet the newest fowl on the block:
                                                          they gobble.                                                              quack,                                                     don’t                                              Turkeys         public interface Turkey {
             public void gobble();
             public void fly();
                                                  Turkeys can fly, although they        }                                                  can only fly short distances.


240      Chapter 7


---

## PDF page 279

the adapter and facade patterns

             public class WildTurkey implements Turkey {                         implementation                                                                                   concrete                                                                                  Here’s a                                                                                                           it                public void gobble() {                                                                                        MallardDuck,                                                             of Turkey; like                    System.out.println("Gobble gobble");                                                                                  just prints out its actions.
                }

                public void fly() {
                    System.out.println("I'm flying a short distance");
                }
            }

Now, let’s say you’re short on Duck objects and you’d like to use some Turkey objects in their
place. Obviously we can’t use the turkeys outright because they have a different interface.
So, let’s write an Adapter:

       Code Up Close
                                                                      First, you need to implement the interface
                                                     of the type you’re adapting to. This is the
                                                                interface your client expects to see.
        public class TurkeyAdapter implements Duck {
            Turkey turkey;
                                                                     Next, we need to get a reference to the
                                                                          object that we are adapting; here we do            public TurkeyAdapter(Turkey turkey) {                                                                  that through the constructor.                this.turkey = turkey;
            }
                                             Now we need to implement all the methods in
                                                       the interface; the quack() translation between            public void quack() {                                                                      classes is easy: just call the gobble() method.                turkey.gobble();
            }

            public void fly() {                          Even though both interfaces have a fly()
                                                                method, Turkeys fly in short spurts—                for(int i=0; i < 5; i++) {                                                               they can’t do long-distance flying like                    turkey.fly();                                                                          ducks. To map between a Duck’s fly()               }                                                           method and a Turkey’s, we need to call
            }                                                the Turkey’s fly() method five times to
       }                                                  make up for it.


                                                                       you are here 4      241


---

## PDF page 280

test the adapter

Test drive the adapter

Now we just need some code to test drive our adapter:
                                             a Duck...     public class DuckTestDrive {                              create                                                             Let’s         public static void main(String[] args) {                                                                            Turkey.             Duck duck = new MallardDuck();                     ...and a
             Turkey turkey = new WildTurkey();                    And then wrap the turkey
             Duck turkeyAdapter = new TurkeyAdapter(turkey);         in a TurkeyAdapter, which                                                                             makes it look like a Duck.
             System.out.println("The Turkey says...");
             turkey.gobble();
             turkey.fly();                                                 Then, let’s test the Turkey:
                                                                           make it gobble, make it fly.
             System.out.println("\nThe Duck says...");
             testDuck(duck);                                        Now let’s test the duck
                                                                                 by calling the testDuck()
             System.out.println("\nThe TurkeyAdapter says...");        method, which expects a
             testDuck(turkeyAdapter);                                   Duck object.
         }                                      Now                                                         the                                                                     big                                                    off                                                                                test:                                                        the                                                       we                                                                to         static void testDuck(Duck duck) {                        turkeyasa try                                                                                       pass             duck.quack();                                                               duck...                                                      Here’s our                                                           testDuck()             duck.fly();                                                                  method;                                                                                 it                                                 gets                                        a duck                                                    and calls its         }                                                                          quack()                                           and                                                            fly()                                                         methods.    }
  Test run                 File Edit Window Help Don’tForgetToDuck
               %java DuckTestDrive
              The Turkey says...                         The Turkey gobbles and
               Gobble gobble                                               flies a short distance.              I'm flying a short distance
              The Duck says...                                                          The Duck quacks and flies               Quack                                                                                 just like you’d expect.              I'm flying
              The TurkeyAdapter says...
               Gobble gobble                                                           And the adapter gobbles when              I'm                   flying                         a                           short                                  distance
              I'm                   flying                         a                           short                                  distance                     quack() is called and flies a few times              I'm flying a short distance                  when fly() is called. The testDuck()              I'm flying a short distance                  method never knows it has a turkey
              I'm flying a short distance                        disguised as a duck!

242      Chapter 7


---

## PDF page 281

the adapter and facade patterns

The Adapter Pattern explained

Now that we have an idea of what an Adapter is, let’s step back and look
at all the pieces again.


                                                                  Adaptee
                Client           request()      translatedRequest()


  The Client is implemented
   against the target interface.

                                   Adapter

                                                             adaptee
                interface                                              interface          target                                 The Adapter implements the                          Turkey was the
                                            target interface and holds an                         adaptee interface.
                                         instance of the Adaptee.          implemented                                                     TurkeyAdapterinterface, Duck.                                                        target                                               the
 Here’s how the Client uses the Adapter

   1  The client makes a request to the adapter by
       calling a method on it using the target interface.
                                                                                       Adaptee
                                                                                             about                                                             Note that the Client andknows      The adapter translates the request into one or              are decoupled—neither   2      more calls on the adaptee using the adaptee               the other.
        interface.

   3  The client receives the results of the call and never
      knows there is an adapter doing the translation.


                                                                       you are here 4      243


---

## PDF page 282

adapter pattern defined


                                                       Let’s say we also need an Adapter that converts a Duck to a
                                                Turkey. Let’s call it DuckAdapter. Write that class:


  How did you handle the fly() method (after all, we know ducks fly longer than turkeys)?
  Check the answers at the end of the chapter for our solution. Did you think of a better way?


    How much “adapting” does an            Does an adapter always wrap one         What if I have old and new partsQ:               Q:               Q:
adapter need to do? It seems like if I need   and only one class?                          of my system, and the old parts expect
 to implement a large target interface, I                                                   the old vendor interface, but we’ve
could have a LOT of work on my hands.          The Adapter Pattern’s role is to convert    already written the new parts to use the                 A:                                        one interface into another. While most        new vendor interface? It's going to get
     You certainly could. The job of           examples of the Adapter Pattern show an      confusing using an adapter here and theA: implementing an adapter really is              adapter wrapping one adaptee, we both       unwrapped interface there. Wouldn’t I be
 proportional to the size of the interface you     know the world is often a bit more messy.       better off just writing my older code and
need to support as your target interface.        So, you may well have situations where an      forgetting the adapter?
Think about your options, however. You         adapter holds two or more adaptees that are
could rework all your client-side calls to        needed to implement the target interface.            Not necessarily. One thing you can do                                   A: the interface, which would result in a lot                                                                        is create a Two Way Adapter that supports
 of investigative work and code changes.        This relates to another pattern called the        both interfaces. To create a Two Way
Or, you can cleanly provide one class that      Facade Pattern; people often confuse the       Adapter, just implement both interfaces
encapsulates all the changes in that class.      two. Remind us to revisit this point when we     involved, so the adapter can act as an old
                                                        talk about facades later in this chapter.           interface or a new interface.


244      Chapter 7


---

## PDF page 283

the adapter and facade patterns

Adapter Pattern defined

Enough ducks, turkeys, and AC power adapters; let’s get real and look at the official
definition of the Adapter Pattern:


        The Adapter Pattern converts the interface of a class
            into another interface the clients expect. Adapter lets
             classes work together that couldn’t otherwise because of
           incompatible interfaces.


Now, we know this pattern allows us to use a client with an incompatible interface by
creating an Adapter that does the conversion. This acts to decouple the client from
the implemented interface, and if we expect the interface to change over time, the
adapter encapsulates that change so that the client doesn’t have to be modified each
time it needs to operate against a different interface.
We’ve taken a look at the runtime behavior of the pattern; let’s take a look at its class
diagram as well:

                          Client                                <<interface>>           The Adapter implements
                                                                  Target               the Target interface.                                                                      request()
          The client sees only the
            Target interface.


                                                            Adapter                           Adaptee
                                                                      request()                                     specificRequest()
                                                                                            All requests get
                           Adapter is composed                                delegated to the
                             with the Adaptee.                                 Adaptee.


The Adapter Pattern is full of good object-oriented design principles: check out the use of
object composition to wrap the adaptee with an altered interface. This approach has the
added advantage that we can use an adapter with any subclass of the adaptee.
Also check out how the pattern binds the client to an interface, not an implementation; we
could use several adapters, each converting a different backend set of classes. Or, we could
add new implementations after the fact, as long as they adhere to the Target interface.


                                                                       you are here 4      245


---

## PDF page 284

object and class adapters

Object and class adapters

Now despite having defined the pattern, we haven’t told you the whole story yet.
There are actually two kinds of adapters: object adapters and class adapters. This
chapter has covered object adapters, and the class diagram on the previous page is
a diagram of an object adapter.
So what’s a class adapter and why haven’t we told you about it? Because you need
multiple inheritance to implement it, which isn’t possible in Java. But that doesn’t
mean you might not encounter a need for class adapters down the road when using
your favorite multiple inheritance language! Let’s look at the class diagram for
multiple inheritance.


                    Client                                    Target                             Adaptee
                                                              request()                                       specificRequest()


                                                                         Adapter
                                                                                        request()
                                                                                     Instead of using composition
                                                                          to adapt the Adaptee, the
                                                                          Adapter now subclasses the
                                                                          Adaptee and the Target classes.
Look familiar? That’s right—the only difference is that with a class adapter
we subclass the Target and the Adaptee, while with an object adapter we use
composition to pass requests to an Adaptee.


       Object adapters and class adapters use two different
     means of adapting the adaptee (composition
       versus inheritance). How do these implementation
       differences affect the flexibility of the adapter?


246      Chapter 7


---

## PDF page 285

the adapter and facade patterns
     Duck Magnets
             Your job is to take the duck and turkey magnets and drag
            them over the part of the diagram that describes the role
              played by that bird, in our earlier example. (Try not to flip
             back through the pages.) Then add your own annotations
                to describe how it works.

Class Adapter

                            Client                                    Target                             Adaptee
                                                                        request()                                       specificRequest()


                                                                                Adapter
                                                                                                 request()


Object Adapter


                            Client                                <<interface>>
                                                                   Target
                                                                        request()


                                                             Adapter                           Adaptee
                                                                        request()                                     specificRequest()


  Drag these onto the class diagram
  to show which part of the diagram
  represents the Duck class and which  represents the Turkey class.


                                                                    you are here 4      247


---

## PDF page 286

exercise answer
                                           Note: the class adapter uses      Duck Magnets                                                 multiple inheritance, so you      Answer                        can’t do it in Java...

                                                                    Turkey class                                   Duck class

 Class Adapter

                               Client                                    Target                             Adaptee
                                                                           request()                                       specificRequest()
                                                                                          not                                                                                             does                                                                                                            class   Client thinks                                                                                Turkey                                  the                 he’s                                                               The                                          is                                                                                                   as                              Target                                                                                      methods   talking                                                                                  same                     The                                                                            the                                                                               have        to a Duck.                                    This                                                                                               can                                          class.                                                                                     Adapter                                                                                 the                       Duck                                                                             but                                                                             Duck,                                            client                              the                                                                                  Adapter                                                                                                                           calls                                                                                method                                is what                                            on.                                                                        Duck                                                                           take                                 methods                 request()                                 invokes                                                                       and turn around and invoke                                                                               on the Turkey class.                                                                           methods                                    The                                             Adapter                                                                 lets                                                        the                                                               Turkey respond to                                                 requests                                                on a                                                       Duck,                                                       by                                                                    extending BOTH                                                      classes (Duck and Turkey).

                                      Duck interface

 Object Adapter


                              Client                                <<interface>>                                                     The Turkey class doesn’t have the same                                                                     Target                                                                       interface                                                                           as the                                                                               Duck.                                                                                               In other                                                                          request()                                                                                                  words,                                                                  Turkeys                                                                           don’t                                                                               have                                                                                       quack()                                                                                           methods,                                                                                                          etc.Client thinks he’s
talking to a Duck.          the Class                  as with                                       is the               Just                     the Target                                 the                                       Turkey                Adapter,                                   is what                          This                            class.          on.                                            object              Duck       methods          Adapter                           Adaptee                          invokes                    client                                                                          request()                                     specificRequest()
                                                                            the Turkey                          The                                                                              Adapter,                                 Adapter                                                                                the                                                             to the                                               implements                                                  the                                                                              that                                                  Duck    Thanks                                                                                                       calls                                                                       get                                     interface,                                      but                                                                                              will                                         when it                                                     gets                                                                                                      interface.                                             a                                                                  (Adaptee)                                                                       Duck                                                                       the                             method                                                                  on                                                  call                                               it                                              turns                                                                    makes                                                 around                                                   and                                                                             client                                   delegates the calls to Turkey.


 248      Chapter 7


---

## PDF page 287

the adapter and facade patterns


                                            Tonight’s talk: Object Adapter and Class
                                      Adapter meet face to face.


Object Adapter:                                        Class Adapter:
Because I use composition I’ve got a leg up. I can
adapt not only an adaptee class, but any of its
subclasses.
                                                                That’s true, I do have trouble with that because I
                                           am committed to one specific adaptee class, but
                                                                             I have a huge advantage because I don’t have to
                                                          reimplement my entire adaptee. I can also override
                                                                the behavior of my adaptee if I need to because I’m
                                                                              just subclassing.
In my part of the world, we like to use composition
over inheritance; you may be saving a few lines
of code, but all I’m doing is writing a little code
to delegate to the adaptee. We like to keep things
flexible.
                                                                    Flexible maybe, but efficient? No. There is just one
                                                                      of me, not an adapter and an adaptee.

You’re worried about one little object? You might be
able to quickly override a method, but any behavior
I add to my adapter code works with my adaptee
class and all its subclasses.                                                            Yeah, but what if a subclass of Adaptee adds some
                                                 new behavior—then what?

Hey, come on, cut me some slack, I just need to
compose with the subclass to make that work.
                                                       Sounds messy...
You wanna see messy? Look in the mirror!


                                                                       you are here 4      249


---

## PDF page 288

real world adapters

Real-world adapters

Let’s take a look at the use of a simple Adapter in the real world
(something more serious than Ducks at least)...

Enumerators                                                                        interface.                                                                                 simple                                                               has aIf you’ve been around Java for a while, you                    Enumeration
probably       remember                     that                        the early                                    collection
types      (Vector,              Stack,                   Hashtable,                         and                               a few                           <<interface>>               Tells you if there are any moreothers) implement a method, elements(), which                Enumeration             elements in the collection.
returns an Enumeration. The Enumeration               hasMoreElements()
                                                                                     nextElement()
interface allows you to step through the
elements of a collection without knowing
the specifics of how they are managed in the                                      Gives you the next elementcollection.                                                                              in the collection.

                                                                                    Analogous to hasMoreElements()
                                                                                               in the Enumeration interface.Iterators                                                                               This method just tells you if
                                                                                           you’ve looked at all the items inThe more recent Collection classes use an                           <<interface>Iterator interface that, like the Enumeration                             Iterator                 the collection.
interface, allows you to iterate through a set of            hasNext()
items in a collection, and adds the ability to                  next()                             Gives you the next
remove items.                                                            remove()                         element in the collection.
                                                                            Removes an item from
                                                                         the collection.


Using Enumerators with code that expects Iterators

We are sometimes faced with legacy code that exposes the
Enumeration interface, yet we’d like for our new code to use only
Iterators. It looks like we need to build an adapter.


250      Chapter 7


---

## PDF page 289

the adapter and facade patterns

Adapting an Enumeration to an Iterator

First we’ll look at the two interfaces to figure out how the methods map from one to
the other. In other words, we’ll figure out what to call on the adaptee when the client
invokes a method on the target.
                                                   These two methods look easy.
                                              They map straight to hasNext()
                                                  and next() in Iterator.        Target interface

                           <<interface>>                             <<interface>>
                                 Iterator                           Enumeration
                       hasNext()                                hasMoreElements()
                          next()                                      nextElement()
                      remove()
                                                                   Adaptee interface
                       But what about this method
                             remove() in Iterator? There’s
                             nothing like that in Enumeration.


Designing the Adapter

Here’s what the classes should look like: we need an adapter that implements the Target
interface and is composed with an adaptee. The hasNext() and next() methods are going
to be straightforward to map from target to adaptee: we just pass them right through.
But what do you do about remove()? Think about it for a moment (and we’ll deal with it
on the next page). For now, here’s the class diagram:

  Your new code still gets                  <<interface>>             We’re making the Enumerations
                                                       Iterator                  in your old code look like  to use Iterators, even
   if there’s really an                  hasNext()                      Iterators for your new code.
  Enumeration underneath.             next()                                 A class
                                          remove()                                                                                                  implementing
                                                                                   the Enumeration
                                                                                                   interface is the
                                                                                               adaptee.
       EnumerationIterator            EnumerationIterator                                <<interface>>Enumeration
           is the adapter.                                           hasNext()                                       hasMoreElements()
                                                 next()                                              nextElement()
                                          remove()


                                                                       you are here 4      251


---

## PDF page 290

enumeration iterator adapter

Dealing with the remove() method

Well, we know Enumeration doesn’t support remove(). It’s a “read only” interface. There’s no
way to implement a fully functioning remove() method on the adapter. The best we can do is
throw a runtime exception. Luckily, the designers of the Iterator interface foresaw this need and
defined the remove() method so that it supports an UnsupportedOperationException.
This is a case where the adapter isn’t perfect; clients will have to watch out for potential
exceptions, but as long as the client is careful and the adapter is well documented, this is a
perfectly reasonable solution.


Writing the EnumerationIterator adapter

Here’s simple but effective code for all those legacy classes still producing Enumerations:
                                                                                        Since we’re adapting
                                                                                Enumeration to Iterator,
                                                                                  our Adapter implements the
                                                                                     Iterator interface...it has to  public class EnumerationIterator implements Iterator<Object> {                                                                                          look like an Iterator.      Enumeration<?> enumeration;
                                                                    The Enumeration we’re
      public EnumerationIterator(Enumeration<?> enumeration) {      adapting. We’re using
          this.enumeration = enumeration;                                   composition, so we stash it
                                                                                                          in an instance variable.     }

      public boolean hasNext() {                          The Iterator’s hasNext() method
          return enumeration.hasMoreElements();                   is delegated to the Enumeration’s
                                                                     hasMoreElements() method...     }
                                                                                         ...and the Iterator’s next() method
                                                                                                            is delegated to the Enumeration’s      public Object next() {                                                                      nextElement() method.          return enumeration.nextElement();
     }

      public void remove() {                                                                            Unfortunately, we can’t support
          throw new UnsupportedOperationException();          Iterator’s remove() method, so
     }                                                        we have to punt (in other words,
                                                               we give up!). Here we just throw }                                                                      an exception.


252      Chapter 7


---

## PDF page 291

the adapter and facade patterns


               While Java has gone in the direction of the Iterator interface, there is nevertheless still legacy
                   client code that depends on the Enumeration interface, so an Adapter that converts an Iterator to
              an Enumeration could potentially be useful.
                Write an Adapter that adapts an Iterator to an Enumeration. You can test your code by
                adapting an ArrayList. The ArrayList class supports the Iterator interface but doesn’t support
               Enumerations.


Some AC adapters do more than just change the interface—they add other features
like surge protection, indicator lights, and other bells and whistles.
If you were going to implement these kinds of features, what pattern would you use?


                                                                 you are here 4      253


---

## PDF page 292

fireside chats: decorator and adapter


                                            Tonight’s talk: The Decorator Pattern and the Adapter
                                         Pattern discuss their differences.


Decorator:                                           Adapter:
I’m important. My job is all about responsibility—you
know that when a Decorator is involved, there’s
going to be some new responsibilities or behaviors
added to your design.
                                                   You decorators want all the glory while us adapters
                                                                are down in the trenches doing the dirty work:
                                                                converting interfaces. Our jobs may not be
                                                             glamorous, but our clients sure do appreciate us
                                                       making their lives simpler.
That may be true, but don’t think we don’t work
hard. When we have to decorate a big interface,
whoa, that can take a lot of code.

                                                        Try being an adapter when you’ve got to bring
                                                                      several classes together to provide the interface your
                                                                           client is expecting. Now that’s tough. But we have a
                                                                     saying: “A decoupled client is a happy client.”

Cute. Don’t think we get all the glory; sometimes
I’m just one decorator that is being wrapped by who
knows how many other decorators. When a method
call gets delegated to you, you have no idea how
many other decorators have already dealt with it
and you don’t know that you’ll ever get noticed for
your efforts servicing the request.

                                                            Hey, if adapters are doing their job, our clients
                                                             never even know we’re there. It can be a thankless
                                                                         job.


254      Chapter 7


---

## PDF page 293

the adapter and facade patterns


Decorator:                                           Adapter:
                                                         But the great thing about us adapters is that we
                                                                allow clients to make use of new libraries and
                                                                    subsets without changing any code; they just rely on
                                                               us to do the conversion for them. Hey, it’s a niche,
                                                              but we’re good at it.

Well, us decorators do that as well, only we allow
new behavior to be added to classes without altering
existing code. I still say that adapters are just fancy
decorators—I mean, just like us, you wrap an object.
                                                       No, no, no, not at all. We always convert the
                                                                      interface of what we wrap; you never do. I’d say a
                                                               decorator is like an adapter; it's just that you don’t
                                                         change the interface!
Uh, no. Our job in life is to extend the behaviors or
responsibilities of the objects we wrap; we aren’t a
simple pass through.
                                                            Hey, who are you calling a simple pass through?
                                            Come on down and we’ll see how long you last
                                                                converting a few interfaces!


Maybe we should agree to disagree. We seem to
look somewhat similar on paper, but clearly we are
miles apart in our intent.
                                        Oh yeah, I’m with you there.


                                                                       you are here 4      255


---

## PDF page 294

who does what?

And now for something different...

There’s another pattern in this chapter.

You’ve seen how the Adapter Pattern converts the interface of a class into one
that a client is expecting. You also know we achieve this in Java by wrapping
the object that has an incompatible interface with an object that implements
the correct one.
We’re going to look at a pattern now that alters an interface, but for a different
reason: to simplify the interface. It’s aptly named the Facade Pattern because
this pattern hides all the complexity of one or more classes behind a clean,
well-lit facade.


                Match each pattern with its intent:


               Pattern                             Intent

                                               Converts one interface to
                 Decorator                                                 another

                Adapter                                                    Doesn’t alter the interface,
                                                  but adds responsibility
                Facade
                                        Makes an interface simpler


256      Chapter 7


---

## PDF page 295

the adapter and facade patterns

Home Sweet Home Theater

Before we dive into the details of the Facade Pattern, let’s take a look at a
growing national obsession: building a nice theater to binge-watch all those
movies and TV series.
You’ve done your research and you’ve assembled a killer system complete
with a streaming player, a projection video system, an automated screen,
surround sound, and even a popcorn popper.
Check out all the components you’ve put together:


                                                                                       Amplifier

                                                                                         tuner
                                                                                          player
                                                                                            on()
                                                                                                                    off()
                                                                                       setStreamingPlayer()
                                   Tuner                                   setStereoSound()
                                   amplifier                                            setSurroundSoud()                                        StreamingPlayer
                                                                                         setTuner()                                                          amplifier                                 on()                                                                                    setVolume()
                                          off()                                                                                                                                                            on()                     That’s a lot of                                                                                                             toString()
                              setAm()                                                                                                                                                 off()                                                                                                                        classes, a lot                              setFm()                                                                                                          pause()                               setFrequency()                                                                                                                   play()                  of interactions,
                                        toString()                                                                                                          setSurroundAudio()                                                                                                                                         setTwoChannelAudio()           and a big set
                                                                                                                                                                   stop()                  of interfaces to
                                                                                                                                                                         toString()                                                                                                        learn and use.
                            Screen
                          up()
                       down()
                               toString()

                                                                                                                                            Projector

                                                                                                                                                          player

                                PopcornPopper                                                                                              on()
                                                                                                                                                                                                      off()
                                      on()                                                                                                        tvMode()
                                                off()                                             TheaterLights                                    wideScreenMode()
                                    pop()                                                                                                                                       toString()
                                             toString()                                             on()
                                                                                                                    off()
                                                                                         dim()
                                                                                                             toString()


You’ve spent weeks running wire, mounting the projector, making all the
connections, and fine tuning. Now it’s time to put it all in motion and enjoy a
movie...


                                                                       you are here 4      257


---

## PDF page 296

tasks to watch a movie

Watching a movie (the hard way)

Pick out a movie, relax, and get ready for movie magic.
Oh, there’s just one thing—to watch the movie, you need
to perform a few tasks:


     1  Turn on the popcorn popper
     2  Start the popper popping
     3  Dim the lights
     4        Put the screen down
     5  Turn the projector on
     6  Set the projector input to streaming player
     7  Put the projector on widescreen mode
     8  Turn the sound amplifier on
     9  Set the amplifier to streaming player input
     10        Set the amplifier to surround sound
                                                                                  I’m already exhausted
     11        Set the amplifier volume to medium (5)                      and all I’ve done is turn
                                                                                     everything on!
     12 Turn the streaming player on
     13 Start playing the movie


258      Chapter 7


---

## PDF page 297

the adapter and facade patterns


Let’s check out those same tasks in terms of the classes and the
method calls needed to perform them:
                                                                Turn on the popcorn popper and start
                                                                                       popping...
                         popper.on();
                         popper.pop();
                                                        Dim the lights to 10%...
                        lights.dim(10);
                classes                                                               Put the screen down... Six different
  involved!                 screen.down();
                                                                  Turn on the projector and put it in                         projector.on();                                                                          widescreen mode for the movie...                         projector.setInput(player);
                         projector.wideScreenMode();
                        amp.on();                            Turn on the amp, set it to Streamingmode,                                                                                      surround-sound                                                                                   player, put it in                         amp.setStreamingPlayer(player);                                                                and set the volume to 5...                        amp.setSurroundSound();
                        amp.setVolume(5);
                                                                   Turn on the Streaming player...                         player.on();                                                                 and FINALLY, play the movie!                         player.play(movie);


But there’s more...

     When the movie is over, how do you turn everything off? Wouldn’t you have to do all
          of this over again, in reverse?
      Wouldn’t it be as complex to listen to the radio?
        If you decide to upgrade your system, you’re probably going to have to learn a slightly
          different procedure.


So what to do? The complexity of using your home theater is becoming apparent!
Let’s see how the Facade Pattern can get us out of this mess so we can enjoy the movie...


                                                                       you are here 4      259


---

## PDF page 298

lights, camera, facade

Lights, Camera, Facade!

A Facade is just what you need: with the Facade Pattern you can take a complex
subsystem and make it easier to use by implementing a Facade class that provides
one, more reasonable interface. Don’t worry; if you need the power of the complex
subsystem, it’s still there for you to use, but if all you need is a straightforward
interface, the Facade is there for you.
 Let’s take a look at how the Facade operates:


                                                                              Facade class treats  1  Okay, time to create a                                          2 The
     Facade for the home                                                     the home theater
      theater system. To do this                                            components as a
    we create a new class      The Facade                                    subsystem, and calls
      HomeTheaterFacade,                                           on the subsystem
      which exposes a few                                                      to implement its
      simple methods such as                                                 watchMovie() method.
       watchMovie().                                        HomeTheaterFacade
                                                                                    watchMovie()
                                                                                   endMovie()
                                                                                              listenToRadio()
                                                                                    endRadio()


                                                                                                                                    Amplifier
                                                                                                                                                                                        tuner
                                                                                                                                                                                         player
                                                                                                                                                                                             on()
                                                                                                                                                                                                                                              off()
                                                                                                                                                                                   setStreamingPlayer()
                                                                                 Tuner                                      setStereoSound()
                                                                                                                                    amplifier                                                  setSurroundSoud()                                    StreamingPlayer
                                                                                                                                                                                       setTuner()                                                                                                                                                                                                                                                                                         amplifier                                                                                                                             on()
                                                                                                                                                                             setVolume()
                                                                                                                                                             off()                                                                                                                                                                                                                                                                          on()
                                                                                                                                                                                                            toString()
                                                                                                                                                                                                                                                                                                                                               off()                                                                                                               setAm()                                                                                                                 setFm()                                                                                                                        pause()                 play()
                                                                                                                   setFrequency()                                                                                                                                   play()
                                                                                                                                       toString()                                                                                                                       setSurroundAudio()
                                                                                                                                                                                                                                         setTwoChannelAudio()
                                                                                                                                                                                                                                                                                     stop()
                                                                                                                                                                                                                                                                                               toString()

                                                                          Screen
                                                                                                                     up()
                                                                                                      down()
  The subsystem the                                                    toString()                                                                                                 Projector             is simplifying.                                                                                                                                                                                      player   Facade
                                                                           PopcornPopper                                                                                                        on()off()
                                                                                                                                  on()                                                                                                                     tvMode()
                                                                                                                                                                    off()                                      TheaterLights                                       wideScreenMode()
                                                                                                                            pop()                                                                                                                                           toString()
                                                                                                                                             toString()                                                 on()                                                                                                                                                                                                                                              off()                               on()
                                                                                                                                                                                        dim()
                                                                                                                                                                                                            toString()


260      Chapter 7


---

## PDF page 299

the adapter and facade patterns


                                    A client of the
                                                    subsystem facade.watchMovie()


   Your client code now calls3   methods on the home theater
    Facade, not on the subsystem.
   So now to watch a movie we just
                    watchMovie(),     call one method,
    and it communicates with
    the lights, streaming player,
     projector, amplifier, screen, and
    popcorn maker for us.


        I’ve got to have
   my low-level access!


                               4   The Facade still leaves the subsystem
                                              accessible so it can be used directly. If
                                     you need the advanced functionality
                                                                      classes,                                                                 they are         Former president of the               availableof the subsystemfor your                                                                 use.         Rushmore High School
       A/V Science Club.


                                                           you are here 4      261


---

## PDF page 300

facade versus adapter


          If the facade encapsulates the             What is the benefit of the facadeQ:               Q:
subsystem classes, how does a client        other than the fact that I now have a
 that needs lower-level functionality gain     simpler interface?access to them?                        A facade not
                                           The Facade Pattern also allows you                 A:                         only simplifies     Facades don’t “encapsulate” the            to decouple your client implementationA:subsystem classes; they merely provide a       from any one subsystem. Let’s say that you                                            an interface, it simplified interface to their functionality. The     get a big raise and decide to upgrade your
subsystem classes still remain available       home theater to all new components that for direct use by clients that need to use        have different interfaces. Well, if you coded       decouples a client
more specific interfaces. This is a nice          your client to the facade rather than the property of the Facade Pattern: it provides      subsystem, your client code doesn’t need to      from a subsystem
a simplified interface while still exposing the     change, just the facade (and hopefully the full functionality of the system to those who      manufacturer is supplying that!).             of components.
may need it.
                                        So the way to tell the difference                 Q:
     Does the facade add any             between the Adapter Pattern and theQ: functionality or does it just pass through    Facade Pattern is that the adapter wraps      Facades and
each request to the subsystem?           one class and the facade may represent                                  many classes?                   adapters may
    A facade is free to add its own “smarts”A:                                       wrap multiple in addition to making use of the subsystem.          No! Remember, the Adapter Pattern                 A:For instance, while our home theater facade    changes the interface of one or more classesdoesn’t implement any new behavior, it is         into one interface that a client is expecting.         classes, but a
smart enough to know that the popcorn         While most textbook examples show thepopper has to be turned on before it can pop    adapter adapting one class, you may need to      facade’s intent is
(as well as the details of how to turn on and     adapt many classes to provide the interfacestage a movie showing).                    a client is coded to. Likewise, a Facade may       to simplify, while
                                            an adapter’s     Does each subsystem have only        class with a very complex interface.Q:                                         provide a simplified interface to a single
one facade?                                       The difference between the two is not in            is to convert
     Not necessarily. The pattern certainly      terms of how many classes they “wrap,” itA:                                                  the interfaceallows for any number of facades to be             is in their intent. The intent of the Adapter
created for a given subsystem.                  Pattern is to alter an interface so that it                                         matches one a client is expecting. The          to something
                                                      intent of the                                                  Facade                                                                    Pattern                                                                                                 is to provide a        different.                                                     simplified                                                              interface                                                                          to                                                           a subsystem.


262      Chapter 7


---

## PDF page 301

the adapter and facade patterns

Constructing your home theater facade

Let’s step through the construction of the HomeTheaterFacade class.
The first step is to use composition so that the facade has access to all the
components of the subsystem:

      public class HomeTheaterFacade {                                                            Here’s the composition; these
          Amplifier amp;                        are all the components of the
          Tuner tuner;                            subsystem we are going to use.
          StreamingPlayer player;
          Projector projector;
          TheaterLights lights;
          Screen screen;
          PopcornPopper popper;

          public HomeTheaterFacade(Amplifier amp,
                       Tuner tuner,
                       StreamingPlayer player;
                                                           The facade is passed a                       Projector projector,                                                                            reference to each component                       Screen screen,                                                                of the subsystem in its
                       TheaterLights lights,                    constructor. The facade
                       PopcornPopper popper) {               then assigns each to the
                                                                              corresponding instance variable.
              this.amp = amp;
              this.tuner = tuner;
              this.player = player;
              this.projector = projector;
              this.screen = screen;
              this.lights = lights;
              this.popper = popper;
          }

              // other methods here
                                                          We’re just about to fill these in...
      }


                                                                       you are here 4      263


---

## PDF page 302

implementing facade

Implementing the simplified interface

Now it’s time to bring the components of the subsystem together into a unified interface.
Let’s implement the watchMovie() and endMovie() methods:
    public void watchMovie(String movie) {
        System.out.println("Get ready to watch a movie...");
        popper.on();
        popper.pop();                                             watchMovie() follows the same sequence        lights.dim(10);                                    we had to do by hand before, but wraps                                                                                it up in a handy method that does all        screen.down();                                                                 the work. Notice that for each task we        projector.on();                                                                       are delegating the responsibility to the        projector.wideScreenMode();                               corresponding component in the subsystem.
        amp.on();
        amp.setStreamingPlayer(player);
        amp.setSurroundSound();
        amp.setVolume(5);
        player.on();
        player.play(movie);
    }
                                                                    And endMovie() takes care of
                                                                                        shutting everything down for    public void endMovie() {                                                                                                           us. Again, each task is delegated        System.out.println("Shutting movie theater down...");                                                                             to the appropriate component in        popper.off();                                                    the subsystem.
        lights.on();
        screen.up();
        projector.off();
        amp.off();
        player.stop();
        player.off();
    }


                                         Think about the facades you’ve encountered in the Java
                                          API. Where would you like to have a few new ones?


264      Chapter 7


---

## PDF page 303

the adapter and facade patterns

Time to watch a movie (the easy way)

It’s showtime!
                                                             Here we’re creating the components
 public class HomeTheaterTestDrive {                   right in the test drive. Normally the
     public static void main(String[] args) {        client is given a facade; it doesn’t have
                                                             to construct one itself.         // instantiate components here
         HomeTheaterFacade homeTheater =                                  First you instantiate
                                                                             the Facade with all the                 new HomeTheaterFacade(amp, tuner, player,                                                                                components in the subsystem.                         projector, screen, lights, popper);

         homeTheater.watchMovie("Raiders of the Lost Ark");
         homeTheater.endMovie();                            Use the simplified interface to
                                                                             first start the movie up, and     }                                                                  then shut it down.
 }                                                     File Edit Window Help SnakesWhy’dItHaveToBeSnakes?
                        %java HomeTheaterTestDrive
    Here’s the output.        Get ready to watch a movie...
                        Popcorn Popper on    Calling the Facade’s                        Popcorn Popper popping popcorn!   watchMovie() does all                        Theater Ceiling Lights dimming to 10%   this work for us...                        Theater Screen going down
                        Projector on
                        Projector in widescreen mode (16x9 aspect ratio)
                        Amplifier on
                        Amplifier setting Streaming player to Streaming Player
                        Amplifier surround sound on (5 speakers, 1 subwoofer)
                        Amplifier setting volume to 5
                        Streaming Player on
                        Streaming Player playing "Raiders of the Lost Ark"
                        Shutting movie theater down...
  ...and here, we’re done       Popcorn Popper off
  watching the movie, so       Theater Ceiling Lights on
  calling endMovie() turns      Theater Screen going up
  everything off.            Projector off
                        Amplifier off
                        Streaming Player stopped "Raiders of the Lost Ark"
                        Streaming Player off
                        %


                                                                       you are here 4      265


---

## PDF page 304

facade pattern defined

Facade Pattern defined

To use the Facade Pattern, we create a class that simplifies and unifies a set of more complex
classes that belong to some subsystem. Unlike a lot of patterns, Facade is fairly straightforward;
there are no mind-bending abstractions to get your head around. But that doesn’t make it
any less powerful: the Facade Pattern allows us to avoid tight coupling between clients and
subsystems, and, as you will see shortly, also helps us adhere to a new object-oriented principle.
Before we introduce that new principle, let’s take a look at the official definition of the pattern:


               The Facade Pattern provides a unified interface to a
                         set of interfaces in a subsystem. Facade defines a higher-
                         level interface that makes the subsystem easier to use.


There isn’t a lot here that you don’t already know, but one of the most important things to
remember about a pattern is its intent. This definition tells us loud and clear that the purpose
of the facade is to make a subsystem easier to use through a simplified interface. You can see
this in the pattern’s class diagram:

                                                                                    Unified interface
                                                             Client                                  Facade                 that is easier to use.   Happy client whose          became   job just    easier because of
   the facade.                                     subsystem classes

                         subsystem.        More complex


That’s it; you’ve got another pattern under your belt! Now, it’s time for that new OO principle.
Watch out, this one can challenge some assumptions!

266      Chapter 7


---

## PDF page 305

the adapter and facade patterns

   The Principle of Least Knowledge

     The Principle of Least Knowledge guides us to reduce the
        interactions between objects to just a few close “friends.”
     The principle is usually stated as:


                    Design Principle
                             Principle of Least Knowledge: talk
                           only to your immediate friends.


      But what does this mean in real terms? It means when you
       are designing a system, for any object, be careful of the
      number of classes it interacts with and also how it comes to
        interact with those classes.
      This principle prevents us from creating designs that have
      a large number of classes coupled together so that changes
        in one part of the system cascade to other parts. When you
       build a lot of dependencies between many classes, you are
       building a fragile system that will be costly to maintain and
      complex for others to understand.


How many classes is this code coupled to?

public float getTemp() {
    return station.getThermometer().getTemperature();
}


                                                          you are here 4      267


---

## PDF page 306

principle of least knowledge

How NOT to Win Friends and Influence Objects

Okay, but how do you keep from doing this? The principle
provides some guidelines: take any object, and from any
method in that object, invoke only methods that belong to:
                                                                                                tell us not                                                                                            guidelines                                                                                were                                                                     these                                                                          that  The object itself                                           that                                                          Notice      on objects                                                                                         methods!!                                                              methods                                                                           other  Objects passed in as a parameter to the method            to call                                                                                           calling                                                          from                                                            returned
  Any object the method creates or instantiates                                                                                 as any object that is                                                                         “component”  Any components of the object                              Think of a                                                                                                         variable. In other                                                              by an instance                                                                                                                  relationship.                                                                 referenced                                                                 words, think of this as a HAS-A
This sounds kind of stringent, doesn’t it? What’s the harm
in calling the method of an object we get back from another
call? Well, if we were to do that, then we’d be making a
request of another object’s subpart (and increasing the
number of objects we directly know). In such cases, the
principle forces us to ask the object to make the request for us;
that way, we don’t have to know about its component objects
(and we keep our circle of friends small). For example:

              public float getTemp() {   Without the                  Thermometer thermometer = station.getThermometer();    Principle
                  return thermometer.getTemperature();
              }
                                                                     Here we get the thermometer object
                                                              from the station and then call the
                                                                        getTemperature() method ourselves.

   With the              public float getTemp() {    Principle                  return station.getTemperature();
              }                                                   When we apply the principle, we add a method
                                                          to the Station class that makes the request
                                                          to the thermometer for us. This reduces the
                                                         number of classes we’re dependent on.


268      Chapter 7


---

## PDF page 307

the adapter and facade patterns

Keeping your method calls in bounds...

Here’s a Car class that demonstrates all the ways you can call methods and still
adhere to the Principle of Least Knowledge:                                                             of this                                                               component                                                                Here’s a                                                                             methods.    public class Car {                                         class. We can call its
           Engine engine;
           // other instance variables
           public Car() {                               Here we’re creating a new
                                                                      object; its methods are legal.                 // initialize engine, etc.
          }                                                                   You can call a method on an
                                                                         object passed as a parameter.
           public void start(Key key) {
                 Doors doors = new Doors();                                                                         method on a                                                               You can call a                 boolean authorized = key.turns();                of the object.                                                                    component                 if (authorized) {
                        engine.start();
                        updateDashboardDisplay();          You can call a local method
                                                                              within the object.                        doors.lock();
                 }                                              You can call a method on an
          }                                                            object you create or instantiate.
           public void updateDashboardDisplay() {
                 // update display
          }
    }


                                        be used when and where they are helpful.      There is another principle called the                                                        Yes; while the principle reducesQ:                                                    All design involves tradeoffs (abstractions  A:Law of Demeter; how are they related?                                                       the dependencies between objects and                                             versus speed, space versus time, and so on)                                                                                                studies have shown this reduces software                                        and while principles provide guidance, you                                                                                       maintenance,                                                                                                                                                                                                        it is also                                                                                                                     the case                                                                                                                                           that applying     The two are               one                   and the                          same,                               and                                             should take                                                                                  all factors into account beforeA:                                                                                                                this principle results                                                                                                                                         in more                                                                                                                       “wrapper” you’ll encounter               these                     terms                           being                             used                                               applying                                                    them.
 interchangeably. We prefer to use the                                                        classes being written to handle method
 Principle of Least Knowledge for a couple                                                              calls to other components. This can result in
                                             Are there any disadvantages           increased complexity and development time of reasons: (1) the name is more intuitive,   Q:
                                               to applying the Principle of Least           as well as decreased runtime performance.and (2) the use of the word “Law” implies we                                     Knowledge?always have to apply this principle. In fact,
no principle is a law; all principles should

                                                                       you are here 4      269


---

## PDF page 308

violating the principle of least knowledge


                                  Do either of these classes violate the Principle of Least
                                       Knowledge? Why or why not?
    public House {
        WeatherStation station;

        // other methods and constructor

        public float getTemp() {
             return station.getThermometer().getTemperature();
        }
   }
    public House {
         WeatherStation station;

        // other methods and constructor

        public float getTemp() {
             Thermometer thermometer = station.getThermometer();
             return getTempHelper(thermometer);
        }

        public float getTempHelper(Thermometer thermometer) {
            return thermometer.getTemperature();
        }                                              Hard hat area.
   }                                                   watchfallingoutassumptionsfor


     Can you think of a common use of Java that
       violates the Principle of Least Knowledge?
      Should you care?

                                                                          System.out.println()? about How Answer:

270      Chapter 7


---

## PDF page 309

the adapter and facade patterns

The Facade Pattern and the Principle of Least Knowledge
                                                                                             friend:                                                                             only has one                                                            This client             In OO                                                       the HomeTheaterFacade.only one                                                                                having                                                                 programming,     thing!                                                                                   is a GOOD                                                                 friend                                                           Client


    HomeTheaterFacade
     manages all those subsystem
     components for the client.                                            HomeTheaterFacade
     It keeps the client simple                                                       watchMovie()
    and flexible.                                                                      endMovie()                                                                                                        listenToRadio()
                                                                                              endRadio()


                                                                                                                                                                                                            tuner              the home                                                                                          Amplifier                                                                                                                                                                                                            player         upgrade  We can                    without                                                                                                                     on()          components                                                                                                                                                                                  off()   theater                                                                                                                                                                      setStreamingPlayer()          the client.                                                   Tuner                                      setStereoSound()   affecting                                                                                                                amplifier                                                  setSurroundSoud()                                    StreamingPlayer
                                                                                                                                                                                                           setTuner()                                                                                                                                                                                                                                                                                                               amplifier                                                                                                                                                 on()
                                                                                                                                                                                               setVolume()
                                                                                                                                                                                       off()                                                                 toString()                                                                on()
                                                                                                                                 setAm()                                                                                                                                                                     off()
                                                                                                                                   setFm()                                                                                                                        pause()
                                                                                                                                      setFrequency()                                                                                                                                   play()
                                                                                                                                                            toString()                                                                                                                       setSurroundAudio()
                                                                                                                                                                                                                                                           setTwoChannelAudio()
                                                                                                                                                                                                                                                                                                          stop()
                                                                                                                                                                                                                                                                                                                     toString()

                                                                                     Screen
                                                                                                                                         up()
                subsystems We try to keep                                                                              down()                   of Least        to the Principle                                                                  toString()                                                                                                 Projector adhering                                                                                                                                                                                                                                                                                         player          as well. If this gets too Knowledge
                                                                                      PopcornPopper                                                                                                        on()off()
                                                                                                                                                                                                                                                                  tvMode() complex and too many friends are                                              on()           we can introduce                                                                    off()                                      TheaterLights                                       wideScreenMode()
                                                                                                                                                                                                                                                                                                                      toString()  intermingling,                                                                                                                                               pop()
                                                                                                                                                                  toString()                                                 on()           facades to form layers
                                                                                                                                                                                                                                                                        off()  additional
                                                                                                                                                                                                            dim()  of subsystems.                                                                                                                                                                            toString()


                                                                       you are here 4      271


---

## PDF page 310

your design toolbox

         Tools for your Design Toolbox
                                                                When you need to use
           Your toolbox is starting to get heavy! In this chapter we’ve                                                                               an existing class and its
           added a couple of patterns that allow us to alter interfaces and                                                                                                       interface is not the one you
            reduce coupling between clients and the systems they use.                                                                                        need, use an adapter.
                                                                When you need to simplify
                                                                               and unify a large interface or
                                                                                  complex set of interfaces, use                 Basics        OO                                                                               a facade.
                                Abstraction                                                                An adapter changes an        Principles  OO                      Encapsulation                                                   interface into one a client                             varies.                                                                                              expects.         Encapsulate what                                  Polymorphism                        over inheritance.        Favor composition                                                 A facade decouples a client                          not     Inheritance              to interfaces,                                                               from a complex subsystem.         Program
           implementations.                                                  Implementing an adapter may                                     designs                            coupled               for loosely                                                                          require little work or a great           Strive                       that interact.                    objects                                                                                                              of work                                                                                               depending                                                                                                  on                                                          technique           between                                                                          level                deal                                      extension       We have a new                                                                                               the size                                                                                     and                                                                                                         complexity                                    a low                    be open for                    should                                                                                                          of the             Classes                                                   maintaining                                                                 designs                                      for                                                                                                       target                                                                                                                 interface.                             modification.                                                  our                    for                                                     in                 closed           but                                                     coupling                                                 to your                                 of                                                            only                       Do not                                                      talk                                                                                                                                                      Implementing                                                                                          a facade                          abstractions.                 on                                             (remember,            Depend                                       classes.                                                                                                 requires that we compose                       concrete                          friends)...             depend on
                                                                                           facade                                                                                                              with its subsystem                                 friends.                                                             the               Talk only to your                                                                               and                                                                                     use delegation                                                                                                                              to
                                                                                         perform the work of the                                                              ...and TWO new patterns.                                                                                             facade.                                            Each changes an interface,
                                              the adapter to convert,        There are two forms of the                                                           to unify                                                        facade                                                  the     Patterns                                             and                                      algorithms,                                                                                        Adapter                                                                                                             Pattern:                                                                                                                   object                       of OO                          family               a                         one-to-many                 defines                a        -                                                                 simplify.                            them                                             and                                                                               and                                                                                                    class                                                                                                        adapters.                                                                                                         Class                                an                                additional                   defines          -                          makes                             that   Strategy                    and                            so                   Attach                                 an            -                   -                     one,               each                         objects                                Define    Observer                                       algorithm                     -                                 Providedynamically.                            the                Factory                                                                                          adapters                                                                                                            require                                                                                                                       multiple                                       its                             of                between                               lets                                           one                          object      Decorator     encapsulates                                         all                   an                                         has                                    but                 to              Method                                    families                    Strategy                                          only                               state,                                                 it.        Abstract      dependency                                       object,                                      use                                          class                           an                      a                         creating                     changes                              that         Factory                 for          responsibilities                                flexible                                                                                                      inheritance.                           Ensure                 a      interchangeable.                                   without               object                                clients                 -                                   of                           creating                                              request                              updated                            a          one                   for                   from                                           pointto            interface                        and                    provide                               objects                                           class      when                                    extending                                        global              interface             Singleton                               which                            forEncapsulates                   -           independently                    depedentnotified        Decorators                are               or     vary                            provide                          decide                                         you                                          classes.a                          subclassing                    and                                           lets            related               to                                          letting       dependents                          of            Command                    subclasses                                                                                        concrete                                                                              You                                                                                     can                                                                                             implement                                                                                            more                                                                                                                 than                  instance              let                           Method                              thereby                     their          alternative                            interface                        Factory                   the                          object,                              it.                                            different                 an             specifying                                   the                  to                 as                               towith        automatically        -                  access                instantiate.Converts                                                                               one                                                                                           facade                                                                                                                              for                                                                                           a                                                                                                     subsystem.                                  clients                                     clients           functionality.                                        and                              instantiation                      interface  Adapter                   defer                                            requests,                    parameterize                                     log                                                                    interface                   class             another          a                           or          into                                                              unified                          together                            queue                                    a      class  a                   work                                                                                                                                      An                                                                                             adapter                                                                                            wraps                                                                                             an                                                                                                                        object                       requests,                                                  Provides                             -                                         operations.                  subclasses.classes                        of                                                                   subsystem.         Lets                                                          in a                          Facade                            undoable                          because    expect.                                                                                                         to                                                                                  change                                                                                                                                                 its                                                                                                                         interface,                                                                                                 a                                                     interfaces                     support                 otherwise                                  of                                                                     interface                                       set                          a         couldn’t                               to                                                             higher-level   that                                  a                                                      to use.                                                                                             decorator                                                                                           wraps                                                                                            an                                                                                                                      object                  interfaces.                                               defines                                                                    easier                                   Facade     incompatible                                                      subsystem                                          the                                                                                                         to                                                                                 add                                                                             new                                                                                                      behaviors                                                                                                and                                        makes                                  that
                                                                                                             responsibilities, and a facade
                                                                                            “wraps” a set of objects to
                                                                                                               simplify.


272      Chapter 7


---

## PDF page 311

the adapter and facade patterns

          Design Patterns Crossword
                       Yes, it’s another crossword. All of the solution words are
                   from this chapter.


                                                                   1             2

                                                          3

                               4        5


                           6             7                          8


                                                                                                                     9

                                                                                 10


                      11

                                                                                          12            13

                           14                                                                                    15

                                                                            16

             17                                  18


                  19


ACROSS                          DOWN
1. True or false? Adapters can wrap only one object.            2. Decorator called Adapter this (three words).
5. An Adapter __________ an interface.                        3. One advantage of Facade.
6. Movie we watched (five words).                              4. Principle that wasn't as easy as it sounded (two words).
10. If in Britain, you might need one of these (two words).      7. A __________ adds new behavior.
11. Adapter with two roles (two words).                          8. Masquerading as a Duck.
14. Facade still ________ low-level access.                     9. Example that violates the Principle of Least
15. Ducks do it better than Turkeys.                       Knowledge: System.out.__________.
16. Disadvantage of the Principle of Least Knowledge:        12. No movie is complete without this.
too many __________.                                      13. Adapter client uses the __________ interface.
17. A __________ simplifies an interface.                     18. An Adapter and a Decorator can be said to ________
                                                  an object.19. New American dream (two words).


                                                                       you are here 4      273


---

## PDF page 312

exercise solutions


                                                              Let’s say we also need an Adapter that converts a Duck to a
                                                      Turkey. Let’s call it DuckAdapter. Here’s our solution:
                                                Now we are adapting Turkeys to Ducks, so    public class DuckAdapter implements Turkey {                                                     we implement the Turkey interface.       Duck duck;
       Random rand;                                                    We stash a reference to the Duck we are adapting.       public DuckAdapter(Duck duck) {
           this.duck = duck;                                                We also create a random object; take a look at the           rand = new Random();                                                                     fly() method to see how it is used.       }
       public void gobble() {
           duck.quack();                   A gobble just becomes a quack.
       }
       public void fly() {
           if (rand.nextInt(5) == 0) {           Since Ducks fly a lot longer than Turkeys,
                duck.fly();                     we decided to only fly the Duck on average
           }                                           one of five times.
       }
   }


                                  Do either of these classes violate the Principle of Least
                                       Knowledge? Why or why not?
    public House {                                                  Violates the Principle of Least Knowledge!        WeatherStation station;                           You are calling the method of an object
        // other methods and constructor                   returned from another call.
        public float getTemp() {
             return station.getThermometer().getTemperature();
        }
   }
    public House {
         WeatherStation station;        // other methods and constructor                                  Doesn’t violate Principle of        public float getTemp() {                                         Least Knowledge! This seems
             Thermometer thermometer = station.getThermometer();       like hacking our way around
             return getTempHelper(thermometer);                        the principle. Has anything
        }                                                                                         really changed since we                                                                                               just moved out the call to
        public float getTempHelper(Thermometer thermometer) {         another method?
            return thermometer.getTemperature();
        }
   }


274      Chapter 7


---

## PDF page 313

the adapter and facade patterns


                  You’ve seen how to implement an adapter that adapts an Enumeration to an Iterator; now write
                 an adapter that adapts an Iterator to an Enumeration.

               public class IteratorEnumeration implements Enumeration<Object> {
                   Iterator<?> iterator;
Notice we keep the                   public IteratorEnumeration(Iterator<?> iterator) {type parameter                       this.iterator = iterator;generic so this will
work for any type     }
 of object.                   public boolean hasMoreElements() {
                       return iterator.hasNext();
                  }
                   public Object nextElement() {
                       return iterator.next();
                  }
              }


                    SOlUTion
             Match each pattern with its intent:

           Pattern                             Intent

                                           Converts one interface to
             Decorator                                             another

            Adapter                                                Doesn’t alter the interface,
                                             but adds responsibility
            Facade
                                     Makes an interface simpler


                                                                   you are here 4      275


---

## PDF page 314

crossword puzzle solution

         Design Patterns Crossword Solution


                                                                        1             2                                                F  A  L  S  E
                                                               3                                   D               I
                                    4        5                           L     C O N  V  E  R  T  S   M
                       E                 C                P
                               6             7                          8                    R  A  I  D  E  R  S O  F  T H  E  L O  S  T A  R  K
                     S     E         U    U        E
                                                                                                                         9                      T     C             P     R         P                           P
                                                                                     10                        K    O            L     K       A  C  A  D A  P  T  E  R
                  N     R            I     E       S                         I
                           11                T W O W A  Y      N     Y       S                 N
                                                                                              12            13              W    T          G            T      P       T       T
                               14                                                                                    15                 A  L  L O W S                H    O      A     F  L  Y
                                                                                 16                       E     R             W  R  A  P  P  E  R  S    N
                  17                                  18            F  A  C  A  D  E    W               O     C       G
                      G          R                U    O        E
                      19            H O M  E  T H  E  A  T  E  R          G     R       T
                                          P                H    N

    A                            D


276      Chapter 7
