# 5 the Singleton Pattern: One-of-a-Kind Objects

_Extracted from PDF pages 207-228. Text only; images and diagrams are not embedded._


---

## PDF page 207

5 the Singleton Pattern
     One-of-a-KindObjects


                                                       You talkin’ to me or the car?
                                                        Oh, and when can I get my oven
        I tell ya she’s ONE                                    mitt back?
  OF A KIND. Look at the
    lines, the curves, the body,
    the headlights!


   Our next stop is the Singleton Pattern, our ticket to creating one-
    of-a-kind objects for which there is only one instance, ever. You might
     be happy to know that of all patterns, the Singleton is the simplest in terms of its class diagram;
       in fact, the diagram holds just a single class! But don’t get too comfortable; despite its simplicity
      from a class design perspective, it’s going to require some deep object-oriented thinking in its
      implementation. So put on that thinking cap, and let’s get going.


                                                                           this is a new chapter      169


---

## PDF page 208

one and only one


                      What is this? An
                             entire chapter about
                       how to instantiate just
                   ONE object?


                                                                 That’s one and ONLY
                                          ONE object.


           Developer: What use is that?
          Guru: There are many objects we only need one of: thread pools, caches, dialog boxes, objects
              that handle preferences and registry settings, objects used for logging, and objects that act as
            device drivers to devices like printers and graphics cards. In fact, for many of these types of
             objects, if we were to instantiate more than one we’d run into all sorts of problems like incorrect
           program behavior, overuse of resources, or inconsistent results.
           Developer: Okay, so maybe there are classes that should only be instantiated once, but do I
          need a whole chapter for this? Can’t I just do this by convention or by global variables? You know,
               like in Java, I could do it with a static variable.
          Guru: In many ways, the Singleton Pattern is a convention for ensuring one and only one object
                is instantiated for a given class. If you’ve got a better one, the world would like to hear about it;
            but remember, like all patterns, the Singleton Pattern is a time-tested method for ensuring only
          one object gets created. The Singleton Pattern also gives us a global point of access, just like a
             global variable, but without the downsides.
           Developer: What downsides?
          Guru: Well, here’s one example: if you assign an object to a global variable, then that object
            might be created when your application begins. Right? What if this object is resource intensive
          and your application never ends up using it? As you will see, with the Singleton Pattern, we can
            create our objects only when they are needed.
           Developer: This still doesn’t seem like it should be so difficult.
          Guru: If you’ve got a good handle on static class variables and methods as well as access
             modifiers, it’s not. But, in either case, it is interesting to see how a Singleton works, and, as
            simple as it sounds, Singleton code is hard to get right. Just ask yourself: how do I prevent more
            than one object from being instantiated? It’s not so obvious, is it?


170      Chapter 5


---

## PDF page 209

the singleton pattern

The Little Singleton
A small Socratic exercise in the style of The Little Lisper

 How would you create a single object?                     new MyObject();


 And, what if another object wanted to create a                    Yes, of course.
 MyObject? Could it call new on MyObject again?


 So as long as we have a class, can we always                       Yes. Well, only if it’s a public class.
 instantiate it one or more times?


 And if not?                                                      Well, if it’s not a public class, only classes in the
                                                     same package can instantiate it. But they can still
                                                                        instantiate it more than once.


 Hmm, interesting.                                       No, I’d never thought of it, but I guess it makes
                                                                  sense because it is a legal definition. Did you know you could do this?

   public MyClass {

      private MyClass() {}

   }


 What does it mean?                                                     I suppose it is a class that can’t be instantiated
                                                            because it has a private constructor.


 Well, is there ANY object that could use                Hmm, I think the code in MyClass is the only
 the private constructor?                                    code that could call it. But that doesn’t make
                                                much sense.


                                                                       you are here 4      171


---

## PDF page 210

