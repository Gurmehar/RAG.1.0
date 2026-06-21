# 6: the Command Pattern: Encapsulating Invocation

_Extracted from PDF pages 229-274. Text only; images and diagrams are not embedded._


---

## PDF page 229

6 the Command Pattern
     EncapsulatingInvocation


       These top secret drop
 boxes have revolutionized the spy
industry. I just drop in my request and
people disappear, governments change
overnight, and my dry cleaning gets done. I
don’t have to worry about when, where, or
        how; it just happens!


             In this chapter, we take encapsulation to a whole new level:
           we’re going to encapsulate method invocation. That’s right—by
                encapsulating method invocation, we can crystallize pieces of computation so that
                 the object invoking the computation doesn’t need to worry about how to do things, it
                    just uses our crystallized method to get it done. We can also do some wickedly smart
                  things with these encapsulated method invocations, like save them away for logging
                  or reuse them to implement undo functionality in our code.


                                                                                       this is a new chapter      191


---

## PDF page 230

home automation or bust


                    Home Automation or Bust, Inc.
                        1221 Industrial Avenue, Suite 2000
                           Future City, IL 62914


                       Greetings!
                            I recently received a demo and briefing from Johnny
                      Hurricane, CEO of Weather-O-Rama, on their new
                     expandable weather station. I have to say, I was so
                     impressed with the software architecture that I’d like to
                     ask you to design the API for our new Home Automation
                   Remote Control. In return for your services we’d be happy
                        to handsomely reward you with stock options in Home
                     Automation or Bust, Inc.
                   You should have already received a prototype of our
                      ground-breaking remote control for your perusal. The
                     remote control features seven programmable slots (each
                     can be assigned to a different household device) along with
                      corresponding on/off buttons for each. The remote also has
                    a global undo button.
                       I’m also attaching to this email a set of Java classes
                        that were created by various vendors to control home
                      automation devices such as lights, fans, hot tubs, audio
                       equipment, and other similar controllable appliances.
                     We’d like you to create an API for programming the remote
                       so that each slot can be assigned to control a device or set of
                         devices. Note that it is important that we be able to control
                              all the current devices, and also any future devices that the
                      vendors may supply.
                      Given the work you did on the Weather-O-Rama weather
                           station, we know you’ll do a great job on our remote control!
                 We look forward to seeing your design.
                           Sincerely,


                               Bill Thompson, CEO


192      Chapter 6


---

## PDF page 231

the command pattern


            Free hardware! Let’s check out the Remote Control...


                                                                  There are on and off
                                                                          buttons for each of
                                                                     the seven slots.

                       We                to program.We’ve got seven slots                          in each                   device         differentcan put a                          buttons.                it via the        controlslot and                                                                              These two                                                                                               buttons are                                                                                    used to control the
                                                                                          household device stored                                                                                             in slot one...
                                                                                                      ...and these two control                                                                          the household device                                                                                    stored in slot two...
                                                                                                 ...and so on.


         Get your Sharpie out and           write your device names here.
                                                      Here’s the global undo button that
                                                 undoes the operation of the last
                                               button pressed.


                                                                    you are here 4      193


---

## PDF page 232

vendor classes from home automation

Taking a look at the vendor classes

Let’s check out the vendor classes the CEO attached to his email.
These should give you some idea of the interfaces of the objects
we need to control from the remote.

     Wow, lots of different kinds                                                               ApplianceControl
                                                                                                                                      on()     of devices that we’re going
                                                                                                                                                                         off()      to need to be able to control.
                                                                                                    Stereo

                                                                                                                  on()
                                                  CeilingLight                                                   off()
                                                                                                            setCd()
                                                  on()                                                                                                           setDvd()
                                                               off()
                                                 dim()                          TV              setRadio()                                                                                                        setVolume()               OutdoorLight                                                                                       FaucetControl
                                                                               on()
           on()                                                                                  off()                                                   openValve()
             off()                                                             setInputChannel()                                         closeValve()
                                                                         setVolume()
                                          CeilingFan                                                    Hottub

                                             high()                                                                                 circulate()
                                                                GarageDoor               jetsOn()           GardenLight           medium()
                                            low()                                                                                    jetsOff()                                                                                  up()
     setDuskTime()                            off()                                                                      setTemperature()                                                                       down()
     setDawnTime()                   getSpeed()                                                                                     stop()                                               Thermostat     manualOn()
                                                                                     lightOn()
      manualOff()                                                                                               lightOff()                                               setTemperature()
                                           Sprinkler                                                                                                         ()                                                                                                   SecurityControl
                                    waterOn()                                                                    Light                          arm()
                                        waterOff()                                                                                                                disarm()
                                                                     on()
                                                                                       off()

   And some very different
     kinds of interfaces across
    these devices.
                                                              It looks like we have quite a set of classes here, and not a lot of
                                                 industry effort to come up with a set of common interfaces. Not
                                               only that, it sounds like we can expect more of these classes in the
                                                      future. Designing a remote control API is going to be interesting.
                                                     Let’s get on to the design.


194      Chapter 6


---

## PDF page 233

the command pattern

                                            Cubicle Conversation

                          Your teammates are already discussing how to design the remote control API...


                Well, we’ve got another design to
                 do. My first observation is that we’ve
Sue           gotbuttonsa simplebut aremoteset of withvendoron andclassesoff
               that are quite diverse.


                     Mary: Yes, I thought we’d see a bunch of classes with on() and off()
                           methods, but here we’ve got methods like dim(), setTemperature(),
                              setVolume(), and setInputChannel(), and waterOn().
                        Sue: Not only that, it sounds like we can expect more vendor classes in
                             the future with methods just as diverse.
                     Mary: I think it’s important we view this as a separation of concerns.
                        Sue: Meaning?
                     Mary: What I mean is that the remote should know how to interpret
                            button presses and make requests, but it shouldn’t know a lot about
                      home automation or how to turn on a hot tub.
                        Sue: But if the remote is dumb and just knows how to make generic
                                requests, how do we design the remote so that it can invoke an action
                                  that, say, turns on a light or opens a garage door?
                     Mary: I’m not sure, but we don’t want the remote to have to know the
                                  specifics of the vendor classes.
                        Sue: What do you mean?
                     Mary: We don’t want the remote to consist of a set of  if statements,
                                    like “if slot1 == Light, then light.on(), else if slot1 == Hottub then
                               hottub.jetsOn()”. We know that is a bad design.
                        Sue: I agree. Whenever a new vendor class comes out, we’d have to go
                                in and modify the code, potentially creating bugs and more work for
                                ourselves!


                                                                you are here 4      195


---

## PDF page 234

command pattern might work


                                Hey, I couldn’t help
                                overhearing. Since Chapter 1
                                  I’ve been boning up on Design
                                  Patterns. There’s a pattern
                                called “Command Pattern” I think
                                    might help.


                    Mary: Yeah? Tell us more.
                          Joe: The Command Pattern allows you to decouple the requester of an action from
                            the object that actually performs the action. So, here the requester would be the remote
                             control and the object that performs the action would be an instance of one of your
                         vendor classes.
                       Sue: How is that possible? How can we decouple them? After all, when I press a button,
                            the remote has to turn on a light.
   Joe                  Joe: You can do that by introducing command objects into your design. A command object                            encapsulates a request to do something (like turn on a light) on a specific object (say, the
                                living room light object). So, if we store a command object for each button, when the
                          button is pressed we ask the command object to do some work. The remote doesn’t have
                        any idea what the work is, it just has a command object that knows how to talk to the right
                             object to get the work done. So, you see, the remote is decoupled from the light object!
                       Sue: This certainly sounds like it’s going in the right direction.
                    Mary: Still, I’m having a hard time wrapping my head around the pattern.
                          Joe: Given that the objects are so decoupled, it’s a little difficult to picture how the pattern
                              actually works.
                    Mary: Let me see if I at least have the right idea: using this pattern, we could create
                       an API in which these command objects can be loaded into button slots, allowing the
                         remote code to stay very simple. And the command objects encapsulate how to do a home
                         automation task along with the object that needs to do it.
                          Joe: Yes, I think so. I also think this pattern can help you with that undo button, but I
                            haven’t studied that part yet.
                    Mary: This sounds really encouraging, but I think I have a bit of work to do to really
                           “get” the pattern.
                       Sue: Me too.


196      Chapter 6


---

## PDF page 235

the command pattern

Meanwhile, back at the Diner...,
     or,
     A brief introduction to the Command Pattern
As Joe said, it is a little hard to understand the Command Pattern by just hearing its
description. But don’t fear, we have some friends ready to help: remember
our friendly diner from Chapter 1? It’s been a while since we visited Alice,
Flo, and the short-order cook, but we’ve got good reason for returning                                                                                      Objectville Diner(beyond the food and great conversation): the diner is going to help us
understand the Command Pattern.
So, let’s take a short detour back to the diner and study the interactions
between the customers, the waitress, the orders, and the short-order
cook. Through these interactions, you’re going to understand the
                                                                                                                     here...objects involved in the Command Pattern and also get a feel for how the             youwere                                                                    Wishdecoupling works. After that, we’re going to knock out that remote control
API.
Checking in at the Objectville Diner...
Okay, we all know how the Diner operates:


                                                                                                withCheese                                                                                               Burger                                                                                     MaltShake


                                                               2 The Waitress
                                                               takes the Order,
  1  You, the Customer,                                          places it on the
     give the Waitress                                             order counter,
     your Order.                                            and says “Order
                                                                       up!”


               3 The Short-Order Cook prepares your meal
                from the Order.

                                                                       you are here 4      197


---

## PDF page 236

the diner

Let’s study the interaction in a little more detail...

