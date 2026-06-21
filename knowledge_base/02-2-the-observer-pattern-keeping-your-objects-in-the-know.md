# 2: the Observer Pattern: Keeping your Objects in the Know

_Extracted from PDF pages 75-116. Text only; images and diagrams are not embedded._


---

## PDF page 75

2 the Observer Pattern
    Keepingyour
    ObjectsintheKnow

                                                 Hey Jerry, I’m notifying
                                                         everyone that the Patterns Group
                                                        meeting moved to Saturday night.
                                                     We’re going to be talking about the
                                                      Observer Pattern. That pattern is
                                                       the best! It’s the BEST, Jerry!


      You don’t want to miss out when something interesting
      happens, do you? We’ve got a pattern that keeps your objects in the
        know when something they care about happens. It’s the Observer Pattern. It is
        one of the most commonly used design patterns, and it’s incredibly useful. We’re
          going to look at all kinds of interesting aspects of Observer, like its one-to-many
           relationships and loose coupling. And, with those concepts in mind, how can you
          help but be the life of the Patterns Party?


                                                                            this is a new chapter      37


---

## PDF page 76

weather monitoring station

Congratulations!

Your team has just won the contract to build
Weather-O-Rama, Inc.’s next-generation,
internet-based Weather Monitoring Station.


                                 Weather-O-Rama, Inc.
                                                  Street                                100 Main                                    OK 45021                                                       Alley,                                   Tornado
                                     of Work                            Statement                                                    our next-generation,                                                 to build                                                  selected                            on being          Station!                       Congratulations       Monitoring                                Weather                    pending                                                            patent                        internet-based                                                                        conditions                                            based on our                                               will be                                                          weather                                       station             current              like                                                        We’d                                                    tracks                 The weather                                     which                                                                    pressure).                                        object,                                                                               display                                                 barometric                                                                      three                     WeatherData                                                               provides                                      humidity, and                                                 a simple                                                   that initially                                                     and                          (temperature,                                                                                statistics,                            an application                                                                           object                                                weather                          to create                    you                                             conditions,                                                      WeatherData                                                  as the                                  current                                              time                          elements:                                         in real                                 updated                                              measurements.                             forecast, all                                           recent                                                             Weather-O-                                most                                the                                                                       station.                                                     own                           acquires                  weather         their                                                                 write                                        expandable                                                         to                              an                                                                                 that                                            is                                       this                                                    developers                                                                                              it’s important                            Further,                                             other                                               So                                        allow                                                                   in.                                    to                                                            right                              wants                                         them                  Rama                                           plug                                 and                                                                     future.                                                       the                                                     in                                      displays                                          add                                                                     once                                              to                         weather                                                                   model:                                  be easy                                            will                                                                    business                                                             great                                        a                    new displays                                                                              for each                                               have                                   we                                                        them                                               thinks                                                         to charge                                                      intend                                     we                                                                  going to pay you                       Weather-O-Rama                                          hooked,                                             we are                                       are                                                                part:                                                        best                                                  for the                           the customers                            Now                                  they use.                               display                                          application.                                                               alpha                                       options.                           in stock                                                         design and                                                your                                         to seeing                                   forward                  We look
                                  Sincerely,


                            CEO                                      Hurricane,               source files!                            Johnny                                              WeatherData                                           attached                                    P.S. See the


38      Chapter 2


---

## PDF page 77

the observer pattern

The Weather Monitoring application overview

Let’s take a look at the Weather Monitoring application we need to deliver—both
what Weather-O-Rama is giving us, and what we’re going to need to build or
extend. The system has three components: the weather station (the physical device
that     acquires             the                 actual                     weather                                   data),                                     the WeatherData                                                        object                                                                      (that                                                                      tracks                                                                       the                                                                        data                                                                                                            differentcoming       from             the              Weather                          Station                           and updates                                             the displays),                                                and                                                              the                                                                     display                                                                              that                                                                                                    weather                                                           The user can view oneconditions,of threeshows       users            the               current                     weather                                 conditions:                                                                          the current                                                                                              displays:                                                                                                forecast.                                                                                        stats, or a


      Humidity                                                      displays           Current                                               pulls data    sensor device                                                                                  Conditions
                                                                                            Temp: 72°
                                                                                                          Humidity: 60
                                                                                                          Pressure:

 Temperature
 sensor device                                WeatherData
                                                      object
                   Weather Station
                                                                                   Display device
                                                          What we need to implement.     Pressure                    What Weather-O-Rama   sensor device                                            We’ll also need to integrate                                  is providing                                                   the WeatherData object with
                                                   the display.

The WeatherData object was written by Weather-O-Rama and knows how to talk
to the physical Weather Station to get updated weather data. We’ll need to adapt
the WeatherData object so that it knows how to update the display. Hopefully
Weather-O-Rama has given us hints for how to do this in the source code.
Remember, we’re responsible for implementing three different display elements:
Current Conditions (shows temperature, humidity, and pressure), Weather
Statistics, and a simple Forecast.
So, our job, if we choose to accept it, is to create an app
that uses the WeatherData object to update three displays
for current conditions, weather stats, and a forecast.


                                                                        you are here 4      39


---

## PDF page 78

weather data class

Unpacking the WeatherData class
Let’s check out the source code attachments that Johnny Hurricane,
the CEO, sent over. We’ll start with the WeatherData class:

      Here is our WeatherData class.
                                                                                    measurements                                                                         weather                                                                                                     respectively.                                                                                       pressure,                                 These three methods returnandthebarometricmost recent                                                         humidity,                                                                                    that the                                          temperature,                                                                                           just know                                                                we               WeatherData            for                                                                            data,                                                                             this                                                                    it gets                                        HOW                                                                                                Station.                                               now                                                    right                                                                            Weather                                             care                                                                      the                                                              from                            We don’t                                                                         info         getTemperature()                                                         updated                                                        gets                                                   object                                  WeatherData          getHumidity()                                                                   has updated values, the                                                   WeatherData                                               whenever          getPressure()               Note that                                                    method is called.        measurementsChanged()         measurementsChanged()

                // other methods
                                        /*
                                        * This method gets called
                                        * whenever the weather measurements
                                        * have been updated                   measurementsChanged()           at the                                anytime         looks                             called  Let’s                                        *                     gets                   again,                                for           which,                                   values   method,                      new                                         */                    obtains      WeatherData   the                         pressure.                                         public void measurementsChanged() {          humidity, and   temp,
                                            // Your code goes here
                                       }
            Our soon-to-be-
              implemented display.                                         WeatherData.java
                                                       It looks like Weather-O-Rama left a note in the comments to
                                          add our code here. So perhaps this is where we need to update
                                              the display (once we’ve implemented it)
                   Current
                   Conditions
                 Temp: 72°        So, our job is to alter the measurementsChanged()
                    Humidity: 60     method so that it updates the three displays for
                    Pressure:                           current conditions, weather stats, and forecast.


            Display device

40      Chapter 2


---

## PDF page 79

the observer pattern

Our Goal

We know we need to implement a display and then have the WeatherData
update that display each time it has new values, or, in other words, each time
the measurementsChanged() method is called. But how? Let’s think through
what we’re trying to acheive:

  ●  We know the WeatherData class has getter methods for
       three measurement values: temperature, humidity, and
       barometric pressure.

  ●  We know the measurementsChanged() method is called
      anytime new weather measurement data is available. (Again,
     we don’t know or care how this method is called; we just                                                                                                                                                     Weather
     know that it is called.)                                                                                                                        Stats
                                                                                                                                                                                 Avg. temp: 62°
                                                                                                                                                                                             Min. temp: 50°
  ●   We’ll need to implement three display elements that use the                                                    Max. temp: 78°
                                                                                                                                      Current
      weather data: a current conditions display, a statistics display,                  Conditions
                                                                                                                                     Temp: 72°
      and a forecast display. These displays must be updated as                          Humidity: 60
       often as the WeatherData has new measurements.                                         Pressure:               Display Two

  ●  To update the displays, we’ll add code to the                                                                                                                                                                      Forecast
      measurementsChanged() method.                                                Display One
                                                    TT
                                                    T
Stretch Goal
But let’s also think about the future—remember the constant in software
development? Change. We expect, if the Weather Station is successful, there                                    Display Three
will be more than three displays in the future, so why not create a marketplace
for additional displays? So, how about we build in:

  ●  Expandability—other developers may want to create new
      custom displays. Why not allow users to add (or remove)
      as many display elements as they want to the application?                 ?       Currently, we know about the initial three display types
       (current conditions, statistics, and forecast), but we expect a
       vibrant marketplace for new displays in the future.                                     Future displays


                                                                        you are here 4      41


---

## PDF page 80

first try with the weather station

Taking a first, misguided implementation
of the Weather Station

Here’s a first implementation possibility—as we’ve discussed, we’re going to add our code to
the measurementsChanged() method in the WeatherData class:

   public class WeatherData {
                                                           Here’s the measurementsChanged() method.       // instance variable declarations
                                                   And here are our code additions...
       public void measurementsChanged() {
           float temp = getTemperature();         First, we grab the most recent measurements by                                                                         calling the WeatherData’s getter methods. We assign           float humidity = getHumidity();                                                         each value to an appropriately named variable.           float pressure = getPressure();

           currentConditionsDisplay.update(temp, humidity, pressure);                                                                             Next we’re going to           statisticsDisplay.update(temp, humidity, pressure);                                                                                       update each display...
           forecastDisplay.update(temp, humidity, pressure);
      }
                                                                                        ...by calling its update method
                                                           and passing it the most recent       // other WeatherData methods here
                                                                 measurements.  }


                     Based on our first implementation, which of the following apply?
                     (Choose all that apply.)

     ❏  A. We are coding to concrete       ❏  D. The display elements don’t implement a
                 implementations, not interfaces.             common interface.
     ❏  B. For every new display we’ll need to   ❏  E. We haven’t encapsulated the part that
                    alter this code.                                  changes.
     ❏  C. We have no way to add (or remove)   ❏   F. We are violating encapsulation of the
                  display elements at runtime.                  WeatherData class.


42      Chapter 2


---

## PDF page 81

the observer pattern

What’s wrong with our implementation anyway?

Think back to all those Chapter 1 concepts and principles—which are we violating, and
which are we not? Think in particular about the effects of change on this code. Let’s work
through our thinking as we look at the code:

      public void measurementsChanged() {                                                          Let’s take another look...
          float temp = getTemperature();
                                                                                   Looks like an area of          float humidity = getHumidity();                                                                                                change. We need to          float pressure = getPressure();                                                                                                encapsulate this.
          currentConditionsDisplay.update(temp, humidity, pressure);
          statisticsDisplay.update(temp, humidity, pressure);
          forecastDisplay.update(temp, humidity, pressure);
      }
                                           At least we seem to be using a
                                               common interface to talk to the
        By coding to concrete                          display elements...they all have an
            implementations, we have no way             update() method that takes the
          to add or remove other display              temp, humidity, and pressure values.
            elements without making changes to
          the code.                                    What if we want to add or remove
                                                   displays at runtime? This looks
                                           hardcoded.
               Umm, I know I’m
           new here, but given that we
            are in the Observer Pattern
             chapter, maybe we should
             start using it?


                                           Good idea. Let’s take a look at
                                                         Observer, then come back and figure
                                                        out how to apply it to the Weather
                                                     Monitoring app.


                                                                        you are here 4      43


---

## PDF page 82

meet the observer pattern

Meet the Observer Pattern
You know how newspaper or magazine
subscriptions work:

   1  A newspaper publisher goes into business and begins
         publishing newspapers.

   2   You subscribe to a particular publisher, and every time
          there’s a new edition it gets delivered to you. As long as
        you remain a subscriber, you get new newspapers.

   3   You unsubscribe when you don’t want papers anymore,
        and they stop being delivered.

   4   While the publisher remains in business, people, hotels,
           airlines, and other businesses constantly subscribe and
         unsubscribe to the newspaper.


            No way we want to
              miss what’s going on in
               Objectville. Of course we
                subscribe.


44      Chapter 2


---

## PDF page 83

the observer pattern

Publishers + Subscribers = Observer Pattern

If you understand newspaper subscriptions, you pretty much
understand the Observer Pattern, only we call the publisher the
SUBJECT and the subscribers the OBSERVERS.
Let’s take a closer look:

                                                                 The observers have subscribed to
                                                                                         (registered with) the Subject
                                                                           to receive updates when the
                                                                                         Subject’s data changes.
                      When data in the Subject changes,                                      are notified.                        the observers
              object  The Subject
   manages some                      t                             c             data.   important                              2         Dog Obje
              2                                 2
    S      int t                             ct                                              at Obje     u     bject Objec           2            C
                      New data values are
                           communicated to the           t                                                   jec                            b                              observers in some form       Mouse O
                         when they change.                                                              Observer Objects

                         This object isn’t an     t                 so it doesn’t                             observer,        jec  DuckOb                        get notified when the                                data changes.                              Subject’s


                                                                        you are here 4      45


---

## PDF page 84

a day in the life of the observer pattern

A day in the life of the Observer Pattern


                                                                                                   ect                                                                                                           g Obj                                           me”      2               Do
    A Duck object comes along                                                                  int t
                                           jec      and tells the Subject that                        Subject Ob                                                                                          ct                                                                   Cat Obje      he wants to become an                                                            “register/subscribe       observer.
                                                                                ect                                              MouseObj                         t      Duck really wants in on the                                                 jec                                                                  Observers                           DuckOb        action; those ints Subject is
       sending out whenever its state
       changes look pretty interesting...


     The Duck object is now an                      2
                                                                                                   ect        official observer.                                           Dog Obj
                                        ject                     Subjecintt Ob
      Duck                is psyched...he’s                          on                             the
                                                                                         ct                                                     Duck Object   Cat Obje          list and                   is waiting with                            great
        anticipation for the next
        notification so he can get an int.
                                                                               ect                                              MouseObj

                                                                                                                                       Observers


                                                        8                 8
     The Subject gets a new                                           8        Dog Object
                                        ject           8      data value!             Subjecintt Ob                                                                          8
                                                                                         ct      Now Duck and all the rest of the                             Duck Object   Cat Obje
       observers get a notification that
       the Subject has changed.
                                                                               ect                                              MouseObj
                                                                                                                                         Observers


46      Chapter 2


---

## PDF page 85

the observer pattern


                                                 8
                                                                                          ect                                                      Dog Obj
                                   jectThe Mouse object asks to be                 Subjecintt Ob
removed as an observer.
                                                                                 ct                                               Duck Object   Cat Obje
The Mouse object has beengetting ints for ages and is tired                               “remove/unsubscribe                                                        me”of it, so he decides it’s time to                                t                                                                        ecstop being an observer.                              MouseObj
                                                                                                                            Observers


                                                8
                                                                                          ect                                                      Dog Obj
                                  jectMouse is outta here!                 Subjecintt Ob

                                                                                 ctThe Subject acknowledges the                              Duck Object   Cat Obje
Mouse’s request and removes him
from the set of observers.
                                         ect                      MouseObj

                                                                                                                            Observers


The Subject has another                         14                14
new int.                                                                 14         Dog Object
                                  ject           14                 Subjecintt ObAll the observers get another
notification,           except                   for                     the
                                                                                 ctMouse      who is            no longer                        included.                                               Duck Object   Cat Obje
Don’t tell anyone, but the Mouse
secretly misses those ints...
maybe he’ll ask to be an observer                                          ect                       MouseObjagain some day.
                                                                                                                            Observers


                                                                  you are here 4      47


---

## PDF page 86

five-minute drama

        Five-minute drama: a subject for observation
            In today’s skit, two enterprising software developers encounter a real
                live head hunter...

                                                   Uh, yeah, you and
        This is Lori. I’m looking                       everybody else, baby.
        for a Java development                        I’m putting you on my list of
         position. I’ve got five years                  Java developers. Don’t call
        of experience and...                           me, I’ll call you!


                                        2
                                                          Headhunter/Subject
 1


    Software                                                                                                          I’ll add you to the list—
  Developer #1                                                                                     you’ll know along with
                              Hi, I’m Jill. I’ve written                                                                                everyone else.
                         a lot of enterprise systems.
                        I’m interested in any job you’ve
                        got with Java development.


                                   4
    3

           Software                                  Subject
         Developer #2

48      Chapter 2


---

## PDF page 87

the observer pattern

5    Meanwhile, for Lori and Jill life goes       on; if a Java job comes along, they’ll get
       notified. After all, they are observers.               Thanks, I’ll send my
                                                   resume right over.


                                                                                This guy is a real jerk.
                                                        Who needs him. I’m
     Hey observers, there’s                                                            looking for my own job.
    a Java opening down at
    JavaBeans-R-Us. Jump on
        it! Don’t blow it!

                         Bwahaha, money in
                         the bank, baby!

                          7                                       Observer


                                                        Observer


  6
            Subject
                                                                         Arghhh!!! Mark my
                                                                  words, Jill, you’ll never
                                                            work in this town again if I
                                                               have anything to do with it. Jill lands her own job!                                                                     You’re off my call list!!!
                      You can take me
                         off your call list. I
                        found my own job!


 8
                                    9       Observer                                         Subject

                                                                      you are here 4      49


---

## PDF page 88

more five-minute drama

Two weeks later...


                                                   Jill’s loving life, and no longer an observer.
                                     She’s also enjoying the nice fat signing
                                   bonus that she got because the company
                                          didn’t have to pay a headhunter.


                            But what has become of our dear Lori? We
                             hear she’s beating the headhunter at his own
                             game. She’s not only still an observer, she’s
                              got her own call list now, and she is notifying
                            her own observers. Lori’s a subject and an
                             observer all in one.


50      Chapter 2


---

## PDF page 89

the observer pattern

The Observer Pattern defined

A newspaper subscription, with its publisher and subscribers, is a
good way to visualize the pattern.

In the real world, however, you’ll typically see the Observer
Pattern defined like this:

    The Observer Pattern defines a one-to-many
      dependency between objects so that when one
       object changes                          state, all                                of its dependents are        The Observer Pattern       notified            and updated                             automatically.
                                            defines a one-to-many
Let’s relate this definition to how we’ve been thinking about the                                              relationship between apattern:
                                                  set of objects.
           ONE-TO-MANY RELATIONSHIP
 Object       that                         When the state of one holds state
                                               object changes, all of its
              8                 8                                8        Dog Object             dependents are notified.
           ject           8    Subjecintt Ob                               8                                                                             Objects
                                                   ct                         Duck Object   Cat Obje


                                          ect                       MouseObj                                                                                       Dependent     Automatic update/notification                     Observers


The subject and observers define the one-to-many relationship. We
have one subject, who notifies many observers when something in the subject
changes. The observers are dependent on the subject—when the subject’s
state changes, the observers are notified.

As you’ll discover, there are a few different ways to implement the
Observer Pattern, but most revolve around a class design that includes
Subject and Observer interfaces.


                                                                        you are here 4      51


---

## PDF page 90

the observer pattern

The Observer Pattern: the Class Diagram
Let’s take a look at the structure of the Observer Pattern, complete with                All potential observers need
its Subject and Observer classes. Here’s the class diagram:                          to implement the Observer
                                                                                           interface. This interface has
                         Objects                 Each subject                just one method, update(),                                                      can have many            that is called when the                   interface. as          Subject                                                              observers.                   Subject’s state changes.     the             toregisterthemselves Here’s                   remove         interface     this               alsoto  use        and   observers              observers.                            <<interface>>                  observers              <<interface>>        being   from                                             Subject                                     Observer
                                                             registerObserver()                                        update()
                                                       removeObserver()
                                                             notifyObservers()


                                                     ConcreteSubject         subject                ConcreteObserver
                                                                registerObserver() {...}                                    update()
                                                         removeObserver() {...}                                                             // other Observer specific
                                                                notifyObservers() {...}                                methods A concrete subject always           the Subject  implements                                            getState()            In addition to  interface.                                              setState()  the register and remove          the concrete subject  methods,               notifyObservers()   implements a                                                 subject may also       Concrete observers can be                                                 and       any class that implements the  method that is used to update   The concrete for setting                                    methods                                 have                  observers    all the current                                               its state (more about       Observerregisters withinterface.a concreteEach observersubject                                   getting                   changes.            state   whenever                                     this later).                        to receive updates.


     What does this have to do with          How does dependence come into              I’ve also heard of a Publish-Q:               Q:               Q:
one-to-many relationships?                  this?                                    Subscribe Pattern. Is that just another
                                                                   name for the Observer Pattern?
      With the Observer Pattern, the Subject        Because the subject is the sole ownerA:               A: is the object that contains the state and          of that data, the observers are dependent on         No, although they are related. The                                   A:controls it. So, there is ONE subject with        the subject to update them when the data       Publish-Subscribe pattern is a more complex
 state. The observers, on the other hand, use    changes. This leads to a cleaner OO design     pattern that allows subscribers to express
 the state, even if they don’t own it. There       than allowing many objects to control the         interest in different types of messages
are many observers, and they rely on the      same data.                              and further separates publishers from
Subject to tell them when its state changes.                                                      subscribers. It is often used in middleware
So there is a relationship between the ONE                                                 systems.
Subject to the MANY Observers.

52      Chapter 2


---

## PDF page 91

the observer pattern


         Guru and Student...
           Guru: Have we talked about loose coupling?
           Student: Guru, I do not recall such a discussion.
Guru: Is a tightly woven basket stiff or flexible?
Student: Stiff, Guru.
Guru: And do stiff or flexible baskets tear or break less easily?
Student: A flexible basket tends to break less easily.
Guru: And in our software, might our designs break less easily if
our objects are less tightly bound together?
Student: Guru, I see the truth of it. But what does it mean for
objects to be less tightly bound?
Guru: We like to call it, loosely coupled.
Student: Ah!
Guru: We say a object is tightly coupled to another object when it is
too dependent on that object.
Student: So a loosely coupled object can’t depend on another
object?
Guru: Think of nature; all living things depend on each other.
Likewise, all objects depend on other objects. But a loosely coupled
object doesn’t know or care too much about the details of another
object.
Student: But Guru, that doesn’t sound like a good quality. Surely
not knowing is worse than knowing.
Guru: You are doing well in your studies, but you have much to
learn. By not knowing too much about other objects, we can create
designs that can handle change better. Designs that have more
flexibility, like the less tightly woven basket.
Student: Of course, I am sure you are right. Could you give me an
example?
Guru: That is enough for today.


                                                   you are here 4      53


---

## PDF page 92

loose coupling

The Power of Loose Coupling

When two objects are loosely coupled, they can interact, but they typically have very little knowledge
of each other. As we’re going to see, loosely coupled designs often give us a lot of flexibility (more
on that in a bit). And, as it turns out, the Observer Pattern is a great example of loose coupling.
Let’s walk through all the ways the pattern achieves loose coupling:

    First, the only thing the subject knows about an observer is that it
   implements a certain interface (the Observer interface). It doesn’t need to
   know the concrete class of the observer, what it does, or anything else about it.
  We can add new observers at any time. Because the only thing the subject depends
   on is a list of objects that implement the Observer interface, we can add new observers
    whenever we want. In fact, we can replace any observer at runtime with another observer
   and the subject will keep purring along. Likewise, we can remove observers at any time.
  We never need to modify the subject to add new types of observers. Let’s say
   we have a new concrete class come along that needs to be an observer. We don’t need         How many
    to make any changes to the subject to accommodate the new class type; all we have              different kinds
    to do is implement the Observer interface in the new class and register as an observer.         of change can you
   The subject doesn’t care; it will deliver notifications to any object that implements the             identify here?
    Observer interface.
  We can reuse subjects or observers independently of each other. If we have
    another use for a subject or an observer, we can easily reuse them because the two aren’t
     tightly coupled.
   Changes to either the subject or an observer will not affect the other.
    Because the two are loosely coupled, we are free to make changes to either, as long as the
    objects still meet their obligations to implement the Subject or Observer interfaces.

                             Design Principle                       Look! We have a new                                                                                Design Principle!                                          Strive for loosely coupled designs
                                 between objects that interact.


  Loosely coupled designs allow us to build flexible OO
  systems that can handle change because they minimize
  the interdependency between objects.


54      Chapter 2


---

## PDF page 93

the observer pattern


Before moving on, try sketching out the classes you’ll need to
implement the Weather Station, including the WeatherData class
and its display elements. Make sure your diagram shows how all
the pieces fit together and also how another developer might
implement her own display element.

If you need a little help, read the next page; your teammates are
already talking about how to design the Weather Station.


                                     you are here 4      55


---

## PDF page 94

conversation about the weather station

Cubicle conversation

Back to the Weather Station project. Your teammates have already begun thinking
through the problem...

                  So, how are we going
                  to build this thing?


                 Mary: Well, it helps to know we’re using the Observer Pattern.
                   Sue: Right...but how do we apply it?
                 Mary: Hmm. Let’s look at the definition again:
                   The Observer Pattern defines a one-to-many dependency between objects so that when
                   one object changes state, all its dependents are notified and updated automatically.

                 Mary: That actually makes some sense when you think about it. Our WeatherData class is the
                      “one,” and our “many” is the various display elements that use the weather measurements.
                   Sue: That’s right. The WeatherData class certainly has state...that’s the temperature,
                       humidity, and barometric pressure, and those definitely change.
                 Mary: Yup, and when those measurements change, we have to notify all the display elements
                       so they can do whatever it is they are going to do with the measurements.
                   Sue: Cool, now I think I see how the Observer Pattern can be applied to our Weather
                        Station problem.
                 Mary: There are still a few things to consider that I’m not sure I understand yet.
     Sue           Sue: Like what?
                 Mary: For one thing, how do we get the weather measurements to the display elements?
                   Sue: Well, looking back at the picture of the Observer Pattern, if we make the WeatherData
                        object the subject, and the display elements the observers, then the displays will register
                       themselves with the WeatherData object in order to get the information they want, right?
                 Mary: Yes...and once the Weather Station knows about a display element, then it can just
                            call a method to tell it about the measurements.
                   Sue: We gotta remember that every display element can be different...so I think that’s where
                      having a common interface comes in. Even though every component has a different type,
                       they should all implement the same interface so that the WeatherData object will know how
                         to send them the measurements.
                 Mary: I see what you mean. So every display will have, say, an update() method that
                    WeatherData will call.
                   Sue: And update() is defined in a common interface that all the elements implement…

56      Chapter 2


---

## PDF page 95

the observer pattern

Designing the Weather Station

How does this diagram compare with yours?

                                                All our weather components               Let’s also create an interface
                                          implement the Observer                 for all display elements
                                               interface. This gives the                to implement. The display                    interface.          Subject                                          Subject a common interface to           elements just need to Here’s our                  familiar.                                            talk to when it comes time to           implement a display() method. This should look                                         update the observers.


           <<interface>>                                         observers              <<interface>>                                 <<interface>>
           Subject                                                                 Observer                          DisplayElement
   registerObserver()                                                                            update()                                           display()
   removeObserver()
   notifyObservers()


                                                         CurrentConditionsDisplay
                              subject                update()                                                                ThirdPartyDisplay
                                                                          display() { // display current
          WeatherData                                                                                                                         update()                                                        measurements }
     registerObserver()                                                                                                                                          display() { // display
     removeObserver()                                                                                                                 something else based on
     notifyObservers()                                                                                                          measurements }
                               This display element            update()StatisticsDisplay     getTemperature()
                                                                                                               display() { // display the aver     getHumidity()                     shows the current                                                                                               age, min and max measure                        Developers can     getPressure()                     measurements from the                                                                                     ments }                                                                                                implement the    measurementsChanged()             WeatherData object.                                                                                               Observer and
                                                                                                 DisplayElement
                                                        This one keeps track           ForecastDisplay      interfaces to                                                                                                                                       update()              create their own      WeatherData now                             of the min/avg/max
                                                                                                                                                      display() { // display the                                                                                                              display element.       implements the Subject                           measurements and
       interface.                                              displays them.                    forecast }

                                                                       This display shows the weather                                                                           forecast based on the barometer.

                                                      These three display elements should have a pointer to
                                                    WeatherData labeled “subject” too, but boy would
                                                                  this diagram start to look like spaghetti if they did.


                                                                        you are here 4      57


---

## PDF page 96

implementing the weather station

Implementing the Weather Station

All right, we’ve had some great thinking from Mary and Sue (from a few pages back)
and we’ve got a diagram that details the overall structure of our classes. So, let’s get
our implemention of the weather station underway. Let’s start with the interfaces:

                                                                Both of these methods take an  public interface Subject {                                                                          Observer as an argument—that is, the
      public void registerObserver(Observer o);                Observer to be registered or removed.
      public void removeObserver(Observer o);
      public void notifyObservers();           This method is called to notify all observers
  }                                                when the Subject’s state has changed.

  public interface Observer {
      public void update(float temp, float humidity, float pressure);
  }                                                                    The Observer interface
                             These are the state values the Observers get from                                                                                                                                is implemented by all
                              the Subject when a weather measurement changes.           observers, so they all
                                                                                        have to implement the
                                                                                         update() method. Here  public interface DisplayElement {                                                                                             we’re following Mary and
      public void display();     The DisplayElement interface                      Sue’s lead and passing
  }                                           just includes one method, display(),              the measurements to the
                                      that we will call when the display                  observers.
                                         element needs to be displayed.


      Mary and Sue thought that passing the measurements directly to the observers was the
      most straightforward method of updating state. Do you think this is wise? Hint: is this an area
        of the application that might change in the future? If it did change, would the change be well
       encapsulated, or would it require changes in many parts of the code?
     Can you think of other ways to approach the problem of passing the updated state to the
       observers?
       Don’t worry; we’ll come back to this design decision after we finish the initial implementation.


58      Chapter 2


---

## PDF page 97

the observer pattern

                                                           REMEMBER: we don’t provide
Implementing the Subject interface                        import and package statements
                                                                                                               in the code listings. Get thein WeatherData                                                                                    complete source code from
 Remember our first attempt at implementing the WeatherData class at the            https://wickedlysmart.com/
 beginning of the chapter? You might want to refresh your memory. Now it’s           head-first-design-patterns
 time to go back and do things with the Observer Pattern in mind:

                                                                WeatherData now implements     public class WeatherData implements Subject {                                                                    the Subject interface.         private List<Observer> observers;
         private float temperature;         private float humidity;                           We’ve added an ArrayList to
         private float pressure;                           hold the Observers, and we                                                                                       constructor.                                                                  create it in the         public WeatherData() {
             observers = new ArrayList<Observer>();
         }                                                           When an observer registers, we
                                                                                just add it to the end of the list.         public void registerObserver(Observer o) {
             observers.add(o);interface.         }                                                              Likewise, when an observer wants to
                                                                               un-register, we just take it off the list.
         public void removeObserver(Observer o) {Subject             observers.remove(o);                                   Here’s the fun part; this is where we
the     }                                                                           tell all the observers about the state.
                                                                        Because they are all Observers, we
                                                                  know they all implement update(), so we         public void notifyObservers() {                                                                                          them.implement                                                              know how to notify             for (Observer observer : observers) {
we             observer.update(temperature, humidity, pressure);
             }                                                             when we                                                                                ObserversHere     }                                               We notify the                                                                           measurements from                                                         get updated         public void measurementsChanged() {                         Station.                                                        the Weather             notifyObservers();
         }
         public void setMeasurements(float temperature, float humidity, float pressure) {
             this.temperature = temperature;
             this.humidity = humidity;               Okay, while we wanted to ship a nice little             this.pressure = pressure;                                                           weather station with each book, the publisher             measurementsChanged();                                                                 wouldn’t go for it. So, rather than reading         }
                                                                   actual weather data off a device, we’re going
         // other WeatherData methods here         to use this method to test our display elements.
    }                                                       Or, for fun, you could write code to grab
                                                            measurements off the web.


                                                                         you are here 4      59


---

## PDF page 98

build the display elements

Now, let’s build those display elements

Now that we’ve got our WeatherData class straightened out, it’s time to build the
display elements. Weather-O-Rama ordered three: the current conditions display, the
 statistics display, and the forecast display. Let’s take a look at the current conditions
display; once you have a good feel for this display element, check out the statistics and
forecast displays in the code directory. You’ll see they are very similar.
                                                                                    It also implements DisplayElement,                                      This display implements the Observer                                                                                 because our API is going to                                         interface so it can get changes from                                                                                      require all display elements to                                    the WeatherData object.                                                                              implement this interface.

 public class CurrentConditionsDisplay implements Observer, DisplayElement {
     private float temperature;
     private float humidity;                                                                 The constructor is passed the     private WeatherData weatherData;                                                                         weatherData object (the Subject)
                                                                         and we use it to register the     public CurrentConditionsDisplay(WeatherData weatherData) {                                                                                            display as an observer.         this.weatherData = weatherData;
         weatherData.registerObserver(this);
     }
     public void update(float temperature, float humidity, float pressure) {
         this.temperature                         = temperature;                                                       When update() is called, we         this.humidity = humidity;         display();                                              save the temp and humidity     }                                                    and call display().
     public void display() {
         System.out.println("Current conditions: " + temperature
            + "F degrees and " + humidity + "% humidity");                                                                 The display() method     }                                                                                           just prints out the most}                                                                                   recent temp and humidity.


       Is update() the best place to call display()?                  Why did you store a reference to the WeatherDataQ:                       Q:
                                                              Subject? It doesn’t look like you use it again after the
       In this simple example it made sense to call display() when the     constructor.A:values changed. However, you’re right; there are much better ways to
design the way the data gets displayed. We’ll see this when we get to          True, but in the future we may want to un-register ourselves as                          A: the Model-View-Controller pattern.                               an observer and it would be handy to already have a reference to the
                                                                            subject.

60      Chapter 2


---

## PDF page 99

the observer pattern

Power up the Weather Station


 1  First, let’s create a test harness.

    The Weather Station is ready to go. All we need is some code to
      glue everything together. We’ll be adding some more displays and
      generalizing things in a bit. For now, here’s our first attempt:

       public class WeatherStation {                                           First, create the
                                                                           WeatherData object.
           public static void main(String[] args) {
               WeatherData weatherData = new WeatherData();

               CurrentConditionsDisplay currentDisplay =If you don’t
want to             new CurrentConditionsDisplay(weatherData);
download the     StatisticsDisplay statisticsDisplay = new StatisticsDisplay(weatherData);
 code, you can               ForecastDisplay forecastDisplay = new ForecastDisplay(weatherData); comment out
 these two lines                                                                           Create the three
 and run it.      weatherData.setMeasurements(80, 65, 30.4f);                        displays and
               weatherData.setMeasurements(82, 70, 29.2f);                      pass them the
                                                                                    WeatherData object.               weatherData.setMeasurements(78, 90, 29.2f);
           }                                         Simulate new weather
       }                                              measurements.


 2 Run the code and let the Observer Pattern do its magic.


                                      File Edit  Window Help StormyWeather
                 %java WeatherStation
                 Current conditions: 80.0F degrees and 65.0% humidity
                 Avg/Max/Min temperature = 80.0/80.0/80.0
                 Forecast: Improving weather on the way!
                 Current conditions: 82.0F degrees and 70.0% humidity
                 Avg/Max/Min temperature = 81.0/82.0/80.0
                 Forecast: Watch out for cooler, rainy weather
                 Current conditions: 78.0F degrees and 90.0% humidity
                 Avg/Max/Min temperature = 80.0/82.0/78.0
                 Forecast: More of the same
                 %


                                                                        you are here 4      61


---

## PDF page 100

exercise: code the heat index display


               Johnny Hurricane, Weather-O-Rama’s CEO, just called and they can’t possibly ship without a Heat
                 Index display element. Here are the details.

               The heat index is an index that combines temperature and humidity to determine the apparent
                temperature (how hot it actually feels). To compute the heat index, you take the temperature, T,
               and the relative humidity, RH, and use this formula:

              heatindex =
                  16.923  + 1.85212 * 10-1 * T  + 5.37941 * RH  - 1.00254 * 10-1 *
                  T * RH  + 9.41695 * 10-3 * T2 + 7.28898 * 10-3 * RH2  + 3.45372 *
                       10-4 * T2 * RH  - 8.14971 * 10-4 * T * RH2  + 1.02102 * 10-5 * T2 *
                      RH2  - 3.8646 * 10-5 * T3  + 2.91583 * 10-5 * RH3  + 1.42721 * 10-6
                  * T3 * RH  + 1.97483 * 10-7 * T * RH3  - 2.18429 * 10-8 * T3 * RH2
                  + 8.43296 * 10-10 * T2 * RH3  - 4.81975 * 10-11 * T3 * RH3

               So get typing!

                   Just kidding. Don’t worry, you won’t have to type that formula in; just create your own
                   HeatIndexDisplay.java file and copy the formula from heatindex.txt into it.
                                                You can get heatindex.txt from wickedlysmart.com.


            How does it work? You’d have to refer to Head First Meteorology, or try asking someone at the
                  National Weather Service (or try a web search).

             When you finish, your output should look like this:


                                                          File Edit  Window Help OverDaRainbow
                         %java WeatherStation
                         Current conditions: 80.0F degrees and 65.0% humidity
                         Avg/Max/Min temperature = 80.0/80.0/80.0
                         Forecast: Improving weather on the way!           Here’s what
          changed in          Heat index is 82.95535
           this output.         Current conditions: 82.0F degrees and 70.0% humidity
                         Avg/Max/Min temperature = 81.0/82.0/80.0
                         Forecast: Watch out for cooler, rainy weather
                         Heat index is 86.90124
                         Current conditions: 78.0F degrees and 90.0% humidity
                         Avg/Max/Min temperature = 80.0/82.0/78.0
                         Forecast: More of the same
                         Heat index is 83.64967
                         %


62      Chapter 2


---

## PDF page 101

the observer pattern


                                            Tonight’s talk: Subject and Observer spar over the right way
                                           to get state information to the Observer.


Subject:                                              Observer:
I’m glad we’re finally getting a chance to chat in
person.
                                                                 Really? I thought you didn’t care much about us
                                                               Observers.


Well, I do my job, don’t I? I always tell you what’s
going on... Just because I don’t really know who
you are doesn’t mean I don’t care. And besides, I
do know the most important thing about you—you
implement the Observer interface.
                                                            Yeah, but that’s just a small part of who I am.
                                                        Anyway, I know a lot more about you...

Oh yeah, like what?

                                                                  Well, you’re always passing your state around to us
                                                            Observers so we can see what’s going on inside you.
                                                  Which gets a little annoying at times...

Well, excuuuse me. I have to send my state with my
notifications so all you lazy Observers will know
what happened!                                            Okay, wait just a minute here; first, we’re not lazy,
                                                 we just have other stuff to do in between your oh-
                                                               so-important notifications, Mr. Subject, and second,
                                                  why don’t you let us come to you for the state we
                                                       want rather than pushing it out to just everyone?

Well...I guess that might work. I’d have to open
myself up even more, though, to let all you
Observers come in and get the state that you
need. That might be kind of dangerous. I can’t
let you come in and just snoop around looking at
everything I’ve got.


                                                                        you are here 4      63


---

## PDF page 102

fireside chat: subject and observer


Subject:                                              Observer:
                                           Why don’t you just write some public getter
                                                        methods that will let us pull out the state we need?

Yes, I could let you pull my state. But won’t
that be less convenient for you? If you have to
come to me every time you want something, you
might have to make multiple method calls to get
all the state you want. That’s why I like push
better...then you have everything you need in one
notification.
                                                           Don’t be so pushy! There are so many different
                                                                 kinds of us Observers, there’s no way you can
                                                                     anticipate everything we need. Just let us come to
                                                        you to get the state we need. That way, if some of
                                                               us only need a little bit of state, we aren’t forced to
                                                                    get it all. It also makes things easier to modify later.
                                                                     Say, for example, you expand yourself and add
                                                    some more state. If you use pull, you don’t have to
                                                        go around and change the update calls on every
                                                                   observer; you just need to change yourself to allow
                                                    more getter methods to access our additional state.


Well, as I like to say, don’t call us, we’ll call you!
But I’ll give it some thought.
                                                                             I won’t hold my breath.


You never know, hell could freeze over.
                                                                             I see, always the wise guy...


Indeed.


64      Chapter 2


---

## PDF page 103

the observer pattern

Looking for the Observer Pattern in the Wild

The Observer Pattern is one of the most common patterns in use, and you’ll find plenty
of examples of the pattern being used in many libraries and frameworks. If we look at the
Java Development Kit (JDK), for instance, both the JavaBeans and Swing libraries make use
of the Observer Pattern. The pattern’s not limited to Java either; it’s used in JavaScript’s
events and in Cocoa and Swift’s Key-Value Observing protocol, to name a couple of other
examples. One of the advantages of knowing design patterns is recognizing and quickly
understanding the design motivation in your favorite libraries. Let’s take a quick diversion
into the Swing library to see how Observer is used.                               If you’re curious about                                                                                        Pattern in                                                                       the ObserverThe Swing library                                                                                       check out the                                                                                 JavaBeans,You probably already know that Swing is Java’s GUI toolkit for user interfaces. One   PropertyChangeListener
of the most basic components of that toolkit is the JButton class. If you look up        interface.
JButton’s superclass, AbstractButton, you’ll find that it has a lot of add/remove
listener methods. These methods allow you to add and remove observers—or, as
they are called in Swing, listeners—to listen for various types of events that occur
on the Swing component. For instance, an ActionListener lets you “listen in” on
any types of actions that might occur on a button, like a button press. You’ll find
various types of listeners all over the Swing API.
A little life-changing application
Okay, our application is pretty simple. You’ve got a button that says, “Should I do
it?” and when you click on that button the listeners (observers) get to answer the
question in any way they want. We’re implementing two such listeners, called the
AngelListener and the DevilListener. Here’s how the application behaves:

                                                       interface.                                      Here’s our fancy


                                                       And here’s the output when                                                        we click on the button.


                                                                     File Edit Window Help HeMadeMeDoIt
                                  %java SwingObserverExample                     Devil answer
                                  Come on, do it!
                      Angel answer     Don’t do it, you might regret it!
                                  %

                                                                        you are here 4      65


---

## PDF page 104

use action listener observers

Coding the life-changing application

This life-changing application requires very little code. All we need to do is
create a JButton object, add it to a JFrame, and set up our listeners. We’re
going to use inner classes for the listeners, which is a common technique in
Swing programming. If you aren’t up on inner classes or Swing, you might
want to review the Swing chapter in your favorite Java reference guide.
                                                                                                       application that   public class SwingObserverExample {                                  Simple Swing                                                                 a frame and                                                                                     creates      JFrame frame;                                                           just                                                                                                      in it.                                                              a button                                                                          throws      public static void main(String[] args) {
          SwingObserverExample example = new SwingObserverExample();
          example.go();
      }
      public void go() {
          frame = new JFrame();
                                                                           Makes the devil and
          JButton button = new JButton("Should I do it?");              angel objects listeners
                                                                                               (observers) of the button.          button.addActionListener(new AngelListener());
          button.addActionListener(new DevilListener());

          // Set frame properties here               Code to set up the frame goes here.
      }
                                                                               Here are the class definitions for
      class AngelListener implements ActionListener {             the observers, defined as inner
          public void actionPerformed(ActionEvent event) {         classes (but they don’t have to be).
              System.out.println("Don't do it, you might regret it!");
          }
      }

      class DevilListener implements ActionListener {
          public void actionPerformed(ActionEvent event) {
              System.out.println("Come on, do it!");
          }
      }                                                     Rather than update(), the actionPerformed()                                                          method gets called when the state in the  }                                                                       subject (in this case the button) changes.


66      Chapter 2


---

## PDF page 105

the observer pattern

                                                                                   in Java                                                                  added                                                                 were          don’t                                                                            them,                                                                      expressions                                                                       with                                            Lambda                                                                                             inner                                                                             familiar                                                                                             using                                                                  aren’t                                                                                continue                                                  8. If you                                                              you can                                                                              it;                                                        about                                                                                     observers.                                                  worry                                                                  Swing                                                      for your                                                                 classes

                                                                                   expression                                                            a lambda                                                                   using                                                 By                                                           further?                                              even                                            Pattern                               Observer                             of the                       use                  your             taking                                                                          lambda       about                                                                         a How                                                                     With                                                                                   object.                                                             ActionListener                                               an                                                    creating                                                 of                                       the step                                     skip                           can                       you                           class,                inner           an                                                                                             pass        than                                                                            you  rather                                                                when                                                                 And,                                                                                      the observer.                                                                                              is                                                                                  object                                                                   function                                                                 the                                      and                                          instead,                                  object                         function                   a                 create          we                                                                                            the  expression,                                                                             actionPerformed(),                                                             matches                                                            signature                                                                             its                                                ensures                                           Java                         addActionListener(),                      to                object   that function
  one method in the ActionListener interface.                                                                               the function                                                                                 its observers—including                                                           notifies                                 the button object                                 is clicked,                 button              the       when   Later,                                                     and calls each listener’s                                             been clicked,                                                                         it’s                              expressions—that                    the lambda               by          created   objects
   actionPerformed() method.
   Let’s take a look at how you’d use lambda expressions as observers to simplify our previous code:

The updated code, using lambda expressions:
  public class SwingObserverExample {
      JFrame frame;      public static void main(String[] args) {                                             SwingObserverExample();                                                                                                AngelListener          SwingObserverExample example = new                                                                              We’ve replaced the          example.go();                                          and DevilListener objects with     }                                                               lambda expressions that implement      public void go() {                                                                     the same functionality that we          frame = new JFrame();                                                                  had before.
          JButton button = new JButton("Should I do it?");           button.addActionListener(event ->                                       do it, you might regret it!"));                System.out.println("Don't           button.addActionListener(event ->                    When you click the button, the                System.out.println("Come on, do it!"));          function objects created by the
                                                                           lambda expressions are notified          // Set frame properties here                                                                        and the method they implement      }                                                                                                                     is run.   }           We’ve removed the two ActionListener classes
                 (DevilListener and AngelListener) completely.                      Using lambda expressions makes
                                                                                          this code a lot more concise.
  For more on lambda expressions, check out the Java docs.


                                                                      you are here 4      67


---

## PDF page 106

revisiting push and pull


           I thought Java had Observer and Observable classes?            JavaBeans offers built-in support throughQ:                        A:                                                                PropertyChangeEvents that are generated when a Bean
     Good catch. Java used to provide an Observable class (the       changes a particular kind of property, and sends notificationsA:Subject) and an Observer interface, which you could use to help          to PropertyChangeListeners. There are also related publisher/
 integrate the Observer Pattern in your code. The Observable class       subscriber components in the Flow API for handling asynchronous
provided methods to add, delete, and notify observers, so that you       streams.
 didn’t have to write that code. And the Observer interface provided
an interface just like ours, with one update() method. These classes          Should I expect notifications from a Subject to its                         Q:
were deprecated in Java 9. Folks find it easier to support the basic      Observers to arrive in a specific order?
Observer Pattern in their own code, or want something more robust,
so the Observer/Observable classes are being phased out.                  With Java’s implementations of Observer, the JDK developers                          A:                                                                                 specifically advise you to not depend on any specific notification
     Does Java offer other built-in support for Observer to          order.Q:
replace those classes?


                      I was thinking about the push/pull discussion
                    we had earlier. Would it generalize the code a
                           bit more if we allowed the displays to pull their
                       data from the WeatherData object as needed?
                     That might make it easier to add new displays in
                       the future.


                              That’s a good idea.
                                 In our current Weather Station design, we are pushing all three pieces of data
                                     to the update() method in the displays, even if the displays don’t need all these
                                      values. That’s okay, but what if Weather-O-Rama adds another data value later,
                                           like wind speed? Then we’ll have to change all the update() methods in all the
                                        displays, even if most of them don’t need or want the wind speed data.
                             Now, whether we pull or push the data to the Observer is an implementation
                                          detail, but in a lot of cases it makes sense to let Observers retrieve the data they
                               need rather than passing more and more data to them through the update()
                               method. After all, over time, this is an area that may change and grow unwieldy.
                              And, we know CEO Johnny Hurricane is going to want to expand the Weather
                                    Station and sell more displays, so let’s take another pass at the design and see if
                           we can make it even easier to expand in the future.
                               Updating the Weather Station code to allow Observers to pull the data they
                               need is a pretty straightforward exercise. All we need to do is make sure the
                                  Subject has getter methods for its data, and then change our Observers to use
                             them to pull the data that’s appropriate for their needs. Let’s do that.

68      Chapter 2


---

## PDF page 107

the observer pattern

Meanwhile, back at Weather-O-Rama

There’s another way of handling the data in the Subject: we can rely on the
Observers to pull it from the Subject as needed. Right now, when the Subject’s data
changes, we push the new values for temperature, humidity, and pressure to the
Observers, by passing that data in the call to update().
Let’s set things up so that when an Observer is notified of a change, it calls getter
methods on the Subject to pull the values it needs.
To switch to using pull, we need to make a few small changes to our existing code.

For the Subject to send notifications...

      1  We’ll modify the notifyObservers() method in WeatherData to call the method
             update() in the Observers with no arguments:
             public void notifyObservers() {
                    for (Observer observer : observers) {
                           observer.update();
                    }
             }
For an Observer to receive notifications...

      1  Then we’ll modify the Observer interface, changing the signature of the
             update() method so that it has no parameters:
             public interface Observer {
                    public void update();
             }

      2 And finally, we modify each concrete Observer to change the signature of its respective
             update() methds and get the weather data from the Subject using the WeatherData’s
             getter methods. Here’s the new code for the CurrentConditionsDisplay class:
             public void update() {
                    this.temperature = weatherData.getTemperature();                                                                                       Here we’re using the                    this.humidity = weatherData.getHumidity();                                                                                                   Subject’s getter methods
                    display();                                                 that were supplied with
             }                                                                    the code in WeatherData
                                                                               from Weather-O-Rama.


                                                                        you are here 4      69


---

## PDF page 108

code magnet exercise

        Code Magnets
              The ForecastDisplay class is all scrambled up on the fridge. Can you
                 reconstruct the code snippets to make it work? Some of the curly
                braces fell on the floor and they were too small to pick up, so feel
                  free to add as many of those as you need!

                                               public ForecastDisplay(WeatherData
                                                weatherData) {
                                                                        display();
                                                weatherData.registerObserver(this);

                                                                          implements                                                          ForecastDisplay                                             public class                                             Observer, DisplayElement {
                                                           public void display() {
                                                            // display code here
                                                     }

                                               = currentPressure;                                          lastPressure                                                  = weatherData.getPressure();                                           currentPressure
                                               private float                                                             currentPressure = 29.92f;                                               private float                                                             lastPressure;

                                            this.weatherData = weatherData;

                                             public void update() {                                                           }

                                             private WeatherData weatherData;


70      Chapter 2


---

## PDF page 109

the observer pattern

Test Drive the new code
Okay, you’ve got one more display to update, the Avg/Min/Max display. Go ahead and
do that now!

Just to be sure, let’s run the new code...


                                                 File Edit  Window Help TryThisAtHome
                         %java WeatherStation
                         Current conditions: 80.0F degrees and 65.0% humidity
                         Avg/Max/Min temperature = 80.0/80.0/80.0
      Here’s what we got.      Forecast: Improving weather on the way!
                         Current conditions: 82.0F degrees and 70.0% humidity
                         Avg/Max/Min temperature = 81.0/82.0/80.0
                         Forecast: Watch out for cooler, rainy weather
                         Current conditions: 78.0F degrees and 90.0% humidity
                         Avg/Max/Min temperature = 80.0/82.0/78.0 Look! This just arrived!                         Forecast: More of the same
                        %


                              Weather-O-Rama, Inc.
                              100 Main Street
                                Tornado Alley, OK 45021


             Wow!
               Your                      design                                       is                                    fantastic.                                Not                                          only                                              did                                            you                                                         quickly                                                                  create                                                                                         all                                                                          three                   displays                           that                      we                               asked                                                  for,                                          you’ve                                                 created                                             a                                                          general                                                                design                                                                           that                  allows                     anyone                               to                                   create                              new                                                   display,                                          and                                                  even                                                              allows                                                                     users                                                                        to                                                             add              and                  remove                               displays                                       at                                      runtime!
                 Ingenious!
                 Until our next                            engagement,


                                                                        you are here 4      71


---

## PDF page 110

design toolbox

         Tools for your Design Toolbox

            Welcome to the end of Chapter 2. You’ve added a
              few new things to your OO toolbox...
                                                              The Observer Pattern defines
                                                                             a one-to-many relationship
                                                                               between objects.
                                                               Subjects update Observers
                                                                                         using a common interface.                 Basics        OO                                       Observers of any concrete type
                               Abstraction                                         can participate in the pattern
                                                                                 as long as they implement the                                 Encapsulation
       Principles                                        Observers are loosely coupled  OO                     Polymorphism                                         Observer interface.                          varies. Inheritence                                                       in that the Subject knows              what      Encapsulate                                                                      nothing about them, other                      over                                                                                       than that they implement the             composition      Favor
        inheritance.                                                               Observer interface.                                                  your newest            You can push or pull data from             to interfaces, not             Here’s       Program                                    Remember,                 the Subject when using the
                                                                  designs               pattern (pull is considered more         implementations.                            principle.coupled       are                                                        loosely                                                       and                         coupled                                                                  flexible                                                                                                            “correct”).                     loosely                          that        much more         Strive for                                                             change.                                               to                        objects               between                           resilient                  Swing makes heavy use of the          designs
                                                                                   Observer Pattern, as do many          interact.                                                                        GUI frameworks.
                                                               You’ll also find the pattern in
                                                                      many other places, including
                                                                                         JavaBeans,                                                                                             and RMI,                                     algorithms,                                         RxJava,    Patterns                                                                                 as well as                                                                                                                         in other language OO              a family of                defines       -                           thema one-to-many                                                                                      frameworks,                                                                                                                                 like                                                                                               Cocoa,                                                                                                                                   Swift,                         makes                      defines   Strategy            -and                                that                    one,                               so              each                                      algorithm       Observer                                                                             and                                                                                               JavaScript                                                                                                           events.                           theobjects                              lets    encapsulates                   between                                             all its                  Strategy                                                it.                                  state,use          dependency                             that                         changes                                                                                                                                      The                                                                                       Observer                                                                                                             Pattern                                                                                                                                                   is related     interchangeable.                              clients                  fromobject                                  updated             one                           and         when                                                                                                        to the                                                                                                   Publish/Subscribe                                                                                                                             Pattern,                          notified    vary independently                   are           dependents                                                             which is for more complex            automatically                                                                       situations with multiple Subjects
                                                                                            and/or multiple message types.
                                                              The Observer Pattern is a
                    A new pattern for communicating state to a            commonly used pattern, and
                              set of objects in a loosely coupled manner. We               we’ll see it again when we learn
                               haven’t seen the last of the Observer Pattern—         about Model-View-Controller.
                                 just wait until we talk about MVC!

72      Chapter 2


---

## PDF page 111

the observer pattern

                 Design Principle Challenge
                               For each design principle, describe how the Observer
                                Pattern makes use of the principle.


Design Principle
Identify the aspects of your application that vary
and separate them from what stays the same.


 Design Principle
 Program to an interface, not an implementation.


                                                       This is a hard one. Hint: think about how observers
                                                  and subjects work together.
Design Principle
Favor composition over inheritance.


                                                                    you are here 4      73


---

## PDF page 112

cross word

           Design Patterns Crossword
                   Time to give your right brain something to do again!
                         All of the solution words are from Chapters 1 & 2.

                                                                                   1
                  2                                           3            4
                                                                                                5
             6                                               7
                                                         8
                  9        10


                          11
                                                                          12  13                        14
                      15


                                                             16  17
                      18
                  19
             20                        21


                                                22

ACROSS                          DOWN
1. One Subject likes to talk to _______ observers.              1. He didn’t want any more ints, so he removed himself.
3. Subject initially wanted to _________ all the data to         2. Temperature, humidity, and __________.
Observer.                                                        4. Weather-O-Rama’s CEO is named after this kind of
6. CEO almost forgot the ________ index display.             storm.
8. CurrentConditionsDisplay implements this interface.         5. He says you should go for it.
9. Java framework with lots of Observers.                       7. The Subject doesn’t have to know much about the
11. A Subject is similar to a __________.                   _____.
12. Observers like to be ___________ when something       10. The WeatherData class __________ the Subject
new happens.                                                     interface.
15. How to get yourself off the Observer list.                  13. Don’t count on this for notification.
16. Lori was both an Observer and a _________.             14. Observers are______ on the Subject.
18. Subject is an ______.                                    17. Implement this method to get notified.
20. You want to keep your coupling ________.                19. Jill got one of her own.
21. Program to an __________ not an implementation.
22. Devil and Angel are _________ to the button.

74      Chapter 2


---

## PDF page 113

the observer pattern


                                                       Based on our first implementation, which of the
                                                              following apply? (Choose all that apply.)


              ❏ A. We are coding to concrete     ❏ D. The display elements don’t implement
                              implementations, not interfaces.         a common interface.
              ❏  B. For every new display element,   ❏  E. We haven’t encapsulated what changes.
                        we need to alter code.       ❏  F. We are violating encapsulation of the
              ❏ C. We have no way to add display         WeatherData class.
                              elements at runtime.


       Design
       Principle
       Challenge
       Solution                      The thing that varies in the Observer Pattern
                                                                                       is the state of the Subject and the number and
 Design Principle                                     types of Observers. With this pattern, you can
  Identify the aspects of your application that               vary the objects that are dependent on the state vary and separate them from what stays the
 same.                                            of the Subject, without having to change that
                                                             Subject. That’s called planning ahead!


                                                Both the Subject and Observers use interfaces.
                                              The Subject keeps track of objects implementing
Design Principle                                   the Observer interface, while the Observers
Program to an interface, not an implementation.            register with, and get notified by, the Subject
                                                              interface. As we’ve seen, this keeps things nice and
                                                                    loosely coupled.


                                               The Observer Pattern uses composition to compose
                                                          any number of Observers with their Subject.
 Design Principle                                   These relationships aren’t set up by some kind
 Favor composition over inheritance.
                                                   of inheritance hierarchy. No, they are set up at
                                                         runtime by composition!


                                                                      you are here 4      75


---

## PDF page 114

exercise solution

       Code Magnets Solution
             The ForecastDisplay class is all scrambled up on the fridge. Can you
                reconstruct the code snippets to make it work? Some of the curly
               braces fell on the floor and they were too small to pick up, so feel
                 free to add as many of those as you need! Here’s our solution.

                              implements              ForecastDisplay public class Observer, DisplayElement {
       private float                     currentPressure = 29.92f;       private float                     lastPressure;
      private WeatherData weatherData;
    public ForecastDisplay(WeatherData
    weatherData) {
       this.weatherData = weatherData;
      weatherData.registerObserver(this);
    }
     public void update() {
                  = currentPressure;         lastPressure                     = weatherData.getPressure();         currentPressure

          display();
     }
   public void display() {
      // display code here
  }
    }


76      Chapter 2


---

## PDF page 115

the observer pattern


         Design Patterns
          Crossword Solution


                                                                      1                               M A N  Y
    2                                           3            4    P                               P U S H   O
                                                                                   5   R                             U    U      D
6                                               7H E A T                O       R    S       E
                                            8   S                  O  B  S  E  R  V  E  R    V
    9        10   S W  I N G              S        I              I
   U   M                    E        C              L
             11   R     P U  B  L  I  S H E  R      A              L
                                                             12  13                        14   E     L                    V     N O T  I  F  I  E D
         15      R  E M O V  E O  B  S  E  R  V  E  R         S    E
      M                    R         D         T     P
                                                16  17         E                   S U  B  J  E  C T    E    E
         18       I N T  E  R  F A  C  E     P       R        N   N
    19   J    T                    D                  E    D
20                        21 L O O S  E     I N T  E  R  F A  C  E            R    E
   B                          T                  N
                                   22                         L  I  S T  E N  I N G           T


                                                                   you are here 4      77