creating a singleton


 Why not ?                                                Because I’d have to have an instance of the
                                                                           class to call it, but I can’t have an instance
                                                            because no other class can instantiate it. It’s
                                                         a chicken-and-egg problem: I can use the
                                                                 constructor from an object of type MyClass,
                                                             but I can never instantiate that object because
                                                    no other object can use “new MyClass()”.

 Okay.  It was just a thought.                               MyClass is a class with a static method. We can call
                                                                the static method like this: What does this mean?
                                                   MyClass.getInstance();
  public MyClass {

     public static MyClass getInstance() {
     }
  }


 Why did you use MyClass instead of                             Well, getInstance() is a static method; in other
 some object name?                                           words, it is a CLASS method. You need to use the
                                                                           class name to reference a static method.

 Very interesting. What if we put things together?             Wow, you sure can.
 Now can I instantiate a MyClass?

  public MyClass {
      private MyClass() {}
      public static MyClass getInstance() {
          return new MyClass();
      }
  }

 So, now can you think of a second way to instantiate          MyClass.getInstance();
 an object?

 Can you finish the code so that only ONE instance               Yes, I think so...
 of MyClass is ever created?
                                                                                         (You’ll find the code on the next page.)

172      Chapter 5


---

## PDF page 211

the singleton pattern

Dissecting the classic Singleton
Pattern implementation
                          Let’s rename                astatic                                                             our                                                        have                                          Singleton.          We                        MyClass to                                                tohold                                                                  variable   ofthe               If you’re just                                                                    instance                                                  one  Singleton.   public class Singleton {                                                                  class                      theflippingbook,throughdon’t
       private static Singleton uniqueInstance;                                    blindly type in this
                                                                                            code; you’ll see it
       // other useful instance variables here                        is                                                   Our constructor               haslatera infewtheissueschapter.                                                             declared private; only       private Singleton() {}                                                                 Singleton can instantiate
                                                                  this class!       public static Singleton getInstance() {
           if (uniqueInstance == null) {          The getInstance() method
               uniqueInstance = new Singleton();   gives us a way to instantiate
           }                                            the class and also to return
           return uniqueInstance;                    an instance of it.
       }
       // other useful methods here
   }                                         Of course, Singleton is a normal                                                                                class; it has other useful instance                                                                        variables and methods.
           Code Up Close
                                                                                            is null, then we                                                     If uniqueInstance                         uniqueInstance holds our ONE       haven’t created the instance yet...
                          instance; remember, it is a                                              ...and, if it doesn’t exist, we
                         static variable.                                                  instantiate Singleton through
                                                                                                    its private constructor and
                                                                                                assign it to uniqueInstance. Note
                                                                            that if we never need the
          if (uniqueInstance == null) {                         instance, it never gets created;
                                                                                            this is lazy instantiation.              uniqueInstance = new Singleton();
          }                                                                  If uniqueInstance wasn’t null,
          return uniqueInstance;                             then it was previously created.                                                                We just fall through to the
                             By the time we hit this code, we            return statement.
                                     have an instance and we return it.


                                                                       you are here 4      173


---

## PDF page 212

interview with singleton


                      Patterns Exposed
                                This week’s interview:
                            Confessions of a Singleton


   HeadFirst: Today we are pleased to bring you an     HeadFirst: So, if we may ask, how do you know
    interview with a Singleton object. Why don’t you         there is only one of you? Can’t anyone with a new
   begin by telling us a bit about yourself?                 operator create a “new you”?
   Singleton: Well, I’m totally unique; there is just one    Singleton: Nope! I’m truly unique.
    of me!                                                 HeadFirst: Well, do developers swear an oath not to
   HeadFirst: One?                                          instantiate you more than once?
   Singleton: Yes, one. I’m based on the Singleton       Singleton: Of course not. The truth be told…well,
    Pattern, which ensures that at any time there is only       this is getting kind of personal but…I have no public
   one instance of me.                                       constructor.
   HeadFirst: Isn’t that sort of a waste? Someone took    HeadFirst: NO PUBLIC CONSTRUCTOR! Oh,
   the time to develop a full-blown class and now all we      sorry, no public constructor?
   can get is one object out of it?                                                  Singleton: That’s right. My constructor is declared
   Singleton: Not at all! There is power in ONE. Let’s     private.
   say you have an object that contains registry settings.                                                 HeadFirst: How does that work? How do you EVER   You don’t want multiple copies of that object and its                                                              get instantiated?    values running around—that would lead to chaos.
   By using an object like me you can ensure that every     Singleton: You see, to get a hold of a Singleton
    object in your application is making use of the same      object, you don’t instantiate one, you just ask for
    global resource.                                  an instance. So my class has a static method called
                                                                 getInstance(). Call that, and I’ll show up at once, ready   HeadFirst: Tell us more…                                                              to work. In fact, I may already be helping other objects
   Singleton: Oh, I’m good for all kinds of things.       when you request me.
   Being single sometimes has its advantages, you know.                                                  HeadFirst: Well, Mr. Singleton, there seems to be a   I’m often used to manage pools of resources, like                                                                        lot under your covers to make all this work. Thanks   connection or thread pools.                                                                  for revealing yourself and we hope to speak with you
   HeadFirst: Still, only one of your kind? That sounds   again soon!
    lonely.
   Singleton: Because there’s only one of me, I do keep
    busy, but it would be nice if more developers knew
  me—many developers run into bugs because they have
    multiple copies of objects floating around they’re not
   even aware of.