...and given this Diner is in Objectville, let’s think about
 the object and method calls involved, too!
                                   of an rder                                           consists                     The Order                                           menu                                         Customer’s                                Slip and the                                          on it.                                 I’ll have a Burger                                         written                          with Cheese and a                            items that are                                                                      Malt Shake.
                           Cheese                     with                 Burger                      Shake                Malt                                  createOrder()


                                                                Here
                                                                          Start
                                                                   The Customer knows
                                                                         what he wants and                           takeOrder()                                           creates an Order.
                                                  The Waitress takes the Order, and when she                                                               gets around to it, she calls its orderUp()                                                       method to begin the Order’s preparation.

                                     orderUp()              all                                                                       The         has                                                                                     Short-Order                                                                   withCheese                                                                 Burger    Order                                                          MaltShake                                                                              CookThe      instructions                                                                                        follows the the      to                                                                                         instructions of the  needed        the                                                                   Order and produces   prepare  Order                                                               the meal.      The                       makeBurger(), makeShake()    meal.         the     directs     Short-Order         with     Cook    like      methods       makeBurger().                                                 output


198      Chapter 6


---

## PDF page 237

the command pattern

The Objectville Diner roles and responsibilities

An Order Slip encapsulates a request to prepare a meal.
                                                                                                                             voidorderUp(){                                                                                                                                         public   Think of the Order Slip as an object that acts as a                                                                                                                                            cook.makeBurger();
   request to prepare a meal. Like any object, it can be passed                                         cook.makeShake();   around—from the Waitress to the order counter, or to the next
    Waitress taking over her shift. It has an interface that consists                      }
    of only one method, orderUp(), that encapsulates the actions
   needed to prepare the meal. It also has a reference to the object
    that needs to prepare it (in our case, the Short-Order Cook). It’s
    encapsulated in that the Waitress doesn’t have to know what’s in
    the Order or even who prepares the meal; she only needs to pass
    the slip through the order window and call “Order up!”                                                               Okay, in real life a                                                              care                                                                                          waitress                                                           what                                                                                  is                                                                                      would                                                              on the                                                                            it, but                                                                                                   probably                                                                           this                                                                             order slip                                                                                   isThe Waitress’s job is to take Order Slips and                                                                            and                                                                            who                                                                                                    cooksinvoke the orderUp() method on them.                                      Objectville...work with us                                                                                                        here!

  The Waitress has it easy: take an Order from the Customer,        Don’t ask me to cook,
   continue helping customers until she makes it back to the        I just take orders and
   order counter, and then invoke the orderUp() method to have       yell “Order up!”
   the meal prepared. As we’ve already discussed, in Objectville, the
    Waitress really isn’t worried about what’s on the Order or who is going
    to prepare it; she just knows Order Slips have an orderUp() method she
   can call to get the job done.
   Now, throughout the day, the Waitress’s takeOrder() method gets
    parameterized with different Order Slips from different customers, but
    that doesn’t faze her; she knows all Order Slips support the orderUp()
   method and she can call orderUp() any time she needs a meal prepared.

The Short-Order Cook has the knowledge
required to prepare the meal.

  The Short-Order Cook is the object that really knows                                                                                        You can definitely
  how to prepare meals. Once the Waitress has invoked                                   say the Waitress and I
    the orderUp() method; the Short-Order Cook takes over and                               are decoupled. She’s not
   implements all the methods that are needed to create meals.                                even my type!
   Notice the Waitress and the Cook are totally decoupled: the
    Waitress has Order Slips that encapsulate the details of the
    meal; she just calls a method on each Order to get it prepared.
    Likewise, the Cook gets his instructions from the Order Slip; he
    never needs to directly communicate with the Waitress.

                                                                       you are here 4      199


---

## PDF page 238

the diner is a model for command pattern


              Okay, we have a Diner with
              a Waitress who is decoupled
            from the Short-Order Cook
             by an Order Slip, so what?
             Get to the point!


                         Patience, we’re getting there...
                             Think of the Diner as a model for an OO design pattern that allows
                                  us to separate an object making a request from the objects that receive
                            and execute those requests. For instance, in our remote control API,
                          we need to separate the code that gets invoked when we press a button
                              from the objects of the vendor-specific classes that carry out those
                                     requests. What if each slot of the remote held an object like the Diner’s
                             Order Slip object? Then, when a button is pressed, we could just call
                                  the equivalent of the orderUp() method on this object and have the
                                         lights turn on without the remote knowing the details of how to make
                                  those things happen or what objects are making them happen.
                            Now, let’s switch gears a bit and map all this Diner talk to the
                       Command Pattern...


     Before we move on, spend some time studying
      the diagram two pages back along with Diner
      roles and responsibilities until you think you’ve
      got a handle on the Objectville Diner objects and
      relationships. Once you’ve done that, get ready
      to nail the Command Pattern!


200      Chapter 6


---

## PDF page 239

the command pattern

From the Diner to the Command Pattern

Okay, we’ve spent enough time in the Objectville Diner that we know all the
personalities and their responsibilities quite well. Now we’re going to rework
the Diner diagram to reflect the Command Pattern. You’ll see that all the
players are the same; only the names have changed.
                                                  The actions and the Receiver
                                                             are bound together in the                                                     command object.                                                                  execute {               object provides               public void The Command        that                    receiver.action1();               execute(),  one method,            the actions and             }   receiver.action2();   encapsulates                   invoke the                                                                       action1()             to                                                                                                                                   action2()      be called   can                                                                                              for                                                                                                                                        ...                                                                                                       responsible                                                                                                                       is                                                                                      Client                                                             The                  Receiver.         on the   actions                                                                                                            object.                                                     eiver                                          Rec                                                                         Command                                                                             the                                                                                  creating
                                                             The command object consists of
                                                                a set of actions on a Receiver.                                  createCommandObject()1
          execute()                                           Here
                                                                   create       Start
                                                                    Command     d   C    omman                                                                    Object()
                        The Client calls                                         setCommand() on                           an Invoker object and passes it the    Client                        Command object, where it gets                              stored until it is needed.                                                  3
                  setCommand()                 2                                           Loading the Invoker
                                                           1  The client creates a                                         setCommand()                   command object.
                 future                                        2  ThesetCommand()client does toa store                   r                          the command object in       pointin           the Command    Invoke   some    callsthe                                                                 the invoker.At                  method...     Invoker the    execute()                                             3  Later...the  object’s                                                                           the invoker clientto executeasks
                                                                                     the command. Note:                                execute()                       ...which results
                                                                      in the actions          as you’ll see later in
    execute()                          action1()     being invoked            the chapter, once the
                                          action2()    on the Receiver.       commandthe invoker,is itloadedmay beinto
                                                                        used                                                                           and                                                                                              discarded,                                                                                                              or it                                               ...   d C                                                                                 remain                                                                                 and be used  omman
                                                                many                                                                                             times.                                 iver                 may                          action1(), action2() Rece

                                                                       you are here 4      201


---

## PDF page 240

who does what


                Match the diner objects and methods with the corresponding names from the
              Command Pattern.

           Diner          Command Pattern

                 Waitress                      Command

                 Short-Order Cook                     execute()

                 orderUp()                              Client

                Order                               Invoker

                Customer                            Receiver

                 takeOrder()                       setCommand()


202      Chapter 6


---

## PDF page 241

the command pattern

Our first command object

Isn’t it about time we built our first command object? Let’s go ahead and write some
code for the remote control. While we haven’t figured out how to design the remote
control API yet, building a few things from the bottom up may help us...


Implementing the Command interface

       First things first: all command objects implement the same interface, which
       consists of one method. In the Diner we called this method orderUp(); however,
    we typically just use the name execute().
      Here’s the Command interface:

       public interface Command {
          public void execute();                                                              Simple. All we need is one method called execute().
      }

Implementing a command to turn a light on
                                                                                                                 Light
     Now, let’s say you want to implement a command for turning a light on.                         on()
      Referring to our set of vendor classes, the Light class has two methods: on()                          off()
     and off(). Here’s how you can implement this as a command:

                                                                             This is a command, so we need to
                                                                             implement the Command interface.
       public class LightOnCommand implements Command {
           Light light;                                      The constructor is passed the specific                                                                                        light that this command is going to
                                                                          control—say the living room light—           public LightOnCommand(Light light) {                                                                     and stashes it in the light instance
               this.light = light;                                        variable. When execute gets called,
           }                                                                    this is the light object that is going
                                                                        to be the receiver of the request.
           public void execute() {  The execute() method calls               light.on();           the on() method on the                                                          object, which is                                                    receiving           }                                                                       controlling.                                        the light we are       }


    Now that you’ve got a LightOnCommand class, let’s see if we can put it to use...

                                                                       you are here 4      203


---

## PDF page 242

using the command object

Using the command object

Okay, let’s make things simple: say we’ve got a remote control with only one
button and corresponding slot to hold a device to control:
                                                                             command,                                           We have one slot to hold our   public class SimpleRemoteControl {            which will control one device.
       Command slot;                                                         We have a method for setting the       public SimpleRemoteControl() {}                                                             command the slot is going to control.
                                                                      This could be called multiple times if the
       public void setCommand(Command command) {             client of this code wanted to change                                                                  the behavior of the remote button.           slot = command;
       }
       public void buttonWasPressed() {                This method is called when the button           slot.execute();                                                                                      is pressed. All we do is take the
       }                                                                current command bound to the slot                                                        and call its execute() method.   }

Creating a simple test to use the Remote Control

Here’s just a bit of code to test out the simple remote control. Let’s take a look and
we’ll point out how the pieces match the Command Pattern diagram:
                                                                      Pattern-speak.                                                 Command                                                                                                                Invoker;                                       This is our Client in                                                                The remote is our                                                                                      command                                                                                       it will be passed a   public class RemoteControlTest {                                         object that can be used to                                                                                                    requests.       public static void main(String[] args) {                       make
           SimpleRemoteControl remote = new SimpleRemoteControl();                                                               Now we create a Light           Light light = new Light();                                                                                            object. This will be the
           LightOnCommand lightOn = new LightOnCommand(light);        Receiver of the request.
                                                                              Here, create a command and           remote.setCommand(lightOn);                                                                                pass the Receiver to it.           remote.buttonWasPressed();
       }                                    Here, pass the command            File Edit  Window Help DinerFoodYum                                      to the Invoker.   }                                                        %java RemoteControlTest
       And then we simulate the                                Light is On
        button being pressed.                 Here’s the output of
                                              running this test code.       %


204      Chapter 6


---

## PDF page 243

the command pattern


                                                                                                GarageDoor
Okay, it’s time for you to implement the
GarageDoorOpenCommand class. First, supply the code for the                               up()
class below. You’ll need the GarageDoor class diagram.                                       down()
                                                                                                                                     stop()
   public class GarageDoorOpenCommand                                                     lightOn()lightOff()
           implements Command {


                                          Your code here

  }

Now that you’ve got your class, what is the output of the
following code? (Hint: the GarageDoor up() method prints out
“Garage Door is Open” when it is complete.)

   public class RemoteControlTest {
       public static void main(String[] args) {
           SimpleRemoteControl remote = new SimpleRemoteControl();
           Light light = new Light();
           GarageDoor garageDoor = new GarageDoor();
           LightOnCommand lightOn = new LightOnCommand(light);
           GarageDoorOpenCommand garageOpen =
               new GarageDoorOpenCommand(garageDoor);

           remote.setCommand(lightOn);
           remote.buttonWasPressed();
           remote.setCommand(garageOpen);
           remote.buttonWasPressed();
       }                                                        File Edit  Window Help GreenEggs&Ham
  }                                 %java RemoteControlTest
         Your output here.


                                                                  you are here 4      205


---

## PDF page 244

command pattern defined

The Command Pattern defined

You’ve done your time in the Objectville Diner, you’ve partly
implemented the remote control API, and in the process you’ve
got a fairly good picture of how the classes and objects interact in
the Command Pattern. Now we’re going to define the Command
Pattern and nail down all the details.                             An encapsulated request.
Let’s start with its official definition:


   The Command Pattern encapsulates a request as an                                                                                                                                action()
     object, thereby letting you parameterize other objects
                                                    Receiver    with different requests, queue or log requests, and
     support undoable operations.                                                                      execute() {
                                                                                                                   receiver.action();
                                                                                                                }
Let’s step through this. We know that a command object          dencapsulates a request by binding together a set of actions on a        Comman
specific receiver. To achieve this, it packages the actions and the
receiver into an object that exposes just one method, execute().
When called, execute() causes the actions to be invoked on the
receiver. From the outside, no other objects really know what
actions get performed on what receiver; they just know that if they
call the execute() method, their request will be serviced.
We’ve also seen a couple examples of parameterizing an object with a
command. Back at the diner, the Waitress was parameterized with                                                                                                                                     execute() en
multiple orders throughout the day. In the simple remote control,                      execute() nd     Op
                                      orwe first loaded the button slot with a “light on” command and     Li                            a  GarageDo                            ghtOnCommthen later replaced it with a “garage door open” command. Like
the Waitress, your remote slot didn’t care what command object it
had, as long as it implemented the Command interface.                                                                        execute()                                  f                                   f
What we haven’t encountered yet is using commands to                                    execute()igh     StereoO
                        Himplement queues and logs and support undo operations. Don’t worry,      C                              eilingFanthose are pretty straightforward extensions of the basic Command
Pattern, and we’ll get to them soon. We can also easily support
what’s known as the Meta Command Pattern once we have the
basics in place. The Meta Command Pattern allows you to create                    lotmacros of commands so that you can execute multiple commands          RemoteS
at once.                                                     An invoker — for instance,
                                                                 one slot of the remote —
                                                                can be parameterized with
                                                                     different requests.


206      Chapter 6


---

## PDF page 245

the command pattern

The Command Pattern defined:
the class diagram

                               The                                              Invoker                                                      holds
                                  a command                                            and                                                 at     Command declares an interface for all commands. As                                                                                                                             its                                                                                              through                                                                                               invoked                                                                                                                          is                                                                    command                                                                 a                                                                        know,                                    some                                                                   already                                              point                                                      asks                                                 the     you                                                                                                    an                                                                                                 perform                                                                                          to                                                                                                     receiver                                                                           a                                                                                            asks                                                                              which                                                                   method,                                 command                                            to                                                               execute()                                                 carry               responsible for              is     Client                                                                                                          undo()                                                                                             anThe                                                                                                  has                                                                                             interface                        and                                                                                             this                                                                                  notice                                                                                      also                                                                                     You’ll                                    out                                     a                                                                      action.                                              request                                              by       a ConcreteCommand                                                                                                         chapter. creating                                                                                          the                                                                                                  later in                                                                        a bit                                                                                 cover                                                                                                we’ll                                                                     which                                                calling                                                      its                                                          method,                                                 execute()             Receiver.         its setting                                    method.


             Client                                      Invoker                                     <<interface>>
                                                                       Command
                                            setCommand()                                  execute()                                                                                                undo()                  The execute()
                                                                                   method invokes
                                                                                     the action(s)
                                                                                      on the receiver
                                                                                          needed to fulfill
                                                      Receiver                         ConcreteCommand           the request.
                                                           action()                                                                                                    execute()
                                                                                                undo()

                                                                                       public void execute() {
        The Receiver knows how to                                                        receiver.action()
          perform the work needed to                                                 }
          carry out the request. Any class          can act as a Receiver.                                        defines a binding between an                                              ConcreteCommand                                     The                                               and a Receiver. The Invoker makes a requestcarriesbyit                                                 action                                                            the ConcreteCommand                                                       and                                                       execute()                                                          calling                                                                              actions on the Receiver.                                                         or more                                                                   calling one                                           out by


            How does the design of the Command Pattern support the decoupling
                    of the invoker of a request and the receiver of the request?


                                                                       you are here 4      207


---

## PDF page 246

where do we begin?


                                                        Okay, I think I’ve got a good
                                                             feel for the Command Pattern now.
                                                   Great tip, Joe, I think we’re going to
                                                           look like superstars after finishing off
                                                    the Remote Control API.


           Mary: Me too. So where do we begin?
            Sue: Like we did in the SimpleRemote, we need to provide a
            way to assign commands to slots. In our case we have seven slots,
              each with an on and off button. So we might assign commands to
               the remote something like this:
            onCommands[0] = onCommand;
            offCommands[0] = offCommand;
            and so on for each of the seven command slots.
           Mary: That makes sense, except for the Light objects. How does
               the remote know the living room from the kitchen light?
            Sue: Ah, that’s just it—it doesn’t! The remote doesn’t know
              anything but how to call execute() on the corresponding
           command object when a button is pressed.
           Mary: Yeah, I sorta got that, but in the implementation, how do
           we make sure the right objects are turning on and off the right
               devices?
            Sue: When we create the commands to be loaded into the
              remote, we create one LightCommand that is bound to the living
            room light object and another that is bound to the kitchen light
                object. Remember, the receiver of the request gets bound to
               the command it’s encapsulated in. So, by the time the button is
                pressed, no one cares which light is which; the right thing just
             happens when the execute() method is called.
           Mary: I think I’ve got it. Let’s implement the remote and I think
                  this will get clearer!
            Sue: Sounds good. Let’s give it a shot...


208      Chapter 6


---

## PDF page 247

the command pattern

Assigning Commands to slots

So we have a plan: we’re going to assign a command to each slot in the
remote control. This makes the remote control our invoker. When a button
is pressed, the execute() method will be called on the corresponding
command, which results in actions being invoked on the receiver (like
lights, ceiling fans, and stereos).

      (1) Each slot gets a command.
                                                                    (2) When the button is pressed, the
                                                                         execute() method is called on the
                                                 execute()                        nd                                corresponding command.               a           Light                 On Comm
                                   execute()                   nd            a         m       LightOn Com

                                                                                                                                          execute()                             execute()                                                                                      and                                    m        Hi         gh                      Light                                                Of fCom      Ce            ilingFan

                                                                                                                                                  execute()                          execute()                 en                                                                                          and
        Op      Ga                                  LightOf fComm           rageDoor
                  CD                                                                                                 execute() f                                execute() or                                                        Of         F                       CeilingFan        StereoOn
  We’ll worry about the                                                                                                         execute() ol
                                          rC  remaining slots in a bit.                           GarageDoose

                                                                                                                                  execute()
                                 ff                                 StereoO

                                                                                     (3) In the execute() method,
                                                                                        actions are invoked on the receiver.   In our code you’ll find that each
  command name has “Command”         The Invoker
  appended to it, but in print,
  we’ve unfortunately run out of
  space for a few of them.                                                                       off()
                                                                                                   on()
                                  Stereo


                                                                       you are here 4      209


---

## PDF page 248

implementing the remote control

Implementing the Remote Control
  public class RemoteControl {                   This time around, the remote is going                                                    to handle seven On and Off commands,      Command[] onCommands;                                                         which we’ll hold in corresponding arrays.      Command[] offCommands;
                                                                               In the constructor, all we need to      public RemoteControl() {                                                          do is instantiate and initialize the          onCommands = new Command[7];                                                      On and Off arrays.
          offCommands = new Command[7];

          Command noCommand = new NoCommand();
          for (int i = 0; i < 7; i++) {
              onCommands[i] = noCommand;
              offCommands[i] = noCommand;           The setCommand() method takes a slot
          }                                                           position and an On and Off command to
                                                              be stored in that slot.      }

      public void setCommand(int slot, Command onCommand, Command offCommand) {
          onCommands[slot] = onCommand;
          offCommands[slot] = offCommand;                  It puts these commands in the
      }                                                 On and Off arrays for later use.

      public void onButtonWasPushed(int slot) {
          onCommands[slot].execute();
                                                              When an On or Off button is      }                                                                                  pressed, the hardware takes
                                                                          care of calling the corresponding      public void offButtonWasPushed(int slot) {                                                                   methods onButtonWasPushed() or
          offCommands[slot].execute();                         offButtonWasPushed().
      }

      public String toString() {
          StringBuffer stringBuff = new StringBuffer();
          stringBuff.append("\n------ Remote Control -------\n");
          for (int i = 0; i < onCommands.length; i++) {
              stringBuff.append("[slot " + i + "] " + onCommands[i].getClass().getName()
                  + "    " + offCommands[i].getClass().getName() + "\n");
          }
          return stringBuff.toString();             We override toString() to print out each slot and
      }                                                                      its corresponding command. You’ll see us use this
                                                            when we test the remote control.  }

210      Chapter 6


---

## PDF page 249

the command pattern