174      Chapter 5


---

## PDF page 213

the singleton pattern

The Chocolate Factory

Everyone knows that all modern chocolate factories have computer-controlled
chocolate boilers. The job of the boiler is to take in chocolate and milk, bring them
to a boil, and then pass them on to the next phase of making chocolate bars.
Here’s the controller class for Choc-O-Holic, Inc.’s industrial strength Chocolate
Boiler. Check out the code; you’ll notice they’ve tried to be very careful to ensure
that bad things don’t happen, like draining 500 gallons of unboiled mixture, or
filling the boiler when it’s already full, or boiling an empty boiler!
 public class ChocolateBoiler {
     private boolean empty;
     private boolean boiled;
                                                   This code is only started     privatepublic  ChocolateBoiler() {                                              when the boiler is empty!         empty = true;
         boiled = false;
     }                                                     To fill the boiler it must be     public void fill() {                               empty, and, once it’s full, we         if (isEmpty()) {                               set the empty and boiled flags.             empty = false;
             boiled = false;
             // fill the boiler with a milk/chocolate mixture
         }
     }
     public void drain() {                                                                To drain the boiler, it must be full         if (!isEmpty() && isBoiled()) {                                                                  (non-empty) and also boiled. Once it is             // drain the boiled milk and chocolate                                                                           drained, we set empty back to true.             empty = true;
         }
     }
     public void boil() {
         if (!isEmpty() && !isBoiled()) {                                                           To boil the mixture, the boiler             // bring the contents to a boil                                                                  has to be full and not already             boiled = true;
         }                                                               boiled. Once it’s boiled, we set
     }                                                     the boiled flag to true.
     public boolean isEmpty() {
         return empty;
     }
     public boolean isBoiled() {
         return boiled;
     }
 }

                                                                       you are here 4      175


---

## PDF page 214

chocolate boiler singleton


              Choc-O-Holic has done a decent job of ensuring bad things don’t happen,
                don’t you think? Then again, you probably suspect that if two ChocolateBoiler
               instances get loose, some very bad things can happen.
          How might things go wrong if more than one instance of ChocolateBoiler is
              created in an application?


                                      Can you help Choc-O-Holic improve their ChocolateBoiler class
                                        by turning it into a Singleton?

           public class ChocolateBoiler {
               private boolean empty;
               private boolean boiled;


                        ChocolateBoiler() {
                   empty = true;
                   boiled = false;
               }


               public void fill() {
                   if (isEmpty()) {
                      empty = false;
                      boiled = false;
                      // fill the boiler with a milk/chocolate mixture
                   }
               }
               // rest of ChocolateBoiler code...
           }


176      Chapter 5


---

## PDF page 215

the singleton pattern

Singleton Pattern defined
Now that you’ve got the classic implementation of Singleton
 in your head, it’s time to sit back, enjoy a bar of chocolate,
and check out the finer points of the Singleton Pattern.
 Let’s start with the concise definition of the pattern:


        The Singleton Pattern ensures a class has only one
             instance, and provides a global point of access to it.


No big surprises there. But let’s break it down a bit more:

      What’s really going on here? We’re taking a class and letting it manage a single
      instance of itself. We’re also preventing any other class from creating a new
      instance on its own. To get an instance, you’ve got to go through the class itself.
      We’re also providing a global access point to the instance: whenever you need
     an instance, just query the class and it will hand you back the single instance.
     As you’ve seen, we can implement this so that the Singleton is created in a lazy
      manner, which is especially important for resource-intensive objects.


Okay, let’s check out the class diagram:
                         is static,                                       The uniqueInstance              method     so you                                                       class variable holds our                    method,     getInstance()                   classThe              it’s a                      method                                               one and only instance      means          this which          access                            using                                           of Singleton.                   code can convenientlyin your                              just as                        Singleton      anywhere       That’s from                     but                static uniqueInstance                             variable,   Singleton.getInstance().a global          accessing                             instantiation                     // Other useful Singleton data...   easy as                    like lazy          benefits  we get       the Singleton.                                           static getInstance()   from                                                                                                               // Other useful Singleton methods...
                                                                           the Singleton                                        A class implementing                                                              Pattern is more than a Singleton; it                                                                                                   class with its                                                                                      is a general-purpose                                                       own set of data and methods.

                                                                       you are here 4      177


---

## PDF page 216

threads are a problem

      PAHershey,
Houston, we have a problem...

It looks like the Chocolate Boiler has let us down; despite
the fact we improved the code using the classic Singleton
Pattern, somehow the Chocolate Boiler’s fill() method was
able to start filling the boiler even though a batch of milk
and chocolate was already boiling! That’s 500 gallons of
spilled milk (and chocolate)! What happened!?


           We don’t know what happened! The new Singleton
                code was running fine. The only thing we can think
                of is that we just added some optimizations to
                the Chocolate Boiler Controller that makes use of
                     multiple threads.


                                     Could the addition of threads have caused
                                           this? Isn’t it the case that once we’ve set the
                                      uniqueInstance variable to the sole instance
                                           of ChocolateBoiler, all calls to getInstance()
                                      should return the same instance? Right?


178      Chapter 5


---

## PDF page 217

the singleton pattern
     BE the JVM
        We have two threads, each executing this code. Your job is to play the JVM
          and determine whether there is a case in which two threads might get a hold
            of different boiler objects. Hint:
          you really just need to look at the                                                  ChocolateBoiler boiler =
                  sequence of operations in the                                                          ChocolateBoiler.getInstance();                      getInstance() method and                                                  boiler.fill();                       the value of uniqueInstance                                                  boiler.boil();                       to see how they might                                                  boiler.drain();                      overlap. Use the code
           magnets to help you study how the
           code might interleave to create two boiler objects.

public static ChocolateBoiler           Make sure you check your answer on
       getInstance() {                  page 188 before continuing!
   if (uniqueInstance == null) {
      uniqueInstance =              Thread                   Thread        Value of
          new ChocolateBoiler();                                  One                 Two   uniqueInstance
   }
   return uniqueInstance;

 }


                                                                      you are here 4      179


---

## PDF page 218

multithreading and singleton

Dealing with multithreading

Our multithreading woes are almost trivially fixed by making
getInstance() a synchronized method:

    public class Singleton {
        private static Singleton uniqueInstance;                                                                                   keyword to                                                                                synchronized                                               By adding the                                                                               force every thread to                                                              we        //           other                 useful instance                                 variables here        getInstance(),                                                                                     the                                                                                      enter                                                                                can                                                                                         it                                                                            before                                                                    turn                                                                               its                                                               wait                                                                             may                                                                                     threads                                                                      two                                                                                                                   is, no                                                           That                                                              method.                                                                                                   time.                                                                                 same                                                                            the                                                                       at        private                Singleton()                            {}                                                                 method                                                               the                                                              enter
        public static synchronized Singleton getInstance() {
            if (uniqueInstance == null) {
                uniqueInstance = new Singleton();
            }
            return uniqueInstance;
        }

        // other useful methods here
    }

                                                  I agree this fixes the
                                                       problem. But synchronization
                                                                      is expensive; is this an issue?


            Good point, and it’s actually a little worse than you make
                  out: the only time synchronization is relevant is the first time
               through this method. In other words, once we’ve set the
                uniqueInstance variable to an instance of Singleton, we have
             no further need to synchronize this method. After the first time
                through, synchronization is totally unneeded overhead!


180      Chapter 5


---

## PDF page 219

the singleton pattern