Implementing the Commands

Well, we’ve already gotten our feet wet implementing the LightOnCommand for the
SimpleRemoteControl. We can plug that same code in here and everything works
beautifully. Off commands are no different; in fact, the LightOffCommand looks like this:
      public class LightOffCommand implements Command {
          Light light;

          public LightOffCommand(Light light) {
              this.light = light;
          }                                       The LightOffCommand works exactly
                                                           the same way as the LightOnCommand,
                                                             except that we’re binding the receiver to          public void execute() {                                                           a different action: the off() method.
              light.off();
          }
      }
                                                                                                         Stereo
Let’s try something a little more challenging; how about writing on and off                           on()
                                                                                                                                                                      off()commands for the Stereo? Okay, off is easy, we just bind the Stereo to the off()                                                                                                                             setCd()
method in the StereoOffCommand. On is a little more complicated; let’s say we                  setDvd()
want to write a StereoOnWithCDCommand...                                                               setRadio()
                                                                                                                         setVolume()
      public class StereoOnWithCDCommand implements Command {
          Stereo stereo;
                                                                                    we          public StereoOnWithCDCommand(Stereo stereo) {    Just like the LightOnCommand,              this.stereo = stereo;                           get passed the instance of the stereo
          }                                                              we’re going to be controlling and we                                                                              store it in an instance variable.
          public void execute() {
              stereo.on();
                                                 To carry out this request, we need to call three              stereo.setCD();                                                  methods on the stereo: first, turn it on, then set              stereo.setVolume(11);            it to play the CD, and finally set the volume to 11.          }                                Why 11? Well, it’s better than 10, right?
      }

Not too bad. Take a look at the rest of the vendor classes; by now, you can definitely
knock out the rest of the Command classes we need for those.

                                                                       you are here 4      211


---

## PDF page 250

testing the remote control

Putting the Remote Control through its paces

Our job with the remote is pretty much done; all we need to do is run some tests and get
some documentation together to describe the API. Home Automation or Bust, Inc., sure
is going to be impressed, don’t ya think? We’ve managed to come up with a design
that will allow them to produce a remote that is easy to maintain, and they’re going
to have no trouble convincing the vendors to write some simple command classes in
the future since those are so easy to write.
Let’s get to testing this code!

 public class RemoteLoader {
    public static void main(String[] args) {
        RemoteControl remoteControl = new RemoteControl();
        Light livingRoomLight = new Light("Living Room");           Create all the devices in                                                                                                               locations.        Light kitchenLight = new Light("Kitchen");                     their proper        CeilingFan ceilingFan = new CeilingFan("Living Room");
        GarageDoor garageDoor = new GarageDoor("Garage");
        Stereo stereo = new Stereo("Living Room");
        LightOnCommand livingRoomLightOn =
                new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff =                  Create all the Light
                new LightOffCommand(livingRoomLight);      Command objects.
        LightOnCommand kitchenLightOn =
                new LightOnCommand(kitchenLight);
        LightOffCommand kitchenLightOff =
                new LightOffCommand(kitchenLight);
        CeilingFanOnCommand                            ceilingFanOn =                                                                   Create the On and Off                new CeilingFanOnCommand(ceilingFan);        CeilingFanOffCommand ceilingFanOff =                 for the ceiling fan.
                new CeilingFanOffCommand(ceilingFan);
        GarageDoorUpCommand garageDoorUp =
                new GarageDoorUpCommand(garageDoor);        Create the Up and Down
        GarageDoorDownCommand garageDoorDown =               commands for the Garage.
                new GarageDoorDownCommand(garageDoor);
        StereoOnWithCDCommand stereoOnWithCD =
                new StereoOnWithCDCommand(stereo);      Create the stereo On
        StereoOffCommand stereoOff =                      and Off commands.
                new StereoOffCommand(stereo);


212      Chapter 6


---

## PDF page 251

the command pattern


        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff);
                                                                        Now that we’ve got        remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff);
                                                                                                                                    all our commands, we        remoteControl.setCommand(3, stereoOnWithCD, stereoOff);
                                                                                           can load them into
                                                                                       the remote slots.        System.out.println(remoteControl);
        remoteControl.onButtonWasPushed(0);                                                                            Here’s where we use our toString() method
        remoteControl.offButtonWasPushed(0);                                                               to print each remote slot and the command
        remoteControl.onButtonWasPushed(1);                                                                            assigned to it. (Note that toString() gets
        remoteControl.offButtonWasPushed(1);                                                                              called automatically here, so we don’t have
        remoteControl.onButtonWasPushed(2);                                                               to call toString() explicitly.)
        remoteControl.offButtonWasPushed(2);
        remoteControl.onButtonWasPushed(3);                                                                           All right, we are ready to roll!        remoteControl.offButtonWasPushed(3);                                                          Now, we step through each slot    }                                                          and push its On and Off buttons.}


Now, let’s check out the execution of our remote control test...


   File Edit  Window Help CommandsGetThingsDone
  % java RemoteLoader
 ------ Remote Control -------
  [slot 0] LightOnCommand            LightOffCommand
  [slot 1] LightOnCommand            LightOffCommand
  [slot 2] CeilingFanOnCommand       CeilingFanOffCommand
  [slot 3] StereoOnWithCDCommand     StereoOffCommand
  [slot 4] NoCommand                 NoCommand
  [slot 5] NoCommand                 NoCommand
  [slot 6] NoCommand                 NoCommand
                 On slots   Off slots
  Living Room light is on
  Living Room light is off
  Kitchen light is on
  Kitchen          light               is off                                                Our commands in action! Remember, the output  Living         Room              ceiling                     fan is on high                                               from each device comes from the vendor classes.  Living Room ceiling fan is off
  Living Room stereo is on                                                  For instance, when a light object is turned on, it  Living Room stereo is set for CD input              prints “Living Room light is on.”
  Living Room stereo volume set to 11
  Living Room stereo is off
  %


                                                                       you are here 4      213


---

## PDF page 252

null object


                  Wait a second, what’s
                   with that NoCommand
                    that’s loaded in slots 4
                 through 6? Trying to pull a
                    fast one?

                             Good catch. We did sneak a little something in there. In the remote
                                           control, we didn’t want to check to see if a command was loaded every
                                     time we referenced a slot. For instance, in the onButtonWasPushed()
                                   method, we would need code like this:

                                     public void onButtonWasPushed(int slot) {
                                         if (onCommands[slot] != null) {
                                             onCommands[slot].execute();
                                        }
                                    }

                                       So, how do we get around that? Implement a command that does nothing!
                                     public class NoCommand implements Command {
                                         public void execute() { }
                                    }

                                  Then, in our RemoteControl constructor, we assign every slot a
                           NoCommand object by default and we know we’ll always have some
                             command to call in each slot.
                                     Command noCommand = new NoCommand();
                                     for (int i = 0; i < 7; i++) {
                                         onCommands[i] = noCommand;
                                         offCommands[i] = noCommand;
                                    }

                                       So, in the output of our test run, you’re seeing only slots that have been
                                       assigned to a command other than the default NoCommand object,
                                  which we assigned when we created the RemoteControl constructor.

                          The NoCommand object is an example of a null object. A null object is useful when
            HeadHonorableFirst   Pattern        you don’t have a meaningful object to return, and yet you want to remove the
                Mention   Honorable      responsibility for handling null from the client. For instance, in our remote control we
         Mention         didn’t have a meaningful object to assign to each slot out of the box, so we provided
                            a NoCommand object that acts as a surrogate and does nothing when its execute()
                           method is called.
                                     You’ll find uses for Null Objects in conjunction with many Design Patterns, and
                            sometimes you’ll even see “Null Object” listed as a Design Pattern.


214      Chapter 6


---

## PDF page 253

the command pattern

Time to write that documentation...


                                                                    Inc.                                                       Bust,                                                 or                                  Automation                        Home                                for                     Design                  API           Control   Remote                                                                         Home                                                                                            your                                                                                                            for                                                                                              interface                                                              programming                                                                 application                                                and                                                 design                                           following                                     the                                                                                                       so that                                with                          you                                                                                                   as possible                      present                    to                                                                                          as simple                                                                          code            pleased         are                                                                                  control    We                                                               remote                                                                 the                                                       keep                                                            to                                               was                                                  goal                                           design                                                                                                                  to                                   primary                                                                                                              Pattern                            Our                          Control.                                                                      Command                                                                                         the              Remote                                                                       employed                                                                      have     Automation                                                       we                                                           end                                                                              this                                                          To                                                   produced.                                                    are                                                classes                                 vendor                                                                                                           of producing                              as new                                                                                                     cost                                                                                           the                    changes                                                                                  reduce               require                                                                                                      will                                                                                             this       doesn’t        it                                                                            believe                                                We                                                                     Classes.                                                Vendor                                                 the                                         from                                              class                        RemoteControl                      the             decouple       logically                                                                              costs.                                                  maintenance                                          ongoing                                        your                                 reduce                              drastically                       as                    well                as        remote     the
     The following class diagram provides an overview of our design:
                                       The RemoteControl class manages a set of
                                 Command objects, one per button. When a button
                                                               is pressed, the corresponding ButtonWasPushed()
                                     method is called, which invokes the execute()
                                      method on the command. That is the full extent of                                                                                    invoking                                                                                                                               it’s                                                                                  classes                                                                        of the                                                   knowledge                                                   remote’s                                                                                           commands                               a         the                             creates                                                                                               RemoteControl                                                                                                                         All            RemoteLoader         The                                                                                from                                                                         remote                                                                            the                                                                 decouples                                                               object                                      Command                                               the                                              as                                                                                                           the Command                               objects                                                                                         implement                   of Command        number                                                                                      work.                                                                        automation                                                     home                                                            the actual                                                    doing                                                                                                                                 of one                                                       classes                                             the                                                                                                                             consists                                      slots                                                                                                 which                            the                           into                                                                                                                   interface,               are loaded           that
           of the Remote Control. Each                                                         method: execute(). Commands
        command object encapsulates                                                            encapsulate a set of actions on a
         a request of a home                                                                                  specific vendor class. The remote
          automation device.                                                                        invokes these actions by calling
                                                                                                 the execute() method.


                                                          RemoteControl                                 <<interface>>Command                  RemoteLoader
                                                  onCommands                                      execute()
                                                       offCommands
                                                                setCommand()
                                                                  onButtonWasPushed()
                                                                     offButtonWasPushed()
                                                                                       LightOnCommand                                                                       Light
                                                                           on()                                      execute()LightOffCommand
                                                                                               off()
                                                                                                                                 execute()
                                                                                                           public void execute() {
                                                                                                               light.on()
                                                                                                }  public void execute() {
                                                                                                        light.off()
                                                                                         }


            The Vendor Classes are used to perform
                                                of                                   work                           automation                  home                   actual                                                                                                                 action             the                                                                                               each                                                                                   implement                                                                   we                                                                                              Interface,                                                    Command                                                                  the                                          using                                               the          Using                                 Here, we’re                           devices.                                                                                                remote               controlling                                                                                                    the                                                                                  on                                                                                        button                                                                                   a                                                                                      pressing                                                                      by                                                                     invoked                                                           be                                                            can                                                                  that                            example.                       an                        as                                                                                                              holds                      class               Light                                                                                                            object                                                                      Command                                                                                 The                                                                                              object.                                                       Command                                                                   simple                                                             a                                                            with                                                                                                                         Class                                                                                               Vendor                                                                                              a                                                                                                           of                                                                                                instance                                                                              an                                                                                                                          is                                                                                         that                                                                                object                                                                 an                                                                          to                                                                  reference                                                        a                                                                                                               or more                                                                                         one                                                                                                                             calls                                                                                                       that                                                                         method                                                                                     execute()                                                                   an                                                            implements                                                     and
                                                     methods on that object. Here we show two such classes
                                                                  that turn a light on and off, respectively.


                                                                       you are here 4      215