Can we improve multithreading?

     For most Java applications, we obviously need to ensure that the Singleton works in the
     presence of multiple threads. But it’s expensive to synchronize the getInstance() method,
     so what do we do?
     Well, we have a few options...

    1. Do nothing if the performance of getInstance() isn’t critical
    to your application.
     That’s right; if calling the getInstance() method isn’t causing substantial overhead for your
      application, forget about it. Synchronizing getInstance() is straightforward and effective.
      Just keep in mind that synchronizing a method can decrease performance by a factor
      of 100, so if a high-traffic part of your code begins using getInstance(), you may have to
      reconsider.

    2. Move to an eagerly created instance rather than a lazily
    created one.
       If your application always creates and uses an instance of the Singleton, or the overhead
      of creation and runtime aspects of the Singleton isn’t onerous, you may want to create
     your Singleton eagerly, like this:

         public class Singleton {                                                                    Go ahead and create an
                                                                                                   instance of Singleton            private static Singleton uniqueInstance = new Singleton();                                                                                                        in a static initializer.
                                                                                       This code is guaranteed            private Singleton() {}                                          to be thread safe!

            public static Singleton getInstance() {                                                                           an                                                                          got                return uniqueInstance;                         We’ve already                                                                                                                    it.                                                                                     return                                                                            so just            }                                                                instance,
        }


     Using this approach, we rely on the JVM to create the unique instance of the Singleton
    when the class is loaded. The JVM guarantees that the instance will be created before
     any thread accesses the static uniqueInstance variable.


                                                                       you are here 4      181


---

## PDF page 220

double-checked locking

3.  Use “double-checked locking” to reduce the use of
synchronization in getInstance().
With double-checked locking, we first check to see if an instance is created, and if not, THEN
we synchronize. This way, we only synchronize the first time through, just what we want.
Let’s check out the code:

   public class Singleton {
       private volatile static Singleton uniqueInstance;

       private Singleton() {}
       public static Singleton getInstance() {                   Check for an instance and
           if (uniqueInstance == null) {                            if there isn’t one, enter a                                                                               synchronized block.               synchronized (Singleton.class) {
                   if (uniqueInstance == null) {
                                                                        Note we only synchronize                       uniqueInstance = new Singleton();                                                                              the first time through!                  }
              }                                                                 Once in the block, check again and           }                                                             if it’s still null, create an instance.           return uniqueInstance;
       }                                         The volatile keyword ensures that multiple threads
   }                                               handle the uniqueInstance variable correctly when it
                                                                             is being initialized to the Singleton instance.

If performance is an issue in your use of the getInstance() method, then this method of
implementing the Singleton can drastically reduce the overhead.

                                               locking doesn’t work in                             Double-checked
                           Java 1.4 or earlier!
                                                        an old version                                                            using                                                          If for some reason you’re                                                                             1.4 and                                                            Java version                                                                in                                       of Java, unfortunately,                     of                                                            implementations                                                 earlier, many JVMs contain                                                                                        for                                                                 synchronization                                                  improper                                                 allow                                               that                         the volatile keyword                                                  JVM earlier than Java                                              must use a                                           you                                                                         If                                             locking.                        double-checked                        your Singleton.                                                implementing                              5, consider other methods of


182      Chapter 5


---

## PDF page 221

the singleton pattern

Meanwhile, back at the Chocolate Factory...

While we’ve been off diagnosing the multithreading problems, the chocolate boiler
has been cleaned up and is ready to go. But first, we have to fix the multithreading
problems. We have a few solutions at hand, each with different tradeoffs, so which
solution are we going to employ?


                                                For each solution, describe its applicability to the
                                          problem of fixing the Chocolate Boiler code:


             Synchronize the getInstance() method:


           Use eager instantiation:


            Double-checked locking:


Congratulations!

At this point, the Chocolate Factory is a happy customer and Choc-O-Holic was glad to
have some expertise applied to their boiler code. No matter which multithreading solution
you applied, the boiler should be in good shape with no more mishaps. Congratulations—
not only have you managed to escape 500 lbs of hot chocolate in this chapter, but you’ve
also been through all the potential problems of the Singleton Pattern.

                                                                       you are here 4      183


---

## PDF page 222

q&a about singleton


      For such a simple pattern                And reflection, and serialization/        One problem with subclassing aQ:               Q:              A:consisting of only one class, Singleton       deserialization?                               Singleton is that the constructor is private.
sure seems to have some problems.                                               You can’t extend a class with a private
                                                                                                     constructor. So, the first thing you’ll have                                                     Yes, reflection and serialization/                 A:                                               to do is change your constructor so that it’s      Well, we warned you up front! But          deserialization can also present problemsA:                                                                                               public or protected. But then, it’s not really adon’t let the problems discourage you; while     with Singletons. If you’re an advanced Java                                                                                              Singleton anymore, because other classes implementing Singletons correctly can be       user using reflection, serialization, and                                                                                  can instantiate it. tricky, after reading this chapter you’re now       deserialization, you’ll need to keep that in mind.
 well informed on the techniques for creating                                                                                                                                                             If you do change your constructor, there’sSingletons and should use them wherever                                                        Earlier we talked about the loose       another issue. The implementation ofyou need to control the number of instances  Q:                                          coupling principle. Isn’t a Singleton          Singleton is based on a static variable, soyou’re creating.                                                violating this? After all, every object in             if you do a straightforward subclass, all of
                                         our code that depends on the Singleton      your derived classes will share the same
      Can’t I just create a class in which      is going to be tightly coupled to that very     instance variable. This is probably not whatQ:
 all methods and variables are defined as     specific object.                           you had in mind. So, for subclassing to work,
static? Wouldn’t that be the same as a                                                   implementing a registry of sorts is required
Singleton?                                                    Yes, and in fact this is a common            in the base class.                 A:                                                      criticism of the Singleton Pattern. The
      Yes, if your class is self-contained and     loose coupling principle says to “strive for       But what are you really gaining fromA:doesn’t depend on complex initialization.        loosely coupled designs between objects       subclassing a Singleton? Like most patterns,
However, because of the way static              that interact.” It’s easy for Singletons to         Singleton is not necessarily meant to be a
 initializations are handled in Java, this can       violate this principle: if you make a change       solution that can fit into a library. In addition,
get very messy, especially if multiple classes     to the Singleton, you’ll likely have to make a     the Singleton code is trivial to add to any
are involved. Often this scenario can result     change to every object connected to it.           existing class. Last, if you are using a large
 in subtle, hard-to-find bugs involving order                                            number of Singletons in your application,
 of initialization. Unless there is a compelling             I’ve always been taught that a class   you should take a hard look at your design.                 Q:need to implement your “singleton” this way,    should                                          do one thing and one thing only.      Singletons are meant to be used sparingly.
 it’s far better to stay in the object world.        For a class to do two things is considered
                                     bad OO design. Isn’t a Singleton violating                  I still don’t totally understand                                  Q:                                                  this too?                           why                                                                                              global variables are worse than a     What about class loaders? IQ:heard there’s a chance that two class                                                     Singleton.
                                            You would be referring to the Single loaders could each end up with their own A:
instance of Singleton.                          Responsibility Principle, and yes, you are              In Java, global variables are basically                                                    correct: the Singleton is responsible not only A:                                                                                                                static references to objects. There are a
                                                         for managing its one instance (and providing    couple of disadvantages to using global      Yes, that is true as each class loaderA:defines a namespace. If you have two or        global access), but also for whatever            variables in this manner. We’ve already
more class loaders, you can load the same        its main role is in your application. So,         mentioned one: the issue of lazy versus
class multiple times (once in each class          certainly you could argue it is taking on two     eager instantiation. But we need to keep
 loader). Now, if that class happens to be a       responsibilities. Nevertheless, it isn’t hard to      in mind the intent of the pattern: to ensure
Singleton, then since we have more than       see that there is utility in a class managing      only one instance of a class exists and to
one version of the class, we also have more       its own instance; it certainly makes the          provide global access. A global variable can
 than one instance of Singleton. So, if you are    overall design simpler. In addition, many        provide the latter, but not the former. Global
 using multiple class loaders and Singletons,     developers are familiar with the Singleton        variables also tend to encourage developers
be careful. One way around this problem is      Pattern as it is in wide use. That said, some      to pollute the namespace with lots of global
 to specify the class loader yourself.            developers do feel the need to abstract out      references to small objects. Singletons don’t
                                                the Singleton functionality.                   encourage this in the same way, but can be
                                                                                abused nonetheless.
                                                                                            I wanted to subclass my Singleton                 Q:
                                          code, but I ran into problems. Is it okay to
                                         subclass a Singleton?

184      Chapter 5


---

## PDF page 223

the singleton pattern


                       I just realized...I think we can
                           solve a lot of the problems with
                         Singleton by using an enum. Is
                         that right?


                       Ah, good idea!
                       Many of the problems we’ve discussed—worrying about
                                 synchronization, class loading issues, reflection, and serialization/
                                   deserialization issues—can all be solved by using an enum to create
                              your Singleton. Here’s how you’d do that:
                            public enum Singleton {
                                UNIQUE_INSTANCE;
                                // more useful fields here
                           }
                            public class SingletonClient {
                                   public static void main(String[] args) {
                                         Singleton singleton = Singleton.UNIQUE_INSTANCE;
                                         // use the singleton here
                                  }
                           }
                               Yep, that’s all there is to it. Simplest Singleton ever, right? Now, you
                             might be asking, why did we go through all that earlier with creating
                             a Singleton class with a getInstance() method and then synchronizing,
                           and so on? We did that so you really, truly understand how Singleton
                                works. Now that you know, you can go off and use enum wheneverAnd back in the old days,                            you need a Singleton, and still be able to ace that Java interview ifwhen we had to walk to                                the question pops up: “How do you implement a Singleton without school, uphill, in the snow, in              Java didn’t     using enum?” both directions,
 have enums.


        Can you rework Choc-O-Holic to use an enum? Give it a try.


                                                                       you are here 4      185