---

## PDF page 254

represent commands with lambdas


   Want to take your Command Pattern coding to the next level? You can use Java’s lambda expressions
    to skip the step of creating all those concrete command objects. With lambda expressions, instead of
     instantiating the concrete command objects, you can use function objects in their place. In other words,
   we can use a function object as a command. And, while we’re at it, we can delete all those concrete
   Command classes, too.
     Let’s take a look at how you’d use lambda expressions as commands to simplify our previous code:
   The updated code, using lambda expressions:
     public class RemoteLoader {
        public static void main(String[] args) {           RemoteControl remoteControl = new RemoteControl();   We create the Light                                                                                object like normal...
           Light livingRoomLight = new Light("Living Room");                                                                              But we can remove           ...
            LightOnCommand livingRoomLightOn =                                 the concrete                                new LightOnCommand(livingRoomLight);     LightOnCommand and
            LightOffCommand livingRoomLightOff =                           LightOffCommand                                new LightOffCommand(livingRoomLight);    objects.
           ...            remoteControl.setCommand(0,() -> livingRoomLight.on(),                                     () -> livingRoomLight.off());
            ...                                              Instead we'll write the concrete commands as lambda
        }    Later, when you click one of the remote’s       expressions that do the same work as the concrete
     }         buttons, the remote calls the execute()        command’s execute() method was doing: that is, turning
               method of the command object in the         the light on or turning the light off.
                    slot for that button, which is represented
                by this lambda expression.
    Once we’ve replaced the concrete commands with lambda expressions, we can delete all those
      concrete command classes (LightOnCommand, LightOffCommand, HottubOnCommand,
     HottubOffCommand, etc.). If you do this for every concrete command, you’ll reduce the total number
      of classes in the remote control application from 22 to 9.
     Note that you can only do this if your Command interface has one abstract method. As soon as we add a
      second abstract method, the lambda shorthand no longer works.
        If you like this technique, check out your favorite Java reference for more information on the lambda
       expression.

216      Chapter 6


---

## PDF page 255

the command pattern


                                             Great job; it looks like
                                              you’ve come up with a terrific
                                              design, but aren’t you forgetting one
                                                        little thing the customer asked for?
                                       LIKE THE UNDO BUTTON?!


              Whoops! We almost forgot...luckily, once
            we have our basic Command classes,
              undo is easy to add. Let’s step through
                adding undo to our commands and to the
               remote control...


What are we doing?

Okay, we need to add functionality to support the undo button on the remote. It works like
this: say the Living Room Light is off and you press the on button on the remote. Obviously
the light turns on. Now if you press the undo button, then the last action will be reversed—in
this case, the light will turn off. Before we get into more complex examples, let’s get the light
working with the undo button:

    1  When commands support undo, they have an undo() method that mirrors the execute()
          method. Whatever execute() last did, undo() reverses. So, before we can add undo to our
         commands, we need to add an undo() method to the Command interface:

            public interface Command {
                public void execute();
                public void undo();           Here’s the new undo() method.
            }

         That was simple enough.
        Now, let’s dive into the Light commands and implement the undo() method.


                                                                       you are here 4      217


---

## PDF page 256

implementing undo


       2    Let’s start with the LightOnCommand: if the LightOnCommand’s execute() method
            was called, then the on() method was last called. We know that undo() needs to do the
              opposite of this by calling the off() method.

                 public class LightOnCommand implements Command {
                     Light light;
                     public LightOnCommand(Light light) {
                         this.light = light;
                     }
                     public void execute() {
                         light.on();
                     }
                                                                      turns the light                                                               execute()                     public void undo() {                                                                   on, so undo() simply turns                         light.off();                                                       the light back off.                     }
                 }

              Piece of cake! Now for the LightOffCommand. Here the undo() method just
             needs to call the Light’s on() method.

                 public class LightOffCommand implements Command {
                     Light light;
                     public LightOffCommand(Light light) {
                         this.light = light;
                     }
                     public void execute() {
                         light.off();
                     }
                     public void undo() {                                             And here, undo() turns                         light.on();             the light back on.                     }
                 }

            Could this be any easier? Okay, we aren’t done yet; we need to work a little
             support into the Remote Control to handle tracking the last button pressed
            and the undo button press.

218      Chapter 6


---

## PDF page 257

the command pattern


3   To add support for the undo button, we only have to make a few small changes to the Remote
    Control class. Here’s how we’re going to do it: we’ll add a new instance variable to track the last
   command invoked; then, whenever the undo button is pressed, we retrieve that command and
     invoke its undo() method.
    public class RemoteControlWithUndo {
        Command[] onCommands;                                                        This is where we’ll stash the last        Command[] offCommands;                  command executed for the undo button.        Command undoCommand;
        public RemoteControlWithUndo() {
            onCommands = new Command[7];
            offCommands = new Command[7];
            Command noCommand = new NoCommand();
            for(int i=0;i<7;i++) {
                onCommands[i] = noCommand;              Just like the other slots, undo
                offCommands[i] = noCommand;             starts off with a noCommand, so
            }                                                         pressing undo before any other
            undoCommand = noCommand;                     button won’t do anything at all.
        }
        public void setCommand(int slot, Command onCommand, Command offCommand) {
            onCommands[slot] = onCommand;
            offCommands[slot] = offCommand;
        }
                                                             When a button is pressed, we take        public void onButtonWasPushed(int slot) {                                                                    the command and first execute            onCommands[slot].execute();                                                                                                     it; then we save a reference to            undoCommand = onCommands[slot];                                                                                       it in the undoCommand instance        }                                                                                         variable. We do this for both on
                                                                  commands and off commands.        public void offButtonWasPushed(int slot) {
            offCommands[slot].execute();
            undoCommand = offCommands[slot];
        }
                                                         When the undo button is pressed, we
        public void undoButtonWasPushed() {               invoke the undo() method of the
            undoCommand.undo();                        command stored in undoCommand.
        }                                                        This undoes the operation of the last
                                                          command executed.
        public String toString() {
            // toString code here...                                              Update to add undoCommands.        }
    }


                                                                    you are here 4      219


---

## PDF page 258

test drive undo

Time to QA that Undo button!

Okay, let’s rework the test harness a bit to test the undo button:
 public class RemoteLoader {
     public static void main(String[] args) {
         RemoteControlWithUndo remoteControl = new RemoteControlWithUndo();
         Light livingRoomLight = new Light("Living Room");   Create a Light, and our new undo()                                                                             enabled Light On and Off Commands.         LightOnCommand livingRoomLightOn =
                 new LightOnCommand(livingRoomLight);
         LightOffCommand livingRoomLightOff =
                 new LightOffCommand(livingRoomLight);
         remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
                                                         Add the light Commands         remoteControl.onButtonWasPushed(0);                                                                      to the remote in slot 0.         remoteControl.offButtonWasPushed(0);
         System.out.println(remoteControl);             Turn the light on, then         remoteControl.undoButtonWasPushed();                                                                       off, and then undo.         remoteControl.offButtonWasPushed(0);
         remoteControl.onButtonWasPushed(0);
         System.out.println(remoteControl);                                                             Then, turn the light off, back on, and undo.         remoteControl.undoButtonWasPushed();
     }
}
And here are the test results...

                                         File Edit  Window Help UndoCommandsDefyEntropy
                      % java RemoteLoader
                     Light is on         Turn the light on, then off.                     Light is off
                                                                                       Here are the Light commands.                    ------ Remote Control -------
                     [slot 0] LightOnCommand        LightOffCommand
                     [slot 1] NoCommand             NoCommand
                     [slot 2] NoCommand             NoCommand
                     [slot 3] NoCommand             NoCommand
                     [slot 4] NoCommand             NoCommand
                     [slot 5] NoCommand             NoCommand
                     [slot 6] NoCommand             NoCommand
                     [undo] LightOffCommand
                                        Undo was pressed... the LightOffCommand      Now undo holds the                     Light is on                                                 undo() turns the light back on.                LightOffCommand, the                     Light is off                                                                  last command invoked.                     Light is on        Then we turn the light off and back on.
                    ------ Remote Control -------
                     [slot 0] LightOnCommand        LightOffCommand
                     [slot 1] NoCommand             NoCommand
                     [slot 2] NoCommand             NoCommand
                     [slot 3] NoCommand             NoCommand
                     [slot 4] NoCommand             NoCommand
                     [slot 5] NoCommand             NoCommand
                     [slot 6] NoCommand             NoCommand
                     [undo] LightOnCommand
                                                                       Now undo holds the LightOnCommand, the last                     Light is off     Undo was pressed, so the light is back off.                                                                                command invoked.

220      Chapter 6


---

## PDF page 259

the command pattern

Using state to implement Undo

Okay, implementing undo on the Light was instructive but a little too easy. Typically,                                                                                                                                     CeilingFan
we need to manage a bit of state to implement undo. Let’s try something a little more
interesting, like the CeilingFan from the vendor classes. The CeilingFan class allows a               high()
                                                                                                                                   medium()number of speeds to be set along with an off method.                                                                                                                                                             low()
Here’s the source code for the CeilingFan class:                                                                                              off()
                                                                                                                                            getSpeed()
 public class CeilingFan {
     public static final int HIGH = 3;
     public static final int MEDIUM = 2;            Notice that the CeilingFan class
     public static final int LOW = 1;                  holds local state representing the
     public static final int OFF = 0;                 speed of the ceiling fan.
     String location;
     int speed;
     public CeilingFan(String location) {
         this.location = location;
         speed = OFF;
     }                                             Hmm, so to properly
                                                             implement undo, I’d have
     public void high() {                                to take the previous speed of
         speed = HIGH;                                 the ceiling fan into account...
         // code to set fan to high
     }
     public void medium() {
         speed = MEDIUM;
         // code to set fan to medium
     }
                                                   These methods set the     public void low() {
                                                         speed of the ceiling fan.         speed = LOW;
         // code to set fan to low
     }
     public void off() {
         speed = OFF;
         // code to turn fan off
     }
                                                      current     public int getSpeed() {     We can get the                                                    fan                                                                  ceiling         return speed;              speed of the     }                                      using getSpeed().
 }

                                                                       you are here 4      221


---

## PDF page 260

add undo to the ceiling fan

Adding Undo to the Ceiling Fan commands

Now let’s tackle adding undo to the various Ceiling Fan commands. To
do so, we need to track the last speed setting of the fan and, if the undo()
method is called, restore the fan to its previous setting. Here’s the code for
the CeilingFanHighCommand:
   public class CeilingFanHighCommand implements Command {          We’ve added local state to                                                                                                            previous      CeilingFan ceilingFan;                                           keep track of the      int prevSpeed;                                                       speed of the fan.
      public CeilingFanHighCommand(CeilingFan ceilingFan) {
          this.ceilingFan = ceilingFan;
      }                                                                                      In execute(), before we
                                                                                 change the speed of the
      public void execute() {                                                 fan, we need to first
          prevSpeed = ceilingFan.getSpeed();                         record its previous state,
                                                                                            just in case we need to          ceilingFan.high();                                                                              undo our actions.      }
      public void undo() {
          if (prevSpeed == CeilingFan.HIGH) {                        To undo, we set the
              ceilingFan.high();                                             speed of the fan back
          } else if (prevSpeed == CeilingFan.MEDIUM) {              to its previous speed.              ceilingFan.medium();
          } else if (prevSpeed == CeilingFan.LOW) {
              ceilingFan.low();
          } else if (prevSpeed == CeilingFan.OFF) {
              ceilingFan.off();
          }
      }
  }


                           We’ve got three more ceiling fan commands to write: low,
                            medium, and off. Can you see how these are implemented?


222      Chapter 6


---

## PDF page 261

the command pattern

Get ready to test the ceiling fan


Time to load up our remote control with the ceiling fan
commands. We’re going to load slot 0’s on button with the
medium setting for the fan and slot 1 with the high setting.
Both corresponding off buttons will hold the ceiling fan off
command.


Here’s our test script:


  public class RemoteLoader {

      public static void main(String[] args) {
          RemoteControlWithUndo remoteControl = new RemoteControlWithUndo();

          CeilingFan ceilingFan = new CeilingFan("Living Room");

          CeilingFanMediumCommand ceilingFanMedium =
                  new CeilingFanMediumCommand(ceilingFan);       Here we instantiate three
          CeilingFanHighCommand ceilingFanHigh =                    commands: medium, high, and off.
                  new CeilingFanHighCommand(ceilingFan);
          CeilingFanOffCommand ceilingFanOff =
                  new CeilingFanOffCommand(ceilingFan);                     Here we put medium in
                                                                                                     slot 0, and high in slot
                                                                                                                               1. We also load up the          remoteControl.setCommand(0, ceilingFanMedium, ceilingFanOff);                                                                                 off command.          remoteControl.setCommand(1, ceilingFanHigh, ceilingFanOff);
          remoteControl.onButtonWasPushed(0);               First, turn the fan on medium.
          remoteControl.offButtonWasPushed(0);          Then turn it off.
          System.out.println(remoteControl);                                                                 Undo! It should go back to medium...          remoteControl.undoButtonWasPushed();
          remoteControl.onButtonWasPushed(1);             Turn it on to high this time.
          System.out.println(remoteControl);              And, one more undo; it should go back
          remoteControl.undoButtonWasPushed();            to medium.
      }
  }


                                                                       you are here 4      223


---

## PDF page 262

test drive the ceiling fan

Testing the ceiling fan...


Okay, let’s fire up the remote, load it with commands, and push some buttons!


   File Edit  Window Help UndoThis! v
  % java RemoteLoader
                                               Turn the ceiling fan on  Living Room ceiling fan is on medium                                                  medium, then turn it off.  Living Room ceiling fan is off
                                                                           commands  ------ Remote Control -------                                     Here are the
  [slot 0] CeilingFanMediumCommand    CeilingFanOffCommand             in the remote control...
  [slot 1] CeilingFanHighCommand      CeilingFanOffCommand
  [slot 2] NoCommand                  NoCommand
  [slot 3] NoCommand                  NoCommand
  [slot 4] NoCommand                  NoCommand
  [slot 5] NoCommand                  NoCommand                         ...and undo has the last command
  [slot 6] NoCommand                  NoCommand                     executed, the CeilingFanOffCommand,
  [undo] CeilingFanOffCommand                                      with the previous speed of medium.
  Living Room ceiling fan is on medium         Undo the last command, and it goes back to medium.
  Living Room ceiling fan is on high
                                         Now, turn it on high.
  ------ Remote Control -------
  [slot 0] CeilingFanMediumCommand    CeilingFanOffCommand
  [slot 1] CeilingFanHighCommand      CeilingFanOffCommand
  [slot 2] NoCommand                  NoCommand
  [slot 3] NoCommand                  NoCommand
  [slot 4] NoCommand                  NoCommand
  [slot 5] NoCommand                  NoCommand
  [slot 6] NoCommand                  NoCommand
  [undo] CeilingFanHighCommand                            Now, high is the last
                                                     command executed.
  Living Room ceiling fan is on medium
                                        One more undo, and the ceiling
                                            fan goes back to medium speed.  %


224      Chapter 6


---

## PDF page 263

the command pattern

                                                                                                                                        Stereo

                                                                                                                                                                on()Every remote needs a Party Mode!                                                                                                                                                                                                          off()
                                                                                                                                                        setCd()                         TV
What’s the point of having a remote if you                                               setDvd()
can’t push one button and have the lights                                                  setRadio()                    on()off()
dimmed, the stereo and TV turned on, and                                             setVolume()                  setInputChannel()                                                                                                                        Hottub
the hot tub fired up?                                                                                                                              setVolume()
                                                                                                                                                 on()
                                                                                                                                                                                       off()                                Light
                                                                                                                                                                  circulate()                                                                                                                                                                               on()
                                                                                                                                                 jetsOn()                                                                                                                                                                                                                             off()
                                                                                                                                                                    jetsOff()                    dim()
              Hmm, our remote                                                                    setTemperature()
                  control would need a
                button for each device, so
               I don’t think we can do this.
                                                             Hold on, Sue, don’t be
                                                               so sure. I think we can do
                                                                       this without changing the
                                                          remote at all!


                                       Mary’s idea is to make a new
                                           kind of Command that can
                                        execute other Commands...
                                     and more than one of them!
                                      Pretty good idea, huh?

        public class MacroCommand implements Command {
           Command[] commands;
           public MacroCommand(Command[] commands) {
               this.commands = commands;                                                          Take an array of Commands and store           }                                                    them in the MacroCommand.
           public void execute() {
               for (int i = 0; i < commands.length; i++) {
                   commands[i].execute();
               }
           }                           When the macro gets executed by the remote,
       }                                     execute those commands one at a time.

                                                                       you are here 4      225


---

## PDF page 264

create a macro command

Using a macro command

Let’s step through how we use a macro command:

    1   First we create the set of commands we want to go into the macro:
                                                                       Create all the devices: a light,
            Light light = new Light("Living Room");             tv, stereo, and hot tub.
            TV tv = new TV("Living Room");
            Stereo stereo = new Stereo("Living Room");
            Hottub hottub = new Hottub();                          Now create all the On                                                                              commands to control them.
            LightOnCommand lightOn = new LightOnCommand(light);
            StereoOnCommand stereoOn = new StereoOnCommand(stereo);
            TVOnCommand tvOn = new TVOnCommand(tv);
             HottubOnCommand hottubOn = new HottubOnCommand(hottub);


                                                         We’ll also need commands for the off buttons.
                                                  Write the code to create those here:


                                                                                    Create an array for    2  Next we create two arrays, one for the On commands and one for the Off                                                                      On commands and
       commands, and load them with the corresponding commands:                    an array for Off
                                                                                               commands...            Command[] partyOn = { lightOn, stereoOn, tvOn, hottubOn};
            Command[] partyOff = { lightOff, stereoOff, tvOff, hottubOff};
                                                                                                                   ...and  create two             MacroCommand partyOnMacro = new MacroCommand(partyOn);                                                                                                  corresponding macros
             MacroCommand partyOffMacro = new MacroCommand(partyOff);      to hold them.
    3  Then we assign MacroCommand to a button like we always do:                       Assign the macro
                                                                             command to a button as            remoteControl.setCommand(0, partyOnMacro, partyOffMacro);                                                                                         you would any command.


226      Chapter 6


---

## PDF page 265

the command pattern


  4    Finally, we just need to push some buttons and see if this works.
           System.out.println(remoteControl);
           System.out.println("--- Pushing Macro On---");
                                                                                            Here’s the output.           remoteControl.onButtonWasPushed(0);
           System.out.println("--- Pushing Macro Off---");
           remoteControl.offButtonWasPushed(0);


 File Edit  Window Help You Can’tBeatABabka
 % java RemoteLoader                        Here are the two macro commands.
------ Remote Control -------
[slot 0] MacroCommand    MacroCommand
[slot 1] NoCommand       NoCommand
[slot 2] NoCommand       NoCommand
[slot 3] NoCommand       NoCommand
[slot 4] NoCommand       NoCommand
[slot 5] NoCommand       NoCommand
[slot 6] NoCommand       NoCommand
[undo] NoCommand
                                                                   All the Commands in the--- Pushing Macro On---                                                  macro are executed when we
 Light is on                                             invoke the on macro...
 Living Room stereo is on
 Living Room TV is on
 Living Room TV channel is set for DVD
 Hottub is heating to a steaming 104 degrees
 Hottub is bubbling!
                                                               ...and when we invoke the off
                                                   macro. Looks like it works.--- Pushing Macro Off---
 Light is off
 Living Room stereo is off
 Living Room TV is off
 Hottub is cooling to 98 degrees


                                                                    you are here 4      227


---

## PDF page 266

exercise with macro commands


                  The only thing our MacroCommand is missing is its undo functionality. When the undo
                       button is pressed after a macro command, all the commands that were invoked in the
                   macro must undo their previous actions. Here’s the code for MacroCommand; go ahead
                   and implement the undo() method:
                 public class MacroCommand implements Command {
                     Command[] commands;
                     public MacroCommand(Command[] commands) {
                         this.commands = commands;
                     }
                     public void execute() {
                         for (int i = 0; i < commands.length; i++) {
                             commands[i].execute();
                         }
                     }
                     public void undo() {


                     }
                 }


     Do I always need a receiver? Why        How can I implement a history             Could I have just implementedQ:               Q:               Q:
can’t the command object implement the     of undo operations? In other words, I        party mode as a Command by creating
details of the execute() method?           want to be able to press the undo button    a PartyCommand and putting the calls
                                              multiple times.                               to execute the other Commands in
       In general, we strive for “dumb”                                              PartyCommand’s execute() method?A:command objects that just invoke an action          Great question. It’s pretty easy                 A:on a receiver; however, there are many           actually; instead of keeping just a reference         You could; however, you’d essentially                                   A:examples of “smart” command objects            to the last Command executed, you keep      be “hardcoding” the party mode into
 that implement most, if not all, of the logic      a stack of previous commands. Then,         PartyCommand. Why go to the trouble?
needed to carry out a request. Certainly you    whenever undo is pressed, your invoker        With MacroCommand, you can decide
can do this; just keep in mind you’ll no longer   pops the first item off the stack and calls its     dynamically which Commands you want to
have the same level of decoupling between     undo() method.                           go into PartyCommand, so you have more
 the invoker and receiver, nor will you be                                                                          flexibility using MacroCommands. In general,
able to parameterize your commands with                                         MacroCommand is a more elegant solution
 receivers.                                                                       and requires less new code.

228      Chapter 6


---

## PDF page 267

the command pattern

More uses of the Command Pattern: queuing requests

Commands give us a way to package a piece of
computation (a receiver and a set of actions) and pass
it around as a first-class object. Now, the computation
itself may be invoked long after some client application
creates the command object. In fact, it may even be                                           Commands
invoked by a different thread. We can take this scenario
                                                                                                                                                        on
                                                                                                                                                                                                                                                                                                     execute()                                                                    Dand    apply                it             to           many                      useful                             applications,                                     such                                              as                                                                                                                                       is                                                                                                                                       utati                                                                              tr                                                                                            i                                                                                      b                                                                                                                        omp                                                                                                             u                                                                                                                                                          t                                                                                                                                                                                                    edC                                                                                                                                                                                             est                                                                     theschedulers,           thread                   pools,                    and                            job                               queues,                                          to                                name                                                                                                                                                                                                                                                                                    execute()                                                                                                             qu                                                                      implementing                                                               e                                           a few.       Objects                                                                                                                                                                                                                                                                                                                   execute()                                                             D                                                                                 o                                                                         are                                                                                                      adR                                                                                                 w                                                                                                                                                                                                 nlo                                                                        interface                                                                                                                                                                                                                        ion                                                                                                                                                                                                                                                                                                   execute()                                                   command                                                                  NeImagine        a          job             queue:                  you                     add                      commands                                           to                                           the                                                                                                                                         tworkFetch                                                                                 at                                                                        Fi                                                                             n                                                                                 a                                                                                     n                                                            the queue.                                                                                                     c                                                                                                                                                                                                                                                                                     execute()                                                                                                                                                               i                                                                                           mput                                                                                                                                                                                  Co                                                                                                                                                     a                                                                                                                                                                                                                                                                                                                                               l                                                    added toqueue     on        one             end,               and                  on                          the                             other                              end sits                                      a                                       group                                                                                                                  sk                                                               C                                                                       o                                                                                                         Tar                                                                          m                                                                                                                                                                                                                                                                         ile                                                                                                                                            p                                                                                                                                                                                                                                                                         execute()of threads. Threads run the following script: they
                                                                                  RayTrace                                                                                                                                                                                                                                            execute()remove a command from the queue, call its execute()                                                            rTask                                                   Ne                                                                                                         tworkFetch Cexecute()ompeilmethod, wait               for the                         call                         to finish,                           and                                   then discard the                                                                                                                  on
                                                            tati                                                                                                                                              est                                                      Financexecute()ialCompucommand           object              and                       retrieve                          a new                                   one.                                                                                                                                                                                                             execute()                                                                                  qu                                                                       queue                                             Do                                                                        wnloadRe                                                                                                                                                                                                    execute()        Job
                                                                                                                                                                                       execute() CompileTarsk
                                                        RayTrace
                                                                                          on
                                               tati                                          Financexecute()ialCompu
                                                                              This gives us an effective way
                                                                         to limit computation to a
                                                                             fixed number of threads.

                Threads remove commands
                                          rTask               from the queue one by one             Compeil                                execute()                            call their                and                                                                                                                                                                                                                                                                          execute()
                                                         Ne                        Once complete,                                                                                                                      tworkFetch                 method.
                 they go back for a new                                                                                                execute()        Thread
                                                                                                                                                                       est                command object.                                                                                                                                                                                                                                                    execute()execute()                                Thread       RayTrace                                                        equ                                        Thread   DownloadR
                                                    Threads computing   Thread
                                                                      jobs
Note that the job queue classes are totally decoupled from
the objects that are doing the computation. One minute a
thread may be computing a financial computation, and the
next it may be retrieving something from the network. The
job queue objects don’t care; they just retrieve commands                                                How might a web server make
and call execute(). Likewise, as long as you put objects into                                                           use of such a queue? What other
the queue that implement the Command Pattern, your                                                                        applications can you think of?
execute() method will be invoked when a thread is available.

                                                                       you are here 4      229


---

## PDF page 268

using the command pattern for logging requests

More uses of the Command Pattern: logging requests

The semantics of some applications require that we log all actions and be able to
recover after a crash by reinvoking those actions. The Command Pattern can support
these semantics with the addition of two methods: store() and load(). In Java we could
use object serialization to implement these methods, but the normal caveats for using
serialization for persistence apply.
                                                                                                                                                      <<interface>>How does this work? As we execute commands, we store a history of them on disk.              Command
When a crash occurs, we reload the command objects and invoke their execute()                 execute()
methods in batch and in order.                                                                                        undo()
                                                                                                                                                           store()
Now, this kind of logging wouldn’t make sense for a remote control; however, there            load()
are many applications that invoke actions on large data structures that can’t be
quickly saved each time a change is made. By using logging, we can save all the
operations since the last checkpoint, and if there is a system failure, apply those
operations to our checkpoint. Take, for example, a spreadsheet application: we might
want to implement our failure recovery by logging the actions on the spreadsheet rather
than writing a copy of the spreadsheet to disk every time a change occurs. In more
advanced applications, these techniques can be extended to apply to sets of operations         We add two methods
in a transactional manner so that all of the operations complete, or none of them do.           for logging.


                                                               execute()                                                               store()     store
                                                               load()
                m                   mandOne                        1.execute()   Co                                        2. execute()            store
                                                                execute()                                                                                               system                                                                         a                                                                            After                                                               load()                                                                                                       are                                                                                                         objects                                                                                      the                                        store                                                                                                             failure,                         3.execute()  Comstore()                       mandTwo   Invoker                                                                                                 executed                                                                                     and                                                                                          reloaded                                            Crash!
                                                               execute()
                                                               store()                                                                                                     in the correct order.                                                               load()
            Comm                                 andThree                                         Restore

      As each command
         is executed, it is                                                                                                                                                         execute()
                                                                                                                                                                                                                 store()        stored on disk.                                           ne     1.                                                                         load   Commload()andO
                                                                                                                                                                                                                    execute()
                                                                                         load                execute()
                                                                                                                                                                                                              store()             2. execute()
                                         wo                                                                          load  Comload()mandT                                                                                                                                                             3.execute()                                                Invoker                                                                                                                                                                                                           execute()
                                                                                                                                                                                                           store()
                                              hree                                         Commload()andT

230      Chapter 6


---

## PDF page 269

the command pattern

Command Pattern in the Real World

Remember the little life-changing application from Chapter 2?
In that chapter we saw how Java’s Swing
library is chock full of Observers in the                                                       Here’s our fancy interface.
form of ActionListeners that listen in (or                                                               And here’s the output when                                                                                                           we click on the button.observe) events on user interface components.
Well, it turns out that ActionListener  is
not just an Observer interface, it’s also a
Command interface, and our AngelListener
and DevilListener classes are not just
Observers, but also concrete Commands.                                                                                        File Edit Window Help HeMadeMeDoIt
                                                                                              Devil answer       %java SwingObserverExampleThat’s right, we have two patterns in one                                              Come on, do it!
example!                                                                              Angel answer     Don’t do it, you might regret it!
                                                                                             %


                                           Here’s the code (the important bits anyway) for the little life-changing
                                         application from Chapter 2. See if you can identify who is the Client, who are
                                      the Commands, who is the Invoker, and who is the Receiver.

     public class SwingObserverExample {
           // Set up ...
             JButton button = new JButton("Should I do it?");
             button.addActionListener(new AngelListener());
             button.addActionListener(new DevilListener());
            // Set frame properties here
        }
         class AngelListener implements ActionListener {
             public void actionPerformed(ActionEvent event) {
                 System.out.println("Don't do it, you might regret it!");
            }
        }
         class DevilListener implements ActionListener {
             public void actionPerformed(ActionEvent event) {
                 System.out.println("Come on, do it!");
            }
        }
    }


                                                                       you are here 4      231