---

## PDF page 224

your design toolbox

           Tools for your Design Toolbox
                You’ve now added another pattern to your toolbox.
                 Singleton gives you another method of creating
                objects—in this case, unique objects.                          The Singleton Pattern
                                                                                        ensures you have at most
                                                                                 one instance of a class in
                                                                                            your application.
                                                                  The Singleton Pattern also                  Basics         OO                                                           provides a global access
         Principles      Abstraction   OO                       Encapsulation                                 pointJava’stoimplementationthat instance.                 what varies.          Encapsulate                  Polymorphism                                                     of the Singleton Pattern                         over inheritance.                                               makes use of a private         Favor composition                                      Inheritance                                                     constructor, a static                        interfaces, not                                                                                 method combined with a          Program to             implementations.                                                                                        static variable.                                      designs                             coupled                         loosely                                                                  Examine your performance            Strive for                        that interact.                     objects            between                                                                  and resource constraints                                       extension                     should be open for               Classes                                                                  and carefully choose an                              modification.                                                                                                  appropriate Singleton            but closed for
                       Do not                                                        implementation for                  on abstractions.             Depend                                        classes.                                                                                                multithreaded                                                                                                                    applications                        concrete              depend on                                                                                          (and we should                                  When you need to ensureofyoua class                                                           instance                                             only have one                                                     your application,                                               around                                consider all applications                                             running                                           multithreaded!).                                                             Singleton.                                       turn to the
                                                                  Beware of the double-
                                      algorithms,                       of     Patterns                          family                                                                                               implementation;                                                                                                                                                                                                                 it                                                                                                                                                     isn’t               a OO                                                                              checked locking                        one-to-many                 defines                a        -                            them                  defines          -                                an                               additional                          makes                             that   Strategy                    and                            so                                                                                               thread                                                                                                      safe                                                                                                                                 in                                                                                                              versions                   Attach                                 an                     one,            -                   -               each                         objects    Observer                                       algorithm                                Define                     -                                 Providedynamically.                                       its                between                Factory                               lets                                           one                            of     encapsulates                          object                                         all     Decorator                   an                                    buthas                 to                   Strategy                                          only                                                                                               before                                                                                           Java                                                                                                                         5.                              state,the              Method                                    families      dependency        Abstract                                     use                                         class                                                 it.object,                      a                     changes                           an                             that         Factory                 for          responsibilities                               flexibleEnsure      interchangeable.                        creatingclients                -                                   of                 a                                   without                           creating                              updated          one                  from                                          pointto                   for                        and           interface                   provide                               objects      when                                           class                                        global                                   extending                      a               objectSingleton              interface                           for                               which                                                                                    depedentnotified                are                                                                         Be                                                                                                            careful                                                                                                                                                                                                       if                                                                                              you                                                                                                             are                                                                                                                 using        Decoratorsindependently     vary                            provide               or                         decide                                          classes.                    and                          subclassing                                           lets            related               to       dependents                    subclasses                 instance                          concrete             let                           Method                     their          alternative                                                                                                        multiple                                                                                                           class                                                                                                                   loaders;                                                                                                                                             this                             it.Factory                  to             specifying                                   the        automatically                               to                 access                instantiate.           functionality.                                                                                              could                                                                                                       defeat                                                                                                             the                                                                                                                 Singleton                              instantiation                   defer         a class
                  subclasses.                                                                      implementation and result                                                                                                                   in multiple instances.
                                                                  You can use Java’s enums
                                                                                                            to simplify your Singleton
        As you’ve seen, despite its apparent simplicity, there are a lot of details            implementation.          involved in Singleton’s implementation. After reading this chapter,
         though, you’re ready to go out and use Singleton in the wild.

186      Chapter 5


---

## PDF page 225