---

## PDF page 270

exercise solution


                                            Here’s the code (the important bits anyway) for the little life-changing
                                          application from Chapter 2. See if you can identify who is the Client, who are
                                       the Commands, who is the Invoker, and who is the Receiver?

                                            Here’s our solution.
                                           The button is our Invoker. The button                                                                                                     (like                                                     the actionPerformed()                                                                     calls                                                                                      (the                                                                       commands                                                                                    in the                                                            methods                                                         execute())   public class SwingObserverExample {                                                                            the button.                                                                                              click                                                                         you                                                               when                                                          ActionListeners)          // Set up ...

           JButton button = new JButton("Should I do it?");
           button.addActionListener(new AngelListener());
           button.addActionListener(new DevilListener());
                                                         The Client is the class that sets up the
           // Set frame properties here                      Swing components and sets the commands
       }                                                               (AngelListener and DevilListener) in the                                                                            Invoker (the Button).
       class AngelListener implements ActionListener {
           public void actionPerformed(ActionEvent event) {
               System.out.println("Don't do it, you might regret it!");
           }                                                                  ActionListener is the Command
       }                                                                              Interface: it has one method,
                                                                                  actionPerformed() that, like
                                                                                       execute(), is executed when the       class DevilListener implements ActionListener {                                                                      command is invoked.
           public void actionPerformed(ActionEvent event) {
               System.out.println("Come on, do it!");
           }
       }
                                                                          AngelListener and DevilListener   }                                                                          are our concrete Commands. They
                                                                        implement the command interface (in         The Receiver in this example is the System object.                                                                                   this case, ActionListener).           Remember, invoking a command results in actions on          the Receiver. In a typical Swing application this would             result in calling actions on other components in the UI.


232      Chapter 6


---

## PDF page 271

the command pattern

        Tools for your Design Toolbox
            Your toolbox is starting to get heavy! In this chapter                The Command Pattern
             we’ve added a pattern that allows us to encapsulate                       decouples an object making
            methods into Command objects: store them, pass them                 a request from the one that
             around, and invoke them when you need them.                       knows how to perform it.
                                                               A Command object is at the
                                                                                             center of this decoupling and
                                                                                        encapsulates a receiver with
                                                                              an action (or set of actions).                Basics        OO                                                               An invoker makes a request
                             Abstraction                                                        of a Command object by       Principles OO                                                                                               calling its execute() method,                               Encapsulation             what varies.     Encapsulate                                                                        which invokes those actions                     over inheritance.Polymorphism                                        on the receiver.     Favor composition                       not     Inheritance                                  Invokers can be            to interfaces,      Program                                                                            parameterized with       implementations.                                 designs                                               Commands, even                        coupled            for loosely                                                                       dynamically at runtime.        Strive        that interact.                 objects        between                                                               Commands may support                                  extension                 be open for                should                                                              undo by implementing an          Classes                 for modification.        but closed                                                                         undo() method that restores                                                           decouple an                                                                                             the object to its previous              on abstractions. Do not        When you need to                                                    from         Depend                                   classes.                                                         requests                    concrete                                                                                                 before                                                                                                         the                                                                                                             execute()                                              making                                         object          depend on                                                        to                 state                                                   how                                                 know                                              that                                                                              method                                                                               was                                                                                                                              last                                                                                                                           called.                                    the objects                                                         the                                                              use                                           the requests,                                       perform                         MacroCommands are a                                                   Pattern.                                  Command                                                                                          simple extension of the
                                                                  Command Pattern that   Patterns                                   algorithms,OO                      of                                                                                               allow                                                                                                          multiple                                                                                 commands                        family              a                       one-to-many               a      -               defines         -                 defines                          themadditional Strategy                            that           -                                                                                                        to                                                                                be                                                                                                  invoked.                                                                                                             Likewise,                  and                 Attach                          so-                               Provide   Observer                                 an                   one,                       makesobjects            each                                    algorithm                                  dynamically.                               Define              Factory                                     its              between    Decorator                                        has                        object                    -all                            lets  encapsulates                 an                             ofonly                                                                       MacroCommands                                                                                                can easily               to                            state,the             Method                                    families                                   but                 Strategy    dependency                                       class      Abstract                     a                                   use                   changes                                              it.object,                         creating               -                           that        Factory                          an                         Ensure                  for        responsibilities                             flexible                                            point               a   interchangeable.                            updated                             clients        one                                 without                         creating                                          global                      and                                                                                           support                                                                                                        undo().                from            interface                            a request                 provide                                to    when                  for             objectSingleton       an                                 extending                                         classa                            objectsprovide                          for              are            interface                  -which                     and      Decoratorsindependently                                 Encapsulates                  depedentnotified   vary             or                        decide                       subclassing                                        you                                        classes.                   instance              to     dependents          related                                         lets            one           Command                                         letting                  subclasses                        concrete                                                                         let                         Method                              it.        alternative                                                                                                        In                                                                                                          practice,                                                                                                                                                                 it’s                                                                                                            not                   their                             thereby                   to                       Factory                  access                          object,      automatically                                           different           specifying           of                                 the                 an                             to                 as                                   with              instantiate.        functionality.                                    clients                                                                      uncommon                                                                                                                             for                                                                                                              “smart”                                       and                            instantiation                                            requests,                  deferparameterize        a class                           queue or log                subclasses.requests,         operations.                                  Command objects to                            undoable                                                    implement the request                    support                                                                                      themselves rather than
                                                                                              delegating to a receiver.
                                                               Commands may also be
                                                                                used to implement logging
                                                                              and transactional systems.


                                                                     you are here 4      233


---

## PDF page 272

design patterns crossword

            Design Patterns Crossword
                      Time to take a breather and let it all sink in.
                                  It’s another crossword; all of the solution words are from
                             this chapter.

                                              1

              2             3                               4

              5


                       6


     7                               8                      9


          10                                                                                        11

     12                                                                      13

                                                                     14       15


                       16                                                                           17


ACROSS                          DOWN
5. Our favorite city.                                              1. The Cook and this person were definitely decoupled.
6. Company that got us word-of-mouth business.               2. The Waitress didn’t do this.
7. Role of customer in the Command Pattern.                   3. A command encapsulates this.
9. Object that knows the actions and the receiver.              4. Act as the receivers in the remote control (two words).
12. Invoker and receiver are _________.                        8. Object that knows how to get things done.
15. The Waitress was one.                                   10. Carries out a request.
16. Dr. Seuss diner food (four words).                          11. All commands provide this.
17. Another thing Command can do.                          13. Our first command object controlled this.
                                                            14. A command __________ a set of actions and a
                                                                   receiver.

234      Chapter 6


---

## PDF page 273

the command pattern

                        SOlUTion

                              Match the diner objects and methods with the corresponding
                              names from the Command Pattern.
                             Diner                   Command Pattern
                              Waitress                       Command

                             Short-Order Cook                       execute()

                             orderUp()                                Client

                           Order                                Invoker

                           Customer                              Receiver

                             takeOrder()                        setCommand()


Here’s the code for the GarageDoorOpenCommand class.
public class GarageDoorOpenCommand implements Command {
    GarageDoor garageDoor;
    public GarageDoorOpenCommand(GarageDoor garageDoor) {
        this.garageDoor = garageDoor;
    }
    public void execute() {
        garageDoor.up();
    }
}
Here’s the output:

  File Edit  Window Help GreenEggs&Ham
 %java RemoteControlTest
 Light is on
 Garage Door is Open
 %


                                                                   you are here 4      235


---

## PDF page 274

exercise solutions

                               public class MacroCommand implements Command {
                                   Command[] commands;
                                   public MacroCommand(Command[] commands) {
                                       this.commands = commands;
                                   }
                                   public void execute() {
                                       for (int i = 0; i < commands.length; i++) {
         Here is the undo()                      commands[i].execute();
                                       }         method for the                                   }
         MacroCommand.               public void undo() {
                                       for (int i = commands.length - 1; i >= 0; i--) {
                                           commands[i].undo();
                                       }
                                   }
                               }


      Here’s the code to create commands for the off button.
    LightOffCommand lightOff = new LightOffCommand(light);
    StereoOffCommand stereoOff = new StereoOffCommand(stereo);
    TVOffCommand tvOff = new TVOffCommand(tv);
    HottubOffCommand hottubOff = new HottubOffCommand(hottub);


                                                                    1                          W
                                    2             3                               4                         C        R         A       V
                                    5                   O  B  J  E  C  T  V  I  L  L  E
                   O     Q          T      N
                        K      U           R       D
                                             6                  W  E  A  T H  E  R   -  O   -  R  A M A
                             S         S        R
                           7                               8                      9                   C  L  I  E N  T     R    S        C O M M A N  D
                                      E               L
                                10                                                                                        11                     R                 C           A                         E
                           12                                                                      13                D  E  C O U  P  L  E  D         S            L            X
                                                                                           14       15                      C                   I            S     B      I N  V O  K  E  R
                     E                V              E      I     G              C
                                             16                                                                           17                        I       G  R  E  E N  E  G  G  S A N  D H A M      U N  D O
                    V                R                 D    T            T
                     E                                 S                   E
                     R

236      Chapter 6