the singleton pattern

        Design Patterns Crossword
                   Sit back, open that case of chocolate that you were sent for solving the
                multithreading problem, and have some downtime working on this
                      little crossword puzzle; all of the solution words are from this chapter.

                                                1                          2


        3                                                 4

                                                                  5        6


                                       7

                              8                                                     9

            10       11                         12


                                       13


                                                                                    14

            15


        16


ACROSS                          DOWN
 3. Company that produces boilers.                              1. Added to chocolate in the boiler.
 6. An incorrect implementation caused this to overflow.         2. Flawed multithreading approach if not using Java 5 or
 7. The Singleton Pattern has one.                                  later (two words).
10. To totally defeat the new constructor, we have to            3. It was “one of a kind.”
 declare the constructor __________.                            4. Multiple __________ can cause problems (two words).
12. The classic implementation doesn’t handle this.             5. If you don’t need to worry about lazy instantiation, you
13. Singleton provides a single instance and __________     can create your instance __________.
 (three words).                                                    8. One advantage over global variables: ________
14. An easy way to create Singletons in Java.                  creation.
15. The Singleton was embarrassed it had no public            9. Chocolate capital of the USA.
__________.                                                   11. Singleton ensures only one of these exists.
16. A Singleton is a class that manages an instance of
________.

                                                                       you are here 4      187


---

## PDF page 226

exercise solutions


          BE the JVM Solution


                       Thead                   Thead        Value of
                        One                 Two   uniqueInstance
   public static ChocolateBoiler                                    null
       getInstance() {
                                  public static ChocolateBoiler                                                                    null
                                      getInstance() {
                                                                          Uh oh, this  if (uniqueInstance == null) {                                                                                                           doesn’t look
                                                                    null             good!                                 if (uniqueInstance == null) {
      uniqueInstance =                                                                    <object1>          new ChocolateBoiler();
                                                                    <object1>         return uniqueInstance;

                                    uniqueInstance =                <object2>     Two different
                                        new ChocolateBoiler();                          objects are
                                                                                                          returned!                                                                    <object2>                                                                                  We have two                                     return uniqueInstance;                                                                                                            ChocolateBoiler
                                                                                                                               instances!!!


188      Chapter 5


---

## PDF page 227

the singleton pattern


                                Can you help Choc-O-Holic improve their ChocolateBoiler class
                                  by turning it into a Singleton?


public class ChocolateBoiler {
    private boolean empty;
    private boolean boiled;

    private static ChocolateBoiler uniqueInstance;

    private ChocolateBoiler() {
        empty = true;
        boiled = false;
    }

    public static ChocolateBoiler getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new ChocolateBoiler();
        }
        return uniqueInstance;
    }

    public void fill() {
        if (isEmpty()) {
            empty = false;
            boiled = false;
            // fill the boiler with a milk/chocolate mixture
        }
    }
   // rest of ChocolateBoiler code...
}


                                                                you are here 4      189


---

## PDF page 228

exercise solutions


                                           For each solution, describe its applicability to the
                                     problem of fixing the Chocolate Boiler code:

     Synchronize the getInstance() method:
      A straightforward technique that is guaranteed to work. We don’t seem to have
         any performance concerns with the chocolate boiler, so this would be a good choice.


     Use eager instantiation:
      We are always going to instantiate the chocolate boiler in our code, so statically initializing
       the instance would cause no concerns. This solution would work as well as the synchronized
       method, although perhaps be less obvious to a developer familar with the standard pattern.

     Double-checked locking:
       Given we have no performance concerns, double-checked locking seems like overkill.  In
        addition, we’d have to ensure that we are running at least Java 5.


                                         1                          2                   M              D
                               I             O
3                                                 4 C H O  C   -  O   -  H O  L  I  C         U
                                                           5        6 A                          K     L    S     B O  I  L  E  R
 R                          A    T     L
                                7                      C  L  A  S  S    A     E
                       8                                                     9                  L               S    T     C    H                                   Design
     10       11                         12     P  R  I  V A  T  E   M U  L  T  I  T H  R  E  A  D  I N  G
       N    Z             O     C     E     R           Patterns
                                13         S     Y    G  L O  B  A  L  A  C  C  E  S  S  P O  I N  T         T                   D     L     K    H          Crossword
                                                                             14        A                      E     L     E     E N U M
     15    C O N  S  T  R U  C  T O  R     Y    D     Y           Solution
          C                    S
16 I  T  S  E  L  F


190      Chapter 5
