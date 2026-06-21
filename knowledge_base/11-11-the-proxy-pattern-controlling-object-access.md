# 11: the Proxy Pattern: Controlling Object Access

_Extracted from PDF pages 463-530. Text only; images and diagrams are not embedded._


---

## PDF page 463

11 the Proxy Pattern
      Controlling
        ObjectAccess


 With you as my proxy,
 I’ll be able to triple the
amount of lunch money I can
extract from friends!


          Ever play good cop, bad cop? You’re the good cop and you provide all
                your services in a nice and friendly manner, but you don’t want everyone asking you
                    for services, so you have the bad cop control access to you. That’s what proxies do:
                  control and manage access. As you’re going to see, there are lots of ways in which
                 proxies stand in for the objects they proxy. Proxies have been known to haul entire
              method calls over the internet for their proxied objects; they’ve also been known to
                  patiently stand in for some pretty lazy objects.


                                                                                 this is a new chapter      425


---

## PDF page 464

what’s the goal


                         Hey team, I’d really like to
                             get some better monitoring for
                     my gumball machines. Can you find a
                        way to get me a report of inventory
                          and machine state?


                             Sounds easy enough. If you remember, we’ve already
                                  got methods in the gumball machine code for getting the
                                count of gumballs, getCount(), and getting the current
                                        state of the machine, getState().
                                     All we need to do is create a report that can be printed out
                            and sent back to the CEO. Hmmm, we should probably
                            add a location field to each gumball machine as well; that
                           way the CEO can keep the machines straight.
Remember the CEO of              Let’swith ajustveryjumpfast inturnaround.and code this. We’ll impress the CEO
Mighty Gumball, Inc.?


426      Chapter 11


---

## PDF page 465

the proxy pattern

Coding the Monitor

Let’s start by adding support to the GumballMachine class so that it
can handle locations:
  public class GumballMachine {                 A location is just a String.      // other instance variables
      String location;

      public GumballMachine(String location, int count) {
          // other constructor code here               The location is passed into the
          this.location = location;                          constructor and stored in the      }                                                                  instance variable.

      public String getLocation() {
          return location;
      }                                                     Let’s also add a getter method to                                                           grab the location when we need it.
      // other methods here
  }

Now let’s create another class, GumballMonitor, that retrieves the machine’s
location, inventory of gumballs, and current machine state and prints them in a
nice little report:

  public class GumballMonitor {
      GumballMachine machine;                                                        The monitor takes the machine in                                                                                   its constructor and assigns it to                                                                the machine instance variable.      public GumballMonitor(GumballMachine machine) {
          this.machine = machine;
      }

      public void report() {
          System.out.println("Gumball Machine: " + machine.getLocation());
          System.out.println("Current inventory: " + machine.getCount() + " gumballs");
          System.out.println("Current state: " + machine.getState());
      }
  }
           Our report() method just prints a report with               location, inventory, and the machine’s state.


                                                                       you are here 4      427


---

## PDF page 466

local gumball monitor

Testing the Monitor

We implemented that in no time. The CEO is going to be thrilled and amazed by our
development skills.
Now we just need to instantiate a GumballMonitor and give it a machine to monitor:
  public class GumballMachineTestDrive {
      public static void main(String[] args) {               Pass in a location and initial # of
          int count = 0;                                             gumballs on the command line.
         if (args.length < 2) {
              System.out.println("GumballMachine <name> <inventory>");
              System.exit(1);                                                                                    Don’t forget to give         }                                                                      the constructor a
                                                                                                    location and count...          count = Integer.parseInt(args[1]);
          GumballMachine gumballMachine = new GumballMachine(args[0], count);
          GumballMonitor monitor = new GumballMonitor(gumballMachine);
                                                                                     ...and instantiate a monitor and pass it a                                                                     machine to provide a report on.
         // rest of test code here                                                                                            File Edit  Window Help FlyingFish
          monitor.report();              %java GumballMachineTestDrive Austin 112
     }                                 Gumball Machine: Austin               When we need a report on }                                     Current Inventory: 112 gumballs                 the machine, we call the                                       Current State: waiting for quarter                   report() method.


                  The                               monitor                                       output                                                 looks
                          great,                            but                               I guess                                     I wasn’t                                                          clear. I need                 And here’s the output!
                       to monitor gumball machines REMOTELY!
                     In fact, we already have the networks in
                        place for monitoring. Come on guys, you’re
                      supposed to be the internet generation!


428      Chapter 11


---

## PDF page 467

the proxy pattern


                                                                              Don’t worry, guys, I’ve
                                                                   been brushing up on my design
         Well, that will teach us to                                          patterns. All we need is a remote
       gather some requirements                                      proxy and we’ll be ready to go.
      before we jump in and code. I hope
     we don’t have to start over...


                                        Frank        Jim     Joe
Frank: A remote what?
Joe: Remote proxy. Think about it: we’ve already got the monitor code written, right? We give the
GumballMonitor class a reference to a machine and it gives us a report. The problem is that the monitor runs
in the same JVM as the gumball machine and the CEO wants to sit at his desk and remotely monitor the
machines! So what if we left our GumballMonitor class as is, but handed it a proxy to a remote object?
Frank: I’m not sure I get it.
Jim: Me neither.
Joe: Let’s start at the beginning...a proxy is a stand in for a real object. In this case, the proxy acts just like it
is a Gumball Machine object, but behind the scenes it is communicating over the network to talk to the real,
remote GumballMachine.
Jim: So you’re saying we keep our code as it is, and we give the monitor a reference to a proxy version of the
GumballMachine...
Frank: And this proxy pretends it’s the real object, but it’s really just communicating over the net to the real
object.
Joe: Yeah, that’s pretty much the story.
Frank: It sounds like something that’s easier said than done.
Joe: Perhaps, but I don’t think it’ll be that bad. We have to make sure that the gumball machine can act as
a service and accept requests over the network; we also need to give our monitor a way to get a reference to
a proxy object, but we’ve got some great tools already built into Java to help us. Let’s talk a little more about
remote proxies first...

                                                                       you are here 4      429


---

## PDF page 468

remote proxy

The role of the ‘remote proxy’

A remote proxy acts as a local representative to a remote object. What’s a “remote
object”? It’s an object that lives in the heap of a different Java Virtual Machine
(or more generally, a remote object that is running in a different address space).
What’s a “local representative”? It’s an object that you can call local methods on
and have them forwarded on to the remote object.


                                                                             Remote                                                       to                                                                                                 Gumball Machine                                                       pretends   CEO’s desktop                                    The proxy                                                                                     with                                                                         a JVM.                                                                 object,                                        be the remote                                         but it’s just a stand in
                                           for the Real Thing.        Remote Heap                           Local Heap


                         ne
                                             hi         Gumball     the Here                          c                           a         the client       G          is           or  Proxy       Gumball M Monitor                     it’s         umball Monti           thinks        it object;       to the Real talking         machine, but                                                        IS  gumball                                                                        object                 talking                                                                         the                                                               Remote                                                                                                It’s                                                   The   it’s really just                                                                               Thing.  to the proxy, which                                          the Real   the method                                                                      with                                                                        the                                                                            does  then talks to the                                                     object              machine        Same as your old                       that actually   Real gumball           network.            code, only it’s                               real work.   over the                                to a proxy.                                  talking
                         The client object is the object
                               making use of the proxy-in our
                                    case, the GumballMonitor class.

         Your client object acts like it’s making remote method calls.
         But what it’s really doing is calling methods on a heap-
          local “proxy” object that handles all the low-level details of
         network communication.


430      Chapter 11


---

## PDF page 469

the proxy pattern


              This is a pretty slick idea.
      We’re going to write some code that
    takes a method invocation, somehow transfers it
   over the network, and invokes the same method
on a remote object. Then I presume when the call is
complete, the result gets sent back over the network
  to our client. But it seems to me this code is going
     to be very tricky to write.


                                                     Hold on now, we aren’t going
                                                      to write that code ourselves; it’s
                                                     pretty much built into Java’s remote
                                                        invocation functionality. All we have to
                                              do is retrofit our code so that it takes
                                                    advantage of RMI.


Before going further, think about how you’d design a system to enable Remote Method
Invocation (RMI). How would you make it easy on the developer so that she has to write as
little code as possible? How would you make the remote invocation look seamless?


       2


Should making remote calls be totally transparent? Is that a good idea? What might be a
problem with that approach?


                                                                 you are here 4      431


---

## PDF page 470

rmi detour

Adding a remote proxy to the Gumball
Machine monitoring code

On paper our plan looks good, but how do we create a proxy that knows how to invoke a
method on an object that lives in another JVM?
Hmmm. Well, you can’t get a reference to something on another heap, right? In other words,
you can’t say:
       Duck d = <object in another heap>
Whatever the variable d is referencing must be in the same heap space as the code running
the statement. So how do we approach this? Well, that’s where Java’s Remote Method
Invocation (RMI) comes in...RMI gives us a way to find objects in a remote JVM and allows
us to invoke their methods.
Now might be a good time to brush up on RMI with your favorite Java reference, or you can
take the RMI Detour ahead, and we’ll walk you though the high points of RMI before adding
the proxy support to the Gumball Machine code.
In either case, here’s our plan:

    1   First, we’re going to take the RMI
        Detour and explore RMI. Even if you are
         familiar with RMI, you might want to
         follow along and check out the scenery.
                                     An RMI Detour
    2  Then we’re going to take our Gumball
       Machine and make it a remote service
        that provides a set of methods calls                      If you’re new to RMI,
        that can be invoked remotely.                              take the detour that runs
                                                                             over the next few pages;
                                                                                otherwise, you might want to
                                                                                   just quickly thumb through    3   Finally, we going to create a proxy that                                                                         the detour as a review. If
       can talk to a remote Gumball Machine,                                                                                    you’d like to continue on,
        again using RMI, and put the monitoring                   just getting the gist of the
       system back together so that the CEO can              remote proxy, that is fine
        monitor any number of remote machines.               too—you can skip the detour.


432      Chapter 11


---

## PDF page 471

the proxy pattern


Remote methods 101                                                            An RMI Detour
                                                    pretends          this design...                     Client helper Consider                                                           service, but                                  to be the                                                   it’s just a proxy for the         Server heap
                         Client heap   Real Thing.


             thinks      object                                               elperClient                               rviceh            the         to             Client helper    Se    talking                        Serviceobjectit’s            It      Service.        Client object Real
 thinks the client                                                                               object IS                                                                                      the             thing                                                                                             Service                                                                                                                  It’s         is the                                                              The                                                              Service helper                                                                       helper                                                                        gets                                                                     the                                                                                                        Service.              do                                                                                   Real           actually                                                                                      method      can                                                                      the                                        going                                                             request                                            is that                                                                               the                                                        from the                              This                                                                                      client                                                                                   with                                                                                    the         work.                                                                                     object                                   our                                                                    helper,                                                                                          does the real                                                                   unpacks                           to be                                                                                               it,                                                                  and                                                                                                     actually                                                                          that                                 proxy.                        calls the method on the                                                                                        work.                                                          Real Service.                      real

Walking through the design
Let’s say we want to design a system that allows us to call a local object that forwards each request
to a remote object. How would we design it? We’d need a couple of helper objects that do the
communicating for us. The helpers make it possible for the client to act as though it’s calling a method
on a local object (which it is). The client calls a method on the client helper, as if the client helper were
the actual service. The client helper then takes care of forwarding that request for us.
In other words, the client object thinks it’s calling a method on the remote service, because the client
helper is pretending to be the service object—that is, pretending to be the thing with the method the
client wants to call.
But the client helper isn’t really the remote service. Although the client helper acts like it (because it has
the same method that the service is advertising), the client helper doesn’t have any of the method logic
the client is expecting. Instead, the client helper contacts the server, transfers information about the
method call (e.g., name of the method, arguments, etc.), and waits for a return from the server.
On the server side, the service helper receives the request from the client helper (through a Socket
connection), unpacks the information about the call, and then invokes the real method on the real service
object. So, to the service object, the call is local. It’s coming from the service helper, not a remote client.
The service helper gets the return value from the service, packs it up, and ships it back (over a Socket’s
output stream) to the client helper. The client helper unpacks the information and returns the value to
the client object.
Let’s walk through this to make it clearer...

                                                                       you are here 4      433


---

## PDF page 472

remote method invocation

How the method call happens

 1  The Client object calls doBigThing() on the client helper object.

                                                    Server heap              Client heap

                        doBigThing()


                   er                                       elp                          rviceh         Client helper    Se                     Serviceobject
    Client object


 2  The Client helper packages up information about the call
     (arguments, method name, etc.) and ships it over the
     network to the service helper.

                                                     Server heap               Client heap                                        “client wants to call a method”

                         doBigThing()

                    er                                        elp                          rviceh         Client helper    Se                     Serviceobject
    Client object


 3  The Service helper unpacks the information from the client
     helper, finds out which method to call (and on which object),
     and invokes the real method on the real service object.
                                                     Server heap               Client heap                                        “client wants to call a method”
                                                                     doBigThing()
                         doBigThing()                                                                     this is the                                                                                 Remember,                                                                                        object with the REAL                  r                                     logic. The one                                                                            method                                        elpe                                                                              that does the real work!                          rviceh         Client helper    Se                     Serviceobject
    Client object

434      Chapter 11


---

## PDF page 473

the proxy pattern


4  The method is invoked on the service object, which returns                           An RMI Detour
   some result to the service helper.
                                                   Server heap             Client heap

                                                                       result

                   er                                      elp                         rviceh        Client helper    Se                    Serviceobject
   Client object


5  The Service helper packages up information returned from the
    call and ships it back over the network to the client helper.


                                                   Server heap              Client heap
                                   packaged up result


                   er                                       elp                         rviceh        Client helper    Se                     Serviceobject
   Client object


6  The Client helper unpackages the returned values and returns
   them to the client object. To the client object, this was all
    transparent.

                                                   Server heap              Client heap

                         result

                   er                                       elp                         rviceh        Client helper    Se                     Serviceobject
   Client object

                                                                     you are here 4      435


---

## PDF page 474

rmi: the big picture

Java RMI, the Big Picture                                                                                            An RMI Detour
Okay, you’ve got the gist of how remote methods work;     There is one difference between RMI calls and local
now you just need to understand how to use RMI.           (normal) method calls. Remember that even though to
                                                           the client it looks like the method call is local, the clientWhat RMI does for you is build the client and service                                                           helper sends the method call across the network. Sohelper objects, right down to creating a client helper                                                            there is networking and I/O. And what do we knowobject with the same methods as the remote service. The                                                      about networking and I/O methods?nice thing about RMI is that you don’t have to write
any of the networking or I/O code yourself. With your      They’re risky! They can fail! And so they throw
client, you call remote methods (i.e., the ones the Real       exceptions all over the place. As a result, the client does
Service has) just like normal method calls on objects        have to acknowledge the risk. We’ll see how in a few
running in the client’s own local JVM.                       pages.
RMI also provides all the runtime infrastructure to make
it all work, including a lookup service that the client can
use to find and access the remote objects.


RMI nomenclature: in RMI, the client helper is a “stub” and the
service helper is a “skeleton.”

                                        This is going
                                    to act as our
                                          proxy!                Server heap                    Client heap

                                   RMI SKELETON                     RMI STUB
                           ct                       Serviceobje                                            elper                             rviceh           Client helper    Se
      Client object


Now let’s go through all the steps needed to make an object
into a service that can accept remote calls and also the steps
needed to allow a client to make remote calls.
You might want to make sure your seat belt is fastened; there
are a lot of steps—but nothing to be too worried about.


436      Chapter 11


---

## PDF page 475

the proxy pattern

Making the Remote service
                                                                                           An RMI Detour
This is an overview of the five steps for making the remote service—in other
words, the steps needed to take an ordinary object and supercharge it so it can
be called by a remote client. We’ll be doing this later to our Gumball Machine.
For now, let’s get the steps down and then we’ll explain each one in detail.
                                                                  the                                                                            defines
                                                                                                                                                                                                                                       interfaceStep one:                                                                                                                                                               public                                                                      you
                                                                                                                                                             MyRemote                                                                     interface  that                                                                                                                                                                                                        extends     This                                                                                                                                                                  Remote                                                                                                                                                                                                                                                                                                 { }    Make a Remote Interface                                 methods                                                        remote    to call.                                                                            clients    The remote interface defines the methods that             want                                                           MyService.java
     a client can call remotely. It’s what the client
       will use as the class type for your service. Both
      the Stub and actual service will implement
        this.
                                                                                                       class                                                                           the                                                                                      Service:                                                                       Real                                                     TheStep two:                                                                                                                                                                     public                                                                                                                                                                                                                                            interface                                                                         do                                                                                                                                                                 MyRemote                                                                                                                                                                                                             extends                                                                            that                                                                     methods                                                                                                                                                                      Remote                                                                                                                                                                                                                                                                                                         { }                                                                 the                                                                with                                                                                     implements    Make a Remote Implementation                         the real work. It
     This is the class that does the Real Work. It                    the remote interface.                                                          MyServiceImpl.java
      has the real implementation of the remote
     methods defined in the remote interface.
         It’s the object that the client wants to call
     methods on (e.g., GumballMachine).

Step three:
     Start the RMI registry (rmiregistry)                    File Edit  Window Help Drink
     The rmiregistry is like the white pages of a phone                                 Run this in a separate                                            %rmiregistry                                                                                             terminal window.      book. It’s where the client goes to get the proxy
       (the client stub/helper object).


Step four:
     Start the remote service                                                                                                                    File Edit  Window Help BeMerry                      101101                                                                                                                                                                                 10 110 1
     You have to get the service object up and running. Your     %java MyServiceImpl                  00010011110010       service implementation class instantiates an instance
       of the service and registers it with the RMI registry.                                               Stub    101101
                                                                                                                                                                                           0                                                                                                                                                                                              11                                                                                                                                                                                                0      Registering it makes the service available for clients.                                                                                           10 110 1                                                                                                                                                                                             001                                                                                                                                                                                                10
                                                                                                                                                                                             001 01
                                                                                                                      Skeleton                                                         The Stub and Skeleton are
                                                                       generated dynamically for you                                                                         behind the scenes.

                                                                       you are here 4      437


---

## PDF page 476

make a remote interface

Step one: make a Remote interface
                                                                                            An RMI Detour

 1  Extend java.rmi.Remote
     Remote is a “marker” interface, which means it has no methods. It has
       special meaning for RMI, though, so you must follow this rule. Notice that
     we say “extends” here. One interface is allowed to extend another interface.                                                                                  that the                                                                             This tells us                                                                                  to be used                                                                                                             is going                                                                                     interface                                                                                   remote calls.        public interface MyRemote extends Remote {      to support


 2  Declare that all methods throw RemoteException
    The remote interface is the one the client uses as the type for the service. In
      other words, the client invokes methods on something that implements the
     remote interface. That something is the stub, of course, and since the stub is
      doing networking and I/O, all kinds of bad things can happen. The client has
      to acknowledge the risks by handling or declaring the remote exceptions. If
      the methods in an interface declare exceptions, any code calling methods on a
      reference of that type (the interface type) must handle or declare the exceptions.
                                  Remote interface is in java.rmi.    import java.rmi.*;
                                                                                  Every remote method
    public interface MyRemote extends Remote {                       call is considered                                                                                                          “risky.” Declaring        public String sayHello() throws RemoteException;                                                                                   RemoteException on
    }                                                                                  every method forces the
                                                                                                     client to pay attention
                                                                              and acknowledge that
 3  Be sure arguments and return values are primitives or Serializable        things might not work.
     Arguments and return values of a remote method must be either primitive
      or Serializable. Think about it. Any argument to a remote method has to
     be packaged up and shipped across the network, and that’s done through             Check out your
       Serialization. The same thing applies with return values. If you use primitives,          favorite Java
       Strings, and the majority of types in the API (including arrays and collections),         reference if you
       you’ll be fine. If you are passing around your own types, just be sure that you          need to refresh your
     make your classes implement Serializable.                                      memory on Serializable.
    public String sayHello() throws RemoteException;
                           This                                return                                            value                                                           is                                            gonna                                               be                                                          shipped                                                              over                                                            the                                                                        wire                                                                from                                                                        the                             server                                back                                   to                                      the                                                       client,                                                     so                                                             it                                                     must                                                        be Serializable.                                                                           That’s                       how                                args                                and                                        return                                                      values                                                get                                                      packaged                                                             up                                                            and                                                                                sent.

438      Chapter 11


---

## PDF page 477

the proxy pattern

Step two: make a Remote implementation
                                                                                           An RMI Detour
 1  Implement the Remote interface
     Your service has to implement the remote interface—the one with
      the methods your client is going to call.
    public class MyRemoteImpl extends UnicastRemoteObject implements MyRemote {
        public String sayHello() {
           return                  "Server                          says, 'Hey'";                                               The                                                                   compiler                                                                                            will                                                                 make                                                                                     sure                                                                            that you’ve                                                                                              implemented                                                                               all       }                                                        the                                                            methods                                                               from                                                                        the                                                                                       interface                                                                                         you                                                                                                    implement.                                                                 In                                                                   this                                                                          case,       // more               code                    in class                                                                             there’s                                                                                    only                                                                                          one.
    }
 2  Extend UnicastRemoteObject
     In order to work as a remote service object, your object needs some functionality
      related to “being remote.” The simplest way is to extend UnicastRemoteObject
      (from the java.rmi.server package) and let that class (your superclass) do the
     work for you.
    public class MyRemoteImpl extends UnicastRemoteObject implements MyRemote {
        private static final long serialVersionUID = 1L;     UnicastRemoteObject implements                                                                                                  Serializable, so we need the
 3  Write a no-arg constructor that declares RemoteException            serialVersionUID field.
     Your new superclass, UnicastRemoteObject, has one little problem—its
      constructor throws RemoteException. The only way to deal with this is to declare
     a constructor for your remote implementation, just so that you have a place to
      declare RemoteException. Remember, when a class is instantiated, its superclass
      constructor is always called. If your superclass constructor throws an exception,
     you have no choice but to declare that your constructor also throws an exception.                                                                                                                     in                                                                                                    anything                                                                                    put                                                                    You don’t have to                                                                                             need a                                                                                                        just                                                                                  You                                                                    the constructor.                                                                                                                    superclass    public MyRemoteImpl() throws RemoteException { }                                                                 way to declare that your                                                                                                          exception.                                                                                  throws an                                                                                constructor 4  Register the service with the RMI registry
    Now that you’ve got a remote service, you have to make it available to remote
       clients. You do this by instantiating it and putting it into the RMI registry (which
     must be running or this line of code fails). When you register the implementation
      object, the RMI system actually puts the stub in the registry, since that’s what the
       client             really                  needs.                         Register                              your                                        service                                            using                                                  the                                                                  static rebind() method                                                                                  of                                                                              the                                                                                                              use                                                                                               can                                                                                                                clients     java.rmi.Naming                            class.                                                                                       (that                                                               a name                                                                                        service                                                                                                                 it                                                                      your                                                                    Give                                                                                                             register                                                                                  and    try        {                                                                                                registry)                                                                         the                                                                      up in                                                                                it                                                                           look                                                                                            the                                                            to                                                                                                   bind                                                                                          you                                                                          When                                                                                              registry.         MyRemote                  service                         =                           new                                MyRemoteImpl();                                                        RMI                                                                 the                                                                                               the                                                                                               for                                                                 with                                                                                                             service                                                                                  the                                                                                      swaps                                                            RMI                                                                                  object,         Naming.rebind("RemoteHello",                                     service);                                                                              service                                                                                                               registry.                                                                                  the                                                                                                     in                                                                                      stub                                                                         the                                                                            puts                                                                and                                                                     stub    }      catch(Exception                      ex)                          {...}

                                                                       you are here 4      439


---

## PDF page 478

start the service

Step three: run rmiregistry
                                                                                             An RMI Detour
  1   Bring up a terminal and start the rmiregistry.
     Be sure you start it from a directory that has access to
      your classes. The simplest way is to start it from your              File Edit  Window Help Huh?
         classes directory.
                                                 %rmiregistry


Step four: start the service

 1   Bring up another terminal and start your service
     This might be from a main() method in your remote
      implementation class or from a separate launcher class.
      In this simple example, we put the starter code in the                File Edit  Window Help Huh?
      implementation class, in a main method that instantiates    %java MyRemoteImpl
      the object and registers it with RMI registry.


                Why are you showing stubs and skeletons in the diagrams for the RMI code? I thought we got      Q:
                    rid of those way back.

                       You’re right; for the skeleton, the RMI runtime can dispatch the client calls directly to the remote      A:                  service using reflection, and stubs are generated dynamically using Dynamic Proxy (which you’ll learn
               more about a bit later in the chapter). The remote object’s stub is a java.lang.reflect.Proxy instance (with an
                   invocation handler) that is automatically generated to handle all the details of getting the local method calls
                by the client to the remote object. But we like to show both the stub and skeleton, because conceptually
                                 it helps you to understand that there is something under the covers that’s making that communication
                between the client stub and the remote service happen.


 440      Chapter 11


---

## PDF page 479

the proxy pattern

Complete code for the server side
                                                                                           An RMI Detour
Let’s take a look at all the code for the server side:

The Remote interface:
                                      and the Remote                          RemoteException                             interface are in the java.rmi package.                                                                                            java.rmi.Remote. import java.rmi.*;                                                      Your interface MUST extend
  public interface MyRemote extends Remote {
                                                                                         All of your remote methods must     public String sayHello() throws RemoteException;                                                                               declare RemoteException. }

The Remote service (the implementation):
                                  UnicastRemoteObject is in
 import java.rmi.*;          the java.rmi.server package.                                                                       UnicastRemoteObject is the import java.rmi.server.*;                              Extending                                                                        easiest way to make a remote object.
  public class MyRemoteImpl extends UnicastRemoteObject implements MyRemote {
     private static final long serialVersionUID = 1L;
                                                                            You MUST                                             You                                                                                                 implement                                                     have to                                                            implement                                                                                                all the                                                                                   your remote     public String sayHello() {                                                                                                                interface!!                                                    interface                                                         methods,                                                         of course.                                                               But
         return "Server says, 'Hey'";  notice that you do NOT have to
     }                                           declare the RemoteException.

     public MyRemoteImpl() throws RemoteException { }  Your superclass constructor (for                                                                                                  declares an exception,                                                                   UnicastRemoteObject)                                                                        so YOU must write a constructor, because it
     public static void main (String[] args) {           means that your constructor is calling risky                                                                 code (its super constructor).         try {
             MyRemote service = new MyRemoteImpl();
             Naming.rebind("RemoteHello", service);
         } catch(Exception                           ex) {                                                    Make the remote                                                                                          object,                                                                                  then “bind” it to the                                                                       rmiregistry             ex.printStackTrace();                                                                                       using the                                                                                            static                                                                                                   Naming.rebind().                                                         name                                                                                    The                                                                   you                                                                                  register                                                                                        it         }                                                                                under                                                                                                                     is                                                                    use                                                                                  the name clients                                                            to                                                                                                                                         will                                                                            look                                                                                 it up in                                                                          the                                                                RMI     }                                                                                                         registry.
 }

                                                                       you are here 4      441


---

## PDF page 480

how to get the stub object


                                                                                            An RMI Detour

                        How does the client actually get
                                   the stub object?


                            And that’s where the RMI registry comes in.
                                     And, you’re right; the client has to get the stub object
                                             (our proxy), because that’s the thing the client will call
                                     methods on. To do that, the client does a “lookup,”
                                                     like going to the white pages of a phone book, and
                                                  essentially says, “Here’s a name, and I’d like the stub
                                              that goes with that name.”
                                                Let’s take a look at the code we need to look up and
                                                 retrieve a stub object.

                                                                             it works                                                               how                                                                               Here’s      page.                                                                       next                                                           on the
       Code Up Close

    The client always uses the remote
      interface as the type of the service.      In fact, the client never needs to     know the actual class name of your                                         This must                                                                           be the name                                                                       that the     remote service.                                                                                                    service was                                             lookup() is a static method                                                                                      registered under.                                    of the Naming class.
     MyRemote service =
         (MyRemote) Naming.lookup("rmi://127.0.0.1/RemoteHello");
              You have to cast it to the                 The host name or IP
                interface, since the lookup                      address where the
             method returns type Object.                      service is running.
                                                              (127.0.0.1 is localhost.)


442      Chapter 11


---

## PDF page 481

the proxy pattern


                                                                                        An RMI Detour


                                                        Server               Client

                  sayHello()
                 3
                                                bject                Stub      stub                     Skeleton Serviceo  Client object                                            returned
                                          2
                       1                     RMI registry (on server)
                                lookup()                                                            Remote Hello


                                                       Stub

How it works...

     1  Client does a lookup on the RMI registry
         Naming.lookup("rmi://127.0.0.1/RemoteHello");

     2  RMI registry returns the stub object
             (as the return value of the lookup method) and RMI
            deserializes the stub automatically.

     3  Client invokes a method on the stub, as if the
         stub IS the real service


                                                                    you are here 4      443


---

## PDF page 482

the remote client

Complete code for the client side
                                                                                            An RMI Detour
Let’s take a look at all the code for the client side:
                                 The Naming class (for doing the rmiregistry                                             lookup) is in the java.rmi package.   import java.rmi.*;

   public class MyRemoteClient {
      public static void main (String[] args) {
           new MyRemoteClient().go();
      }
                                                              as type                                                                     registry      public void go() {                                                        the cast.                                        It comes out of theforget                                              so don’t                                               Object,        try {
           MyRemote service = (MyRemote) Naming.lookup("rmi://127.0.0.1/RemoteHello");
                                                       You need the IP
           String s = service.sayHello();           address or                                                                                 hostname...       ...and the name used to                                                                                        the service.                                                                                           bind/rebind
           System.out.println(s);      It looks just like a regular old         } catch(Exception ex) {      method call! (Except it must            ex.printStackTrace();      acknowledge the                                                             RemoteException.)         }
      }
   }


        1.
              The things programmers do wrong
                 with RMI are:


        1. Forget to start rmiregistry before starting the remote
          service (when the service is registered using Naming.
           rebind(), the rmiregistry must be running!)
        2. Forget to make arguments and return types serializable
         (you won’t know until runtime; this is not something the
          compiler will detect).


444      Chapter 11


---

## PDF page 483

the proxy pattern

Back to our GumballMachine remote proxy

Okay, now that you have the RMI basics down, you’ve got the tools you need
to implement the gumball machine remote proxy. Let’s take a look at how the
GumballMachine fits into this framework:


                                                                          Remote                                                                                           GumballMachine CEO’s desktop                                                                      a JVM.                                  The stub is a proxy                      with
                                     to the remote
                                             GumballMachine.
                                                          Server heap                         Client heap


                                     ton                          e                                               kele                        mballS                         Gu            GumballStub    Gu      G                            mballMachin       umballMonitor
    This is our             code. It    Monitor                                                                       The                                              The skeleton accepts the     uses a proxy to                                                                                         GumballMachine is                                                     remote calls and makes           remote     talk to                                                                                       our remote service;             machines.                                       everything work on the      gumball                                                                                                                       it’s going to expose                                                                  service side.                                                                        a remote interface
                                                                                     for the client to
                                                                                                             use.


      Stop and think through how we’re going to adapt the gumball machine code to work with
      a remote proxy. Feel free to make some notes here about what needs to change and
       what’s going to be different than the previous version.


                                                                       you are here 4      445


---

## PDF page 484

remote interface for the gumball machine

Getting the GumballMachine ready to
be a remote service

The first step in converting our code to use the remote proxy is to enable the
GumballMachine to service remote requests from clients. In other words,
we’re going to make it into a service. To do that, we need to:
 1. Create a remote interface for the GumballMachine. This will provide a set
   of methods that can be called remotely.
 2. Make sure all the return types in the interface are serializable.
 3. Implement the interface in a concrete class.
We’ll start with the remote interface:

            Don’t forget to import java.rmi.*
                                                                This is the remote interface.
     import java.rmi.*;

     public interface GumballMachineRemote extends Remote {
         public int getCount() throws RemoteException;
         public String getLocation() throws RemoteException;
         public State getState() throws RemoteException;
    }

          All return types need                Here are the methods we’re going to support.
        to be primitive or                  Each one throws RemoteException.
           Serializable...


We have one return type that isn’t Serializable: the State class. Let’s fix it up...
                                                Serializable is in the java.io package.     import java.io.*;

     public interface State extends Serializable {                                                       Then we just extend the Serializable         public void insertQuarter();                                                                     interface (which has no methods in it).
         public void ejectQuarter();                 And now State in all the subclasses can
         public void turnCrank();                       be transferred over the network.
         public void dispense();
    }

446      Chapter 11


---

## PDF page 485

the proxy pattern


Actually, we’re not done with Serializable yet; we have one problem with State. As you may
remember, each State object maintains a reference to a gumball machine so that it can call the
gumball machine’s methods and change its state. We don’t want the entire gumball machine
serialized and transferred with the State object. There is an easy way to fix this:
                                                                                   In each implementation of State, we add
                                                                   the serialVersionUID and the transient   public class NoQuarterState implements State {                                                                    keyword to the GumballMachine instance
       private static final long serialVersionUID = 2L;      variable. The transient keyword tells the
       transient GumballMachine gumballMachine;         JVM not to serialize this field. Note
       // all other methods here                               that this can be slightly dangerous if you                                                                   try to access this field once the object’s   }                                                                        been serialized and transferred.
We’ve already implemented our GumballMachine, but we need to make sure it can act as a service and
handle requests coming from over the network. To do that, we have to make sure the GumballMachine is
doing everything it needs to implement the GumballMachineRemote interface.
As you’ve already seen in the RMI detour, this is quite simple; all we need to do is add a couple of things...
        First, we need to import the                                        GumballMachine is     RMI packages.                                             going to subclass the
                                         UnicastRemoteObject;
                                              this gives it the ability to             GumballMachine also needs to import java.rmi.*;
 import java.rmi.server.*;                                        act as a remote service.               implement the remote interface...
 public class GumballMachine
         extends UnicastRemoteObject implements GumballMachineRemote
 {
     private static final long serialVersionUID = 2L;
     // other instance variables here
     public GumballMachine(String location, int numberGumballs) throws RemoteException {
         // code here
     }
     public int getCount() {                                                           ...and the constructor needs         return count;                                                   to throw a remote exception,     }                                                                                     because the superclass does.
     public State getState() {                      That’s it! Nothing
         return state;                                 changes here at all!     }
     public String getLocation() {
         return location;
     }
     // other methods here
 }

                                                                       you are here 4      447


---

## PDF page 486

register the gumball service

Registering with the RMI registry...

That completes the gumball machine service. Now we just need to fire it up so
it can receive requests. First, we need to make sure we register it with the RMI
registry so that clients can locate it.
We’re going to add a little code to the test drive that will take care of this for us:

  public class GumballMachineTestDrive {
      public static void main(String[] args) {
          GumballMachineRemote gumballMachine = null;
         int count;
         if (args.length < 2) {
              System.out.println("GumballMachine <name> <inventory>");
              System.exit(1);
         }                                                          First we need to add a try/catch block
                                                                  around the gumball instantiation because our         try {                                                    constructor can now throw exceptions.             count = Integer.parseInt(args[1]);
              gumballMachine = new GumballMachine(args[0], count);
              Naming.rebind("//" + args[0] + "/gumballmachine", gumballMachine);
         } catch (Exception e) {
              e.printStackTrace();
         }                                        We also add the call to Naming.rebind,
     }                                                      which publishes the GumballMachine stub
 }                                                          under the name gumballmachine.

Let’s go ahead and get this running...                                                                                             Mighty                                                                                                               “official”                                        This gets the RMI                         We’re using the                                                                                            you should                                                                                 Gumball machines;          Run this first.                  registry service up                                                                                        your own machine name                                                                                        substitute                                     and running.                                                                                          here, or “localhost”.

   File Edit  Window Help Huh?
 % rmiregistry

              File Edit  Window Help Huh?
      % java GumballMachineTestDrive austin.mightygumball.com 100


                                                                  This gets the GumballMachine up and running
                            Run this second.                   and registers it with the RMI registry.

448      Chapter 11


---

## PDF page 487

the proxy pattern

Now for the GumballMonitor client...

Remember the GumballMonitor? We wanted to reuse it without
having to rewrite it to work over a network. Well, we’re pretty much
going to do that, but we do need to make a few changes.
                         We need to import the RMI package because we
 import java.rmi.*;       are using the RemoteException class below...
                                              Now we’re going to rely on the remote public class GumballMonitor {                                                               interface rather than the concrete     GumballMachineRemote machine;                                                         GumballMachine class.
     public GumballMonitor(GumballMachineRemote machine) {
         this.machine = machine;
     }

     public void report() {
         try {
             System.out.println("Gumball Machine: " + machine.getLocation());
             System.out.println("Current inventory: " + machine.getCount() + " gumballs");
             System.out.println("Current state: " + machine.getState());
         } catch (RemoteException e) {
             e.printStackTrace();             We also need to catch any remote exceptions         }                                         that might happen as we try to invoke methods     }                                                     that are ultimately happening over the network.
 }


                              Joe was right;
                                      this is working out
                                     quite nicely!


                                                                       you are here 4      449


---

## PDF page 488

test drive the monitor

Writing the Monitor test drive

Now we’ve got all the pieces we need. We just need to write some
code so the CEO can monitor a bunch of gumball machines:

                                  Here’s the monitor test drive. The
                      CEO is going to run this!
                                                                                       locations  import java.rmi.*;                                            Here’s all the                                                                                   monitor.                                                                   we’re going to                                                                   We create an array  public class GumballMonitorTestDrive {                                                                        of locations, one for
                                                                                   each machine.
      public static void main(String[] args) {
          String[] location = {"rmi://santafe.mightygumball.com/gumballmachine",
                               "rmi://boulder.mightygumball.com/gumballmachine",
                               "rmi://austin.mightygumball.com/gumballmachine"};

          GumballMonitor[] monitor = new GumballMonitor[location.length];
                                                                        We also create an
          for (int i=0; i < location.length; i++) {                            array of monitors.
              try {
                  GumballMachineRemote machine =
                          (GumballMachineRemote) Naming.lookup(location[i]);
                  monitor[i] = new GumballMonitor(machine);
                  System.out.println(monitor[i]);
             } catch (Exception e) {
                  e.printStackTrace();                 Now we need to get a proxy
                                                                    to each remote machine.             }
         }

          for (int i=0; i < monitor.length; i++) {
              monitor[i].report();
         }
      }                                      Then we iterate through each
 }                                          machine and print out its report.


450      Chapter 11


---

## PDF page 489

the proxy pattern

       Code Up Close
                         This returns a proxy to the remote                                                                    Remember, Naming.lookup() is a                         Gumball Machine (or throws an exception                                                                                 static method in the RMI package                            if one can’t be located).                                                                    that takes a location and service
                                                                  name and looks it up in the      try {                                                                               rmiregistry at that location.          GumballMachineRemote machine =
                    (GumballMachineRemote) Naming.lookup(location[i]);

          monitor[i] = new GumballMonitor(machine);
                                                                        remote                                                                  the                                                               to     }        catch              (Exception e) {                                                a proxy                                              we get                                                Once                                                                            GumballMonitor                                                              new                                                     a                                                                create                                                 we          e.printStackTrace();                                                         machine,                                                                                   monitor.                                                                 to                                                                   machine                                                                 it the                                              and pass     }


Another demo for the CEO of Mighty Gumball...

Okay, it’s time to put all this work together and give another demo. First let’s make
sure a few gumball machines are running the new code:
   On each machine, run rmiregistry in                           ...and then run the GumballMachine, giving it
   the background or from a separate                     a location and an initial gumball count.
    terminal window...


              File Edit  Window Help Huh?
     % rmiregistry &
     % java GumballMachineTestDrive santafe.mightygumball.com 100


   File Edit  Window Help Huh?
 % rmiregistry &
 % java GumballMachineTestDrive boulder.mightygumball.com 100


              File Edit  Window Help Huh?
     % rmiregistry &
     % java GumballMachineTestDrive austin.mightygumball.com 250
                                                                     Popular machine!

                                                                       you are here 4      451


---

## PDF page 490

demoing the monitor

And now let’s put the monitor in the hands of the CEO.
Hopefully, this time he’ll love it:


       File Edit  Window Help GumballsAndBeyond
  % java GumballMonitorTestDrive
  Gumball Machine: santafe.mightygumball.com
  Current inventory: 99 gumballs
  Current state: waiting for quarter                  The monitor iterates
                                                                              over each remote
                                                                           machine and calls
  Gumball Machine: boulder.mightygumball.com              its getLocation(),
  Current inventory: 44 gumballs                             getCount(), and                                                                          getState() methods.  Current state: waiting for turn of crank

  Gumball Machine: austin.mightygumball.com
  Current inventory: 187 gumballs
  Current state: waiting for quarter         This is amazing; it’s going to
                                                                revolutionize my business and  %
                                                        blow away the competition!


 By invoking methods on the proxy, we make
  a remote call across the wire, and get back
  a String, an integer, and a State object.
  Because we are using a proxy, the Gumball
  Monitor doesn’t know, or care, that calls
  are remote (other than having to worry
  about remote exceptions).


452      Chapter 11


---

## PDF page 491

the proxy pattern


              This worked great! But                                                Behind              I want to make sure I
           understand exactly what’s                                                       the Scenes                     going on...


1  The CEO runs the monitor, which first grabs the proxies to the remote
    gumball machines and then calls getState() on each one (along with
    getCount() and getLocation()).

 CEO’s desktop
                                                                         Remote GumballMachine                                                                                 with a JVM                          Type is                                    GumballMachineRemote


                    getState( )
                    3                        e                    ub
                                   eleton Gu       r     Proxy/St                                      proxy  Sk                          mballMachin    GumballMonito                                                returned                                             2
                       1
                                 lookup(                  RMI registry (on gumball machine)
                                                                                  austin                                           “austin”)


                                                          Proxy/Stub


                                                                      you are here 4      453


---

## PDF page 492

proxy behind the scenes


 2   getState() is called on the proxy, which forwards the call to the remote
      service. The skeleton receives the request and then forwards it to the
     GumballMachine.

                                                                             getState()
                       getState()

                         e                     ub
                       Skeleton Gu       r     Proxy/St                           mballMachin    GumballMonito


 3   GumballMachine returns the state to the skeleton, which serializes it and
      transfers it back over the wire to the proxy. The proxy deserializes it and
      returns it as an object to the monitor.
                                                                         State                                                       Serialized                                                                             object                                                  State
                           State
                             object


                         e                     ub
                       Skeleton Gu       r     Proxy/St                           mballMachin    GumballMonito

                                                                            Likewise, the GumballMachine  The monitor hasn’t changed at all,                                    implements another interface and  except it knows it may encounter                              may throw a remote exception in its  remote exceptions. It also uses the                                     constructor, but other than that, the  GumballMachineRemote interface rather                           code hasn’t changed.  than a concrete implementation.

                   We also have a small bit of code to register and locate stubs using the
                  RMI registry. But no matter what, if we were writing something to
                     work over the internet, we’d need some kind of locator service.


454      Chapter 11


---

## PDF page 493

the proxy pattern

The Proxy Pattern defined

We’ve already put a lot of pages behind us in this chapter; as you
can see, explaining the Remote Proxy is quite involved. Despite that,
you’ll see that the definition and class diagram for the Proxy Pattern
 is actually fairly straightforward. Note that the Remote Proxy is one
implementation of the general Proxy Pattern; there are actually
quite a few variations of the pattern, and we’ll talk about them later.
For now, let’s get the details of the general pattern down.
Here’s the Proxy Pattern definition:

    The Proxy Pattern provides a surrogate or           Use the Proxy
      placeholder for another object to control access to it.                                          Pattern to create a
                                              representative object
Well, we’ve seen how the Proxy Pattern provides a surrogate or                                             that controls accessplaceholder for another object. We’ve also described the proxy as
a “representative” for another object.                                                to another object,
But what about a proxy controlling access? That sounds a littlestrange. No worries. In the case of the gumball machine, just think      which may be remote,
of   the proxy             controlling                        access                                to                                the                                remote                                               object.                                      The                                                  proxy         expensive to create, orneeded        to control                  access                      because                             our                                           client,                                          the                                             monitor,                                                           didn’t
know how to talk to a remote object. So in some sense the remoteproxy controlled access so that it could handle the network details        in need of securing.
for us. As we just discussed, there are many variations of the Proxy
Pattern, and the variations typically revolve around the way the
proxy “controls access.” We’re going to talk more about this later,
but for now here are a few ways proxies control access:
    As we know, a remote proxy controls access to a remote
     object.
    A virtual proxy controls access to a resource that is expensive
     to create.
    A protection proxy controls access to a resource based on
     access rights.
Now that you’ve got the gist of the general pattern, check out the
class diagram...


                                                                       you are here 4      455


---

## PDF page 494

the proxy pattern defined

                                                        Both the Proxy and the                                                                                implement the                                                                      RealSubject                                                                                     interface. This                                                                                   <<interface>>             Subject
                                                                       Subject                                                                             allows any client to treat
                                                                                request()                                                             the proxy just like the
                                                                           RealSubject.


                                            RealSubject                   subject               Proxy
                                                 request()                                                   request()

                                                           The Proxy keeps a               The RealSubject is                                            to the                                                                                reference                       usually the object                                    The Proxy often instantiates          Subject, so it can                 that does most                                                                                           requests                                           or handles the creation of           forward               of the real work;                                         the RealSubject.                  to the Subject                the Proxy controls                                                                    when necessary.                    access to it.


                   Let’s step through the diagram...
                    First we have a Subject, which provides an interface for the RealSubject and the
                  Proxy. Because it implements the same interface as the RealSubject, the Proxy can
               be substituted for the RealSubject anywhere it occurs.
             The RealSubject is the object that does the real work. It’s the object that the Proxy
                  represents and controls access to.
             The Proxy holds a reference to the RealSubject. In some cases, the Proxy may be
                  responsible for creating and destroying the RealSubject. Clients interact with the
                RealSubject through the Proxy. Because the Proxy and RealSubject implement the
              same interface (Subject), the Proxy can be substituted anywhere the Subject can be
                  used. The Proxy also controls access to the RealSubject; this control may be needed
                            if the Subject is running on a remote machine, if the Subject is expensive to create
                   in some way, or if access to the subject needs to be protected in some way.
           Now that you understand the general pattern, let’s look at some other ways of using
                proxy beyond the Remote Proxy...


456      Chapter 11


---

## PDF page 495

the proxy pattern

Get ready for the Virtual Proxy

Okay, so far you’ve seen the definition of the Proxy Pattern and you’ve taken a look
 at one specific example: the Remote Proxy. Now we’re going to take a look at a different
 type of proxy, the Virtual Proxy. As you’ll discover, the Proxy Pattern can manifest
 itself in many forms, yet all the forms follow roughly the general proxy design. Why
 so many forms? Because the Proxy Pattern can be applied to a lot of different use
 cases. Let’s check out the Virtual Proxy and compare it to the Remote Proxy:


Remote Proxy                                                     request(request())
With the Remote Proxy, the proxy                                          )acts as a local representative                    request(
for an object that lives in a
different JVM. A method call on                   t
                                                              bjecthe proxy results in the call being                 Proxy        RealSu
transferred over the wire and       Client
invoked remotely, and the result
being returned back to the proxy
and then to the Client.                                                     We know this diagram
                                                                                     pretty well by now...


                                                                                to create” object.                                                                          Big “expensive

                                                          The proxy creates
Virtual Proxy                                                  the RealSubject
The Virtual Proxy acts as a                      )       when it’s needed.                                                 request(representative for an object that
may be expensive to create. The
Virtual Proxy often defers the
                             tcreation of the object until it                    Proxy         c                                                            bjeis needed; the Virtual Proxy        Client               RealSu
also acts as a surrogate for                   The proxy may handle the request, or if
the object before and while it is                 the RealSubject has been created, delegate
being created. After that, the proxy             the calls to the RealSubject.
delegates requests directly to the
RealSubject.


                                                                       you are here 4      457


---

## PDF page 496

image proxy controls access

Displaying Album covers

Let’s say you want to write an application that displays your favorite album covers.
You might create a menu of the album titles and then retrieve the images from an
online service like Amazon.com. If you’re using Swing, you might create an Icon
and ask it to load the image from the network. The only problem is, depending
on the network load and the bandwidth of your connection, retrieving an album
cover might take a little time, so your application should display something while
you’re waiting for the image to load. We also don’t want to hang up the entire
application while it’s waiting on the image. Once the image is loaded, the message
should go away and you should see the image.
An easy way to achieve this is through a virtual proxy. The virtual proxy can stand
in place of the icon, manage the background loading, and before the image is
fully retrieved from the network, display “Loading album cover, please wait...”.
Once the image is loaded, the proxy delegates the display to the Icon.
                          Choose the album cover of                          your liking here.


                                                                          While the album cover is loading,                                                                 the proxy displays a message.


                          cover is               the album          When                    the proxy                   loaded,               fully                 the image.                displays


458      Chapter 11


---

## PDF page 497

the proxy pattern

Designing the Album Cover Virtual Proxy

Before writing the code for the Album Cover Viewer, let’s look at the class diagram.
You’ll see this looks just like our Remote Proxy class diagram, but here the proxy is
used to hide an object that is expensive to create (because we need to retrieve the data
for the Icon over the network) as opposed to an object that actually lives somewhere
else on the network.

                   This is the Swing
                                                                                         <<interface>>                     Icon interface used                           Icon
                  to display images in a                getIconWidth()
                     user interface.                           getIconHeight()
                                                                                         paintIcon()


                                                                                      subject
                                               ImageIcon                                  ImageProxy
                                                     getIconWidth()                                            getIconWidth()
                                                      getIconHeight()                                            getIconHeight()
                                                          paintIcon()                                                   paintIcon()
   This is javax.swing.ImageIcon,
   a class that displays an Image.                                            This is our proxy, which first
                                                                                       displays a message and then, when
                                                                      the image is loaded, delegates to
                                                                              ImageIcon to display the image.
How ImageProxy is going to work:

      1  ImageProxy first creates an ImageIcon and starts
        loading it from a network URL.

      2  While the bytes of the image are being retrieved,
       ImageProxy displays “Loading album cover, please
          wait...”.

      3  When the image is fully loaded, ImageProxy delegates
          all method calls to the image icon, including
         paintIcon(), getIconWidth(), and getIconHeight().

      4    If the user requests a new image, we’ll create a new
        proxy and start the process over.


                                                                       you are here 4      459


---

## PDF page 498

the image proxy
                                       The ImageProxy
                                                                                                                                              <<interface>>Writing the Image Proxy          implements the Icon
                                                         interface.                              getIconWidth()Icon class ImageProxy implements Icon {
     volatile ImageIcon imageIcon;                                                               getIconHeight()
     final URL imageURL;                                                                                          paintIcon()
     Thread retrievalThread;
     boolean retrieving = false;                            The imageIcon is the REAL icon that we
                                                                                     eventually want to display when it’s loaded.     public ImageProxy(URL url) { imageURL = url; }
     public int getIconWidth() {                            We pass the URL of the image into         if (imageIcon != null) {                                                                      the constructor. This is the image we             return imageIcon.getIconWidth();                                                                        need to display once it’s loaded!         } else {
             return 800;
         }                                                         We return a default width and height     }                                                                                    until the imageIcon is loaded; then we     public int getIconHeight() {         if (imageIcon != null) {                            turn it over to the imageIcon.
             return imageIcon.getIconHeight();
         } else {
             return 600;
         }
     }                                                                          imageIcon is used by two different
                                                                                  threads, so along with making the variable
     synchronized void setImageIcon(ImageIcon imageIcon) {       volatile (to protect reads), we use a         this.imageIcon = imageIcon;                                                                                     synchronized setter (to protect writes).     }
     public void paintIcon(final Component c, Graphics  g, int x,  int y) {
         if (imageIcon != null) {
             imageIcon.paintIcon(c, g, x, y);
         } else {
             g.drawString("Loading album cover, please wait...", x+300, y+190);
             if (!retrieving) {
                 retrieving = true;
                 retrievalThread = new Thread(new Runnable() {
                     public void run() {
                         try {
                             setImageIcon(new ImageIcon(imageURL, "Album Cover"));
                             c.repaint();
                         } catch (Exception e) {                   Here’s where things get interesting.
                             e.printStackTrace();               This code paints the icon on the
                         }                                               screen (by delegating to imageIcon).
                     }                                                  However, if we don’t have a fully                 });                                                                            created imageIcon, then we create                 retrievalThread.start();                                                                                        one. Let’s look at this up close on the             }                                                                         next page...         }
     }
 }

460      Chapter 11


---

## PDF page 499

the proxy pattern

.       Code Up Close

                        This method is called when it’s time to paint the icon on the screen.

    public void paintIcon(final Component c, Graphics  g, int x,  int y) {
         if (imageIcon != null) {
                                                                            If we’ve got an icon already, we go
                                                                   ahead and tell it to paint itself.             imageIcon.paintIcon(c, g, x, y);

         } else {

             g.drawString("Loading album cover, please wait...", x+300, y+190);
             if (!retrieving) {                                                    Otherwise we
                                                                                                        display the
                                                                                                     “loading” message.                 retrieving = true;
                 retrievalThread = new Thread(new Runnable() {
                     public void run() {
                         try {
                             setImageIcon(new ImageIcon(imageURL, "Album Cover"));
                             c.repaint();
                         } catch (Exception e) {
                             e.printStackTrace();
                         }                                                          that                                                                            Note                                                                                            image.                                                                                     icon                     }                                                                                  the                                                    REAL                                                              the                                                 we load                                                                                               is synchronous:                                                      where                 });                                                                             IconImage                                                         Here’s                                                                               the image                                                                 with                                                                                                   until                                                                    loading                                                                               return                                                                             do                                                                                to                                                        image                                                                             doesn’t                                              the                                                            a chance                                                                  of                                                                  constructor                                                                      much                                                                          us                                                                                                     we’re                                                                                       so                                                                                  give                                                        ImageIcon                                                                       doesn’t                 retrievalThread.start();                                                                                                    displayed,                                                   That                                                                                message                                                               is loaded.                                                                     have our                                                                                “Code Way Up                                                         and                                                                        See the             }                                                            updates                                                         screen                                                                               asynchronously.                                                                     this                                                do                                                                                              more...         }                                                          going to                                                                    page for                                                             next                                                       the                                                   on     }                                                  Close”


                                                                       you are here 4      461


---

## PDF page 500

image proxy up close

        Code Way Up Close

              If we aren’t already trying to retrieve the image...
                                                        ...then it’s time to start retrieving it (in case you                                           were wondering, only one thread calls paint, so we                                                  should be okay here in terms of thread safety).
       if (!retrieving) {                                                          We don’t want to hang up the           retrieving = true;                                                                               entire user interface, so we’re
                                                                                going to use another thread to
           retrievalThread = new Thread(new Runnable() {      retrieve the image.
               public void run() {
                   try {
                       setImageIcon(new ImageIcon(imageURL, "Album Cover"));
                       c.repaint();                                               In our thread we
                  } catch (Exception e) {                                       instantiate the
                                                                                           Icon object. Its                       e.printStackTrace();
                                              When we have the image,          constructor will not                  }                                               we tell Swing that we            return until the
              }                                  need to be repainted.            image is loaded.
           });
           retrievalThread.start();
       }

              So, the next time the display is painted after the ImageIcon is instantiated,
            the paintIcon() method will paint the image, not the loading message.


462      Chapter 11


---

## PDF page 501

the proxy pattern
     Design Puzzle

                               The ImageProxy class appears to have two states that are controlled
                                  by conditional statements. Can you think of another pattern that might
                                     clean up this code? How would you redesign ImageProxy?

class ImageProxy implements Icon {
    // instance variables & constructor here

    public int getIconWidth() {
        if (imageIcon != null) {
                                                    Two states            return imageIcon.getIconWidth();
        } else {
            return 800;
        }
    }

    public int getIconHeight() {
        if (imageIcon != null) {
            return imageIcon.getIconHeight();     Two states
        } else {
            return 600;
        }
    }

    public void paintIcon(final Component c, Graphics  g, int x,  int y) {
        if (imageIcon != null) {
            imageIcon.paintIcon(c, g, x, y);                                                                              Two states
        } else {
            g.drawString("Loading album cover, please wait...", x+300, y+190);
            // more code here
        }
    }
}


                                                                   you are here 4      463


---

## PDF page 502

test drive the image proxy

Testing the Album Cover Viewer

                                    Okay, it’s time to test out this fancy new virtual proxy. Behind the scenes
          Ready Bake     we’vecreatesbeena frame,bakinginstallsup a thenewmenus,ImageProxyTestDriveand creates our proxy.that setsWeupdon’tthe window,go
          Code              throughsource codeall thatandcodehave ina look,gory detailor checkhere,it outbut atyouthecanendalwaysof thegrabchapterthe
                                  where we list all the source code for the Virtual Proxy.
                                       Here’s a partial view of the test drive code:
  public class ImageProxyTestDrive {
     ImageComponent imageComponent;
     public static void main (String[] args) throws Exception {
         ImageProxyTestDrive testDrive = new ImageProxyTestDrive();
     }
                                                                      Here we create an image proxy and     public ImageProxyTestDrive() throws Exception {                                                                          set it to an initial URL. Whenever
                                                                        you choose a selection from the Album         // set up frame and menus                                                                           menu, you’ll get a new image proxy.
         Icon icon = new ImageProxy(initialURL);
         imageComponent = new ImageComponent(icon);           Next we wrap our proxy in a
         frame.getContentPane().add(imageComponent);           component so it can be added to
     }                                                                  the frame. The component will
 }                                                                        take care of the proxy's width,                                               Finally we add the proxy to the                                                                                        height, and similar details.                                    frame so it can be displayed.
Now let’s run the test drive:


        File Edit  Window Help JustSomeOfTheAlbumsThatGotUsThroughThisBook
   % java ImageProxyTestDrive

                                    Running ImageProxyTestDrive
                                       should give you a window like this.
                                                                                                                                     aphex twin
Things to try...

      1  Use the menu to load different album covers; watch the
         proxy display “loading” until the image has arrived.
      2   Resize the window as the “loading” message is displayed.
          Notice that the proxy is handling the loading without
         hanging up the Swing window.
      3  Add your own favorite albums to ImageProxyTestDrive.

464      Chapter 11


---

## PDF page 503

the proxy pattern

What did we do?
                                                 Behind
        created                an ImageProxy                                  class                                   for the display.                                          The 1 We
     paintIcon()              method                              is called                             and ImageProxy                                                   fires                                                   off a               the Scenes
     thread to retrieve the image and create the ImageIcon.
                                                                     creates a                                                       ImageProxy         the                                                      to instantiate                                                     thread                                                                 which starts                   SomeSome imageimage                                             paintIcon()paintIcon()           ImageIcon,                                                          the image.                          serverserver onon                                                                 retrieving                                                                                                        thethe internetinternet                                                                                         getget imageimage


                 y
                   ox                            n                              Pr   ImageIco                            Image
                                             displaysdisplays loadingloading
                                     messagemessage


                                                                                       imageimage retrievedretrieved

 2  At some point the image is returned and
     the ImageIcon fully instantiated.
                         ImageIcon

 3  After the ImageIcon is created, the next time paintIcon()
      is called, the proxy delegates to the ImageIcon.


                                              paintIcon()paintIcon()
                                                                      paintIcon()paintIcon()


                 y
                   ox                               Pr   I                            Image                        mageIcon


                                                       displaysdisplays thethe realreal imageimage


                                                                       you are here 4      465


---

## PDF page 504

q&a about the image proxy


                                                  the client would have to wait until each          The Remote Proxy and Virtual                                                                                             I see how Decorator and Proxy  Q:                                image is retrieved before it could paint  Q:      Proxy seem so different to me; are                                                      relate, but what about Adapter? An                                                                    its entire interface. The proxy controls      they really ONE pattern?                                                      adapter seems very similar as well.                                            access to the ImageIcon so that before
                                                                                           it is fully created, the proxy provides
                                                                                        Both Proxy and Adapter sit in front  A:               You’ll find a lot of variants of the      another onscreen representation. Once  A:
      Proxy Pattern in the real world; what        the ImageIcon is created, the proxy         of other objects and forward requests to
       they all have in common is that they        allows access.                          them. Remember that Adapter changes
        intercept a method invocation that the                                                 the interface of the objects it adapts,
        client is making on the subject. This                                                    while Proxy implements the same                                     How do I make clients use the        level of indirection allows us to do    Q:                                         interface.                                         Proxy rather than the Real Subject?     many things, including dispatching
       requests to a remote subject, providing                                          There is one additional similarity that
      a representative for an expensive            Good question. One common         relates to the Protection Proxy. A                  A:
       object as it is created, or, as you’ll see,     technique is to provide a factory that        Protection Proxy may allow or disallow
       providing some level of protection that      instantiates and returns the subject.       a client access to particular methods
      can determine which clients should be     Because this happens in a factory            in an object based on the role of the
        calling which methods. That’s just the      method, we can then wrap the subject       client. In this way a Protection Proxy
       beginning; the general Proxy Pattern        with a proxy before returning it. The      may only provide a partial interface to
      can be applied in many different ways,       client never knows or cares that it’s       a client, which is quite similar to some
      and we’ll cover some of the other ways     using a proxy instead of the real thing.     Adapters. We are going to take a look at
        at the end of the chapter.                                                              Protection Proxy in a few pages.
                                                                                               I noticed in the ImageProxy                  Q:
           ImageProxy seems just like       example, you always create a new  Q:
      a Decorator to me. I mean, we are       ImageIcon to get the image, even if
       basically wrapping one object with      the image has already been retrieved.
      another and then delegating the calls   Could you implement something
       to the ImageIcon. What am I missing?    similar to the ImageProxy that
                                         caches past retrievals?
          Sometimes Proxy and Decorator  A:       look very similar, but their purposes are        You are talking about a                  A:
        different: a decorator adds behavior to      specialized form of a Virtual Proxy
      a class, while a proxy controls access       called a Caching Proxy. A caching proxy
        to it. You might ask, “Isn’t the loading       maintains a cache of previously created
      message adding behavior?” In some        objects and when a request is made it
      ways it is; however, more importantly,       returns a cached object, if possible.
       the ImageProxy is controlling access
        to an ImageIcon. How does it control      We’re going to look at this and at
      access? Well, think about it this way:       several other variants of the Proxy
       the proxy is decoupling the client from      Pattern at the end of the chapter.
       the ImageIcon. If they were coupled


466      Chapter 11


---

## PDF page 505

the proxy pattern


                                          Tonight’s talk: Proxy and Decorator get intentional.


Proxy:                                                Decorator:
Hello, Decorator. I presume you’re here because
people sometimes get us confused?
                                                                  Well, I think the reason people get us confused is
                                                                     that you go around pretending to be an entirely
                                                                        different pattern, when in fact, you’re just Decorator
                                                                     in disguise. I really don’t think you should be
                                                             copying all my ideas.
Me copying your ideas? Please. I control access to
objects. You just decorate them. My job is so much
more important than yours it’s just not even funny.

                                                                    “Just” decorate? You think decorating is some
                                                                          frivolous, unimportant pattern? Let me tell you
                                                              buddy, I add behavior. That’s the most important
                                                                 thing about objects—what they do!
Fine, so maybe you’re not entirely frivolous...but I
still don’t get why you think I’m copying all your
ideas. I’m all about representing my subjects, not
decorating them.
                                                   You can call it “representation” but if it looks like
                                                          a duck and walks like a duck... I mean, just look at
                                                            your Virtual Proxy; it’s just another way of adding
                                                              behavior to do something while some big expensive
                                                                   object is loading, and your Remote Proxy is a way
                                                                      of talking to remote objects so your clients don’t
                                                           have to bother with that themselves. It’s all about
I don’t think you get it, Decorator. I stand in for                    behavior, just like I said.
my Subjects; I don’t just add behavior. Clients use
me as a surrogate of a Real Subject, because I can
protect them from unwanted access, or keep their
GUIs from hanging up while they’re waiting for big
objects to load, or hide the fact that their Subjects
are running on remote machines. I’d say that’s a
very different intent from yours!
                                                                 Call it what you want. I implement the same
                                                                      interface as the objects I wrap; so do you.


                                                                       you are here 4      467


---

## PDF page 506

fireside chats: proxy and decorator


Proxy:                                                Decorator:
Okay, let’s review that statement. You wrap an
object. While sometimes we informally say a proxy
wraps its Subject, that’s not really an accurate term.

                                        Oh yeah? Why not?
Think about a remote proxy...what object am
I wrapping? The object I’m representing and
controlling access to lives on another machine!
Let’s see you do that.
                                                          Okay, but we all know remote proxies are kinda
                                                                  weird. Got a second example? I doubt it.
Sure, okay, take a virtual proxy...think about the
album viewer example. When the client first uses
me as a proxy the subject doesn’t even exist! So
what am I wrapping there?
                                          Uh huh, and the next thing you’ll be saying is that
                                                        you actually get to create objects.

I never knew decorators were so dumb! Of course
I sometimes create objects. How do you think a
virtual proxy gets its subject?! Okay, you just pointed
out a big difference between us: we both know
decorators only add window dressing; they never get
to instantiate anything.
                                        Oh yeah? Instantiate this!

Hey, after this conversation I’m convinced you’re
just a dumb proxy!                                          Dumb proxy? I’d like to see you recursively wrap
                                                      an object with 10 decorators and keep your head
                                                                        straight at the same time.
Very seldom will you ever see a proxy get into
wrapping a subject multiple times; in fact, if you’re
wrapping something 10 times, you better go back
reexamine your design.
                                                                           Just like a proxy, acting all real when in fact you just
                                                               stand in for the objects doing the real work. You
                                                           know, I actually feel sorry for you.


468      Chapter 11


---

## PDF page 507

the proxy pattern

Using the Java API’s Proxy to create a
protection proxy

Java’s got its own proxy support right in the java.lang.reflect package. With this package,
Java lets you create a proxy class on the fly that implements one or more interfaces and
forwards method invocations to a class that you specify. Because the actual proxy class is
created at runtime, we refer to this Java technology as a dynamic proxy.
We’re going to use Java’s dynamic proxy to create our next proxy implementation (a
 protection proxy), but before we do that, let’s quickly look at a class diagram that shows
how dynamic proxies are put together. Like most things in the real world, it differs
 slightly from the classic definition of the pattern:


                                           <<interface>>                                                <<interface>>
                                          Subject                                             InvocationHandler
                                       request()                                                                                                          invoke()

                                                                                                               consists                                                                The Proxy now                                                                                                                classes.                                                                  of two

              RealSubject                                    Proxy                        InvocationHandler
          request()                                              request()                                invoke()


                        The Proxy is generated
                           by Java and implements                                     which gets passed                                                                              InvocationHandler,                                                                     supply the                            the                                    entire Subject          You                                                                                                 Proxy.                                                                                  on the                                                                                      invoked                                                                   that are                                                                                       calls                                                                               all method                                 interface.                                                                                        the                                                                                     to                                                                                              access                                                                                    controls                                              The InvocationHandler
                                                      methods of the RealSubject.


Because Java creates the Proxy class for you, you need a way to tell the Proxy class what
to do. You can’t put that code into the Proxy class like we did before, because you’re not
implementing one directly. So, if you can’t put this code in the Proxy class, where do
you put it? In an InvocationHandler. The job of the InvocationHandler is to respond to
any method calls on the proxy. Think of the InvocationHandler as the object the Proxy
asks to do all the real work after it has received the method calls.
Okay, let’s step through how to use the dynamic proxy...

                                                                       you are here 4      469


---

## PDF page 508

protection proxy

Geeky Matchmaking in Objectville

Every town needs a matchmaking service, right? You’ve risen to the task and
implemented a dating service for Objectville. You’ve also tried to be innovative
by including a “Geek rating” feature where participants can rate each other’s
geekiness (a good thing)—you figure this keeps your customers engaged and
looking through possible matches; it also makes things a lot more fun.
Your service revolves around a Person interface that allows you to set and get
information about a person:
                         interface; we’ll                   is the            This                         implementation            get to the                             sec...              in just a                                                            Here we can get                                                            about the      information                                                                                      person’s                                                                   gender,          name,                                                                                    interests, and Geek                                                                   rating                                                                         (1-10).              public interface Person {

                  String getName();
                  String getGender();
                  String getInterests();
                  int getGeekRating();

                  void setName(String name);
                  void setGender(String gender);
                  void setInterests(String interests);
                  void setGeekRating(int rating);
                                                                               integer              }                                                takes an                                                       setGeekRating()                                                                           running                                                          the                                                              it to                                             and adds                   We can also set the same                                                                             person.                                                                    this                                                       for                         information through the         average
                           respective method calls.


Now let’s check out the implementation...


470      Chapter 11


---

## PDF page 509

the proxy pattern

The Person implementation
                                                  The PersonImpl implements the Person interface.
 public class PersonImpl implements Person {
     String name;
     String gender;
     String interests;             The instance variables.
     int rating;
     int ratingCount = 0;
     public String getName() {
         return name;
     }
                                                                           All the getter methods; they each return
     public String getGender() {                      the appropriate instance variable...
         return gender;
     }
     public String getInterests() {
         return interests;
     }                                                                ...except for getGeekRating(),
                                                              which computes the average
     public int getGeekRating() {                  of the ratings by dividing the
         if (ratingCount == 0) return 0;              ratings by the ratingCount.
         return (rating/ratingCount);
     }

     public void setName(String name) {
         this.name = name;                                   And here’s all the setter
     }                                                                   methods, which set the
                                                                                corresponding instance variable.
     public void setGender(String gender) {
         this.gender = gender;
     }
     public void setInterests(String interests) {
         this.interests = interests;
     }
                                                                                         Finally, the     public            void setGeekRating(int                                   rating) {                                                                                      setGeekRating()                                                                                     method                                                                           increments the         this.rating                     += rating;                                                                                         total                                                                                           ratingCount                                                                                         and         ratingCount++;                                                                 adds the rating to the                                                                                                    running total.     }
 }


                                                                      you are here 4      471


---

## PDF page 510

person needs protecting


                                          I wasn’t very successful finding dates.
                                        Then I noticed someone had changed my
                                                    interests. I also noticed that a lot of
                                                people are bumping up their Geek scores
                                          by giving themselves high ratings. You
                                                   shouldn’t be able to change someone else’s
                                                  interests or give yourself a rating!


               While we suspect other factors may be keeping Elroy from getting
                   dates, he’s right: you shouldn’t be able to vote for yourself or to
               change another customer’s data. The way Person is defined, any client
               can call any of the methods.
                This is a perfect example of where we might be able to use a
                 Protection Proxy. What’s a Protection Proxy? It’s a proxy that controls
                  access to an object based on access rights. For instance, if we had an
               employee object, a Protection Proxy might allow the employee to call
                  certain methods on the object, a manager to call additional methods                    Elroy
                      (like setSalary()), and a human resources employee to call any method
              on the object.
                In our dating service we want to make sure that a customer can set
                   his own information while preventing others from altering it. We also
              want to allow just the opposite with the Geek ratings: we want the
                 other customers to be able to set the rating, but not that particular
                 customer. We also have a number of getter methods in Person, and
                because none of these return private information, any customer
                should be able to call them.


472      Chapter 11


---

## PDF page 511

the proxy pattern

      Five-minute drama: protecting subjects
        The internet bubble seems a distant memory; those were the days
         when all you needed to do to find a better, higher-paying job was
          to walk across the street. Even agents for software developers
         were in vogue...
                                                                       Subject
                    I’d like to make an
                  offer, can we get her on
                the phone?


                                                               She’s tied up...uh...
                                                                            in a meeting right now,
                                                       what did you have in
                                                          mind?
                                                       a protection                                                                         Like                                                                          the agent                                                                                   proxy,       to his                                                                                              access                                                                                 protects       only                                                                                                letting                           Agent                                                  subject,                                                                                                           calls through...                                                                                     certain
Jane DotCom

                                                  Come on.
          We think we can                                You’re wasting our time
             meet her current                               here! Not a chance! Come
                 salary plus 15%.                             back later with a better
                                                                  offer.


                                                                   you are here 4      473


---

## PDF page 512

big picture of proxy

Big Picture: creating a Dynamic Proxy
for the Person
We have a couple of problems to fix: customers shouldn’t be changing their
own Geek rating and customers shouldn’t be able to change other customers’
personal information. To fix these problems we’re going to create two proxies:
one for accessing your own Person object and one for accessing another
customer’s          Person                    object. That way, the proxies can control what requests can                                                                           Remember this diagrambe made in          each circumstance.                                                                          from a few pages back...To create these proxies we’re going to use the Java
API’s dynamic proxy that you saw a few pages                                                      <<interface>>                                           <<interface>>
back. Java will create two proxies for us; all we                                                   request()Subject                                             invoke()InvocationHandler
need to do is supply the handlers that know what
to do when a method is invoked on the proxy.

Step one:                                                                              RealSubject                                 Proxy                     InvocationHandler
     Create two InvocationHandlers.                               request()                                         request()                             invoke()
      InvocationHandlers implement the behavior
       of the proxy. As you’ll see, Java will take care
       of creating the actual proxy class and object;
     we just need to supply a handler that knows                                        We need two
     what to do when a method is called on it.                                             of these.
Step two:                                                  We create the
    Write the code that creates the                                    proxy itself at
     dynamic proxies.                                                          runtime.
    We need to write a little bit of code to
      generate the proxy class and instantiate it.
      We’ll step through this code in just a bit.
                                                                                          Proxy                       OwnerInvocationHandler
Step three:                                                                                  request()                                    invoke()
    Wrap any Person object with the
     appropriate proxy.
    When we need to use a Person object, either it’s          When a customer is viewing his own bean
      the object of the customer himself (in that case,
       we’ll call him the “owner”), or it’s another user           When a customer is viewing someone else’s bean
       of the service that the customer is checking out
        (in that case we’ll call him “non-owner”).
                                                                                           Proxy                      NonOwnerInvocationHandler
      In either case, we create the appropriate proxy                        request()                                    invoke()
       for the Person.


474      Chapter 11


---

## PDF page 513

the proxy pattern

Step one: creating Invocation Handlers

We know we need to write two invocation handlers, one for the owner and one for
the non-owner. But what are invocation handlers? Here’s the way to think about
them: when a method call is made on the proxy, the proxy forwards that call to
your invocation handler, but not by calling the invocation handler’s corresponding
method. So, what does it call? Have a look at the InvocationHandler interface:

                                            <<interface>>
                                         InvocationHandler
                                  invoke()


There’s only one method, invoke(), and no matter what methods get called
on the proxy, the invoke() method is what gets called on the handler. Let’s see
how this works:

 1  Let’s say the setGeekRating()
    method is called on the proxy.

                                                          2 The proxy then
              proxy.setGeekRating(9);                           turns around and
                                                                                        calls invoke() on the
                                                                         InvocationHandler.
          invoke(Object proxy, Method method, Object[] args)
                                                                The Method class, part of the
                                                           Here’s how                   reflection API, tells us what
  3 The handler decides                     we invoke the             method was called on the proxy
     what it should do                         method on the                via its getName() method.
      with the request                               RealSubject.
     and possibly
     forwards it on to
     the RealSubject.            return method.invoke(person, args);
    How does the
      handler decide?
                                                                                                            ...with the original      We’ll find out next.             Here we invoke the                                                                   Only now we                                                                                         arguments.                                                  original method that was                                                                          invoke it on the                                               called on the proxy. This                                                                              RealSubject...                                          object was passed to us in
                                      the invoke call.

                                                                       you are here 4      475


---

## PDF page 514

creating an invocation handler

Creating Invocation Handlers, continued...

When invoke() is called by the proxy, how do you know what to do with the call?
Typically, you’ll examine the method that was called on the proxy and make
decisions based on the method’s name and possibly its arguments. Let’s implement
OwnerInvocationHandler to see how this works:

                       is part of the java.lang.reflectInvocationHandler                                                                      All invocation                                                                              handlers package, so we need to import it.                              implement                                                                the
                                                                 InvocationHandler interface.
 import java.lang.reflect.*;
                                                                                       We're passed the
 public class OwnerInvocationHandler implements InvocationHandler {   RealSubject in the
     Person person;                                                                constructor and we
                                                                                  keep a reference to it.
     public OwnerInvocationHandler(Person person) {
         this.person = person;                                                           Here’s the invoke()
                                                                                method that gets     }
                                                                                                        called every time a
                                                                                method is invoked     public Object invoke(Object proxy, Method method, Object[] args)                                                                                          on the proxy.             throws IllegalAccessException {
                                                                                                 If the method is a getter,
         try {                                                               we go ahead and invoke it
             if (method.getName().startsWith("get")) {                     on the real subject.
                 return method.invoke(person, args);
             } else if (method.getName().equals("setGeekRating")) {
                 throw new IllegalAccessException();                                                                                             Otherwise, if it is             } else if (method.getName().startsWith("set")) {                                                                                     the setGeekRating()                 return method.invoke(person, args);                                                                               method we disallow
             }                                                                                          it by throwing
         } catch (InvocationTargetException e) {                                 IllegalAccessException.
             e.printStackTrace();
         }                                                           Because we are the
                                             This will happen if        owner, any other set         return null;                                         the real subject         method is fine and we     }                                           throws an                                                            exception.      go ahead and invoke it }                                                                      on the real subject.            If any other method is called,
            we’re just going to return null
           rather than take a chance.


476      Chapter 11


---

## PDF page 515

the proxy pattern


The NonOwnerInvocationHandler works just like the OwnerInvocationHandler except
that it allows calls to setGeekRating() and it disallows calls to any other set method.
Go ahead and write this handler yourself:


                                                 you are here 4      477


---

## PDF page 516

create the proxy

Step two: creating the Proxy class and
instantiating the Proxy object
Now, all we have left is to dynamically create the Proxy class and instantiate the proxy
object. Let’s start by writing a method that takes a Person object and knows how to create
an owner proxy for it. That is, we’re going to create the kind of proxy that forwards its
method calls to OwnerInvocationHandler. Here’s the code:
                                                         real                                             (the                                        object                                 Person                          a                         takes               method            This                                                                              the                                                                                creates                                                                    code                                                                   This                                                  the                                              Because                                                           it.                                      for                            a proxy                          returns                   and              subject)                                                                                some                                                                                                                      is                                                                                        this                                                         Now                                                                       proxy.                                              we                                                     subject,                                          as the                                 interface                         same                     the                   has            proxy                                                                                                             let’s                                                                                         so                                                                                   code,                                                                                     ugly                                                                  mighty             return a Person.                                                                      step through it carefully.
                                                                          To create a proxy we use the
   Person getOwnerProxy(Person person) {                                   static newProxyInstance()
                                                                        method on the Proxy class.
       return (Person) Proxy.newProxyInstance(                                                        We pass it the class loader for our subject...               person.getClass().getClassLoader(),
               person.getClass().getInterfaces(),
                                                                                             ...and the set of interfaces the               new OwnerInvocationHandler(person));                                                                        proxy needs to implement...   }
        We pass the real subject into the constructor of
         the invocation handler. If you look back two pages,     ...and an invocation handler, in this
            you’ll see this is how the handler gets access to        case our OwnerInvocationHandler.
         the real subject.


                                                 While it is a little complicated, there isn’t much to creating
                                                  a dynamic proxy. Why don’t you write getNonOwnerProxy(),
                                              which returns a proxy for NonOwnerInvocationHandler:


 Take it further: can you write a method called getProxy() that takes
 a handler and a person and returns a proxy that uses that handler?


478      Chapter 11


---

## PDF page 517

the proxy pattern

Testing the matchmaking service

Let’s give the matchmaking service a test run and see how it controls access to
the setter methods based on the proxy that is used.
                                                         The main() method just creates
 public class MatchMakingTestDrive {                        the test drive and calls its drive()
     // instance variables here                             method to get things going.
     public static void main(String[] args) {
         MatchMakingTestDrive test = new MatchMakingTestDrive();
         test.drive();
     }                                               The constructor initializes our database
                                                         of people in the matchmaking service.
     public MatchMakingTestDrive() {
         initializeDatabase();
     }                                                                        Let’s retrieve a person
                                                                      from the database...
     public void drive() {
         Person joe = getPersonFromDatabase("Joe Javabean");                                                                                                          ...and create an owner proxy.         Person ownerProxy = getOwnerProxy(joe);
         System.out.println("Name is " + ownerProxy.getName());          Call a getter...         ownerProxy.setInterests("bowling, Go");
         System.out.println("Interests set from owner proxy");              ...and then a setter.
         try {
             ownerProxy.setGeekRating(10);                               And then try to
         } catch (Exception e) {                                                  change the rating.
             System.out.println("Can't set rating from owner proxy");
         }                                                                                 This shouldn’t work!         System.out.println("Rating is " + ownerProxy.getGeekRating());
                                                                    Now create a non-
         Person nonOwnerProxy = getNonOwnerProxy(joe);                    owner proxy...
         System.out.println("Name is " + nonOwnerProxy.getName());                                                                                                               ...and call a getter...         try {
             nonOwnerProxy.setInterests("bowling, Go");                                ...followed by a
         } catch (Exception e) {                                                            setter.
             System.out.println("Can't set interests from non owner proxy");
         }                                                                                 This shouldn’t work!
         nonOwnerProxy.setGeekRating(3);
         System.out.println("Rating set from non owner proxy");
         System.out.println("Rating is " + nonOwnerProxy.getGeekRating());    Then try to set
     }                                                                                   the rating.
     // other methods like getOwnerProxy and getNonOwnerProxy here                                                                                            This should work! }


                                                                       you are here 4      479


---

## PDF page 518

test drive the protection proxy

Running the code...


                  File Edit  Window Help Born2BDynamic
      % java MatchMakingTestDrive
       Name is Joe Javabean                                                               Our Owner proxy allows       Interests set from owner proxy                                                                          getting and setting,
       Can't set rating from owner proxy                except for the Geek
                                                                                   rating.       Rating is 7

       Name is Joe Javabean                                Our NonOwner proxy allows
       Can't set interests from non owner proxy       getting only, but also                                                                                     allows calls to set the Geek
       Rating set from non owner proxy                       rating.
       Rating is 5
      %
                               The new rating is the average of the previous rating, 7,
                                   and the value set by the NonOwner proxy, 3.


     So what exactly is the “dynamic”             That’s because the InvocationHandler         Are there any restrictions onQ:               A:                  Q:aspect of dynamic proxies? Is it that I’m        isn’t a proxy—it’s a class that the proxy         the types of interfaces I can pass into
 instantiating the proxy and setting it to a     dispatches to for handling method calls. The    newProxyInstance()?
handler at runtime?                         proxy itself is created dynamically at runtime
                                          by the static Proxy.newProxyInstance()               Yes, there are a few. First, it                                   A:     No, the proxy is dynamic because        method.                                                                                                                          is worth pointing out that we alwaysA: its class is created at runtime. Think about                                               pass newProxyInstance() an array of
 it: before your code runs there is no proxy               Is there any way to tell if a class is     interfaces—only interfaces are allowed, no                 Q:
class; it is created on demand from the set of   a Proxy class?                                 classes. The major restrictions are that
 interfaces you pass it.                                                                                                     all non-public interfaces need to be from
                                                    Yes. The Proxy class has a static          the same package. You also can’t have                 A:     My InvocationHandler seems like a                                        method called isProxyClass(). Calling this        interfaces with clashing method namesQ:very strange proxy; it doesn’t implement    method with a class will return true if the         (that is, two interfaces with a method with
any of the methods of the class it’s           class is a dynamic proxy class. Other than       the same signature). There are a few other
proxying.                                            that, the proxy class will act like any other      minor nuances as well, so at some point
                                                class that implements a particular set of        you should take a look at the fine print on
                                                    interfaces.                                dynamic proxies in the javadoc.

480      Chapter 11


---

## PDF page 519

the proxy pattern


Match each pattern with its description:

Pattern              Description

                            Wraps another object Decorator
                             and provides a different
                                   interface to it.

                            Wraps another object Facade
                             and provides additional
                                 behavior for it.

                            Wraps another object Proxy
                                       to control access to it.

                             Wraps a bunch of
Adapter                           objects to simplify
                                       their interface.


                                                      you are here 4      481


---

## PDF page 520

the proxy zoo

The Proxy Zoo

Welcome to the Objectville Zoo!
You now know about the remote, virtual, and protection proxies, but
out in the wild you’re going to see lots of mutations of this pattern.
Over here in the Proxy corner of the zoo we’ve got a nice collection
of wild proxy patterns that we’ve captured for your study.
Our job isn’t done; we’re sure you’re going to see more variations of
this pattern in the real world, so give us a hand in cataloging more
proxies. Let’s take a look at the existing collection:

                                                    Habitat: often seen in the location
                                          of corporate firewall systems.                         Firewall Proxy
                    controls access to a
                       set of network
                  resources, protecting
        the subject from “bad” clients.

                 Help find a habitat

                                                 Smart Reference Proxy
                                                          provides additional actions
                                                       whenever a subject is
                                                      referenced, such as counting
                                                   the number of references to
                                                                      an object.


               Caching Proxy provides
              temporary storage for                                                            Habitat: often seen in web server proxies as well                 results of operations                                                              as content management and publishing systems.              that are expensive. It
  can also allow multiple clients to share
  the results to reduce computation or
  network latency.


482      Chapter 11


---

## PDF page 521

the proxy pattern

                                                      Seen hanging around                                                                                         Collections,                                                                                 where it controls                                                           synchronized access to                                                                     an                                                                                         underlying set of objects                                                                in a multithreaded    Synchronization Proxy                                                environment.
   provides safe access to a
subject from multiple threads.


                     Help find a habitat                           Complexity Hiding Proxy
                                                              hides the complexity of
                                                        and controls access to a
                                                          complex set of classes.
                                                             This is sometimes called
                                                          the Facade Proxy for obvious reasons.
                                                 The Complexity Hiding Proxy differs from
                                                             the Facade Pattern in that the proxy
                                                                controls access, while the Facade Pattern
                                                                    just provides an alternative interface.

                Copy-On-Write Proxy
                   controls the copying of
                  an object by deferring
                 the copying of an                        Habitat: seen in the vicinity of the
              object until it is required by                  Java’s CopyOnWriteArrayList.
              a client. This is a variant of
             the Virtual Proxy.


           Field Notes: please add your observations of other proxies in the wild here:


                                                                       you are here 4      483


---

## PDF page 522

crossword puzzle

          Design Patterns Crossword
                             It’s been a LONG chapter. Why not unwind by doing a
                    crossword puzzle before it ends?

                         1                      2                 3                          4

           5                                                                   6

                                                                          7

                    8

                                                        9


                                                                                                               10

                                      11                                                    12

                                                                                             13


                                  14                                                    15


                    16                                                                  17


                         18                              19


ACROSS                          DOWN
5. Group of first album cover displayed (two words).            1. Objectville Matchmaking is for ________.
7. Commonly used proxy for web services (two words).         2. Java’s dynamic proxy forwards all requests to this (two
8. In RMI, the object that takes the network requests on       words).
the service side.                                                 3. This utility acts as a lookup service for RMI.
11. Proxy that protects method calls from unauthorized         4. Proxy that stands in for expensive objects.
callers.                                                           6. Remote ______ was used to implement the gumball
13. Group that did the album MCMXC a.D.                 machine monitor (two words).
14. A ________ proxy class is created at runtime.               9. Software developer agent was being this kind of proxy.
15. Place to learn about the many proxy variants.             10. Our first mistake: the gumball machine reporting was
16. The Album viewer used this kind of proxy.                 not _____.
17. In RMI, the proxy is called this.                           12. Similar to proxy, but with a different purpose.
18. We took one of these to learn RMI.
19. Why Elroy couldn’t get dates.

484      Chapter 11


---

## PDF page 523

the proxy pattern

         Tools for your Design Toolbox

          Your design toolbox is almost full; you’re prepared for
           almost any design problem that comes your way.
                                                              The Proxy Pattern provides
                                                                             a representative for another
                                                                                                object in order to control the
                                                                                                                client’s access to it. There                Basics        OO                                                         are a number of ways it can
                             Abstraction                                      manage that access.     Principles OO                                Encapsulation                               A Remote Proxy manages          what varies. Encapsulate                                                                                          interaction between a client                 over inheritance.   Polymorphism                                                                             and a remote object.  Favor composition                    not         Inheritance         to interfaces,                                                A Virtual Proxy controls   Program   implementations.                                                                    access to an object that is                             designs                    coupled                loosely                          interact.                                                           expensive to instantiate.    Strive for                that            objects    between                              extension                                        A Protection Proxy controls              be open for            should      Classes             for modification.                                 this                   access to the methods of an          closed     but                                                                                                object                                                                                   based                                                                                       on the caller.                                                   the                                   new principles                                                             close                  Do not          No                                          can you                                                                        all?           on abstractions.                                                them                                          chapter;                                                                 Depend                              classes.                                                                      Many other                                                                                                             variants                                                                                                                            of                                              remember                concrete      depend on                                     book and                                                                                            the Proxy Pattern exist                          friends.                                                                                                 including caching proxies,       Only talk to your
                                                                                            synchronization proxies,       Don’t call us, we’ll call you.                                  reason                                                                   firewall proxies, copy-on-write                    have only one                should                                                                             proxies, and so on.     A class
        to change.
                                                              Proxy is structurally similar
                                                                                                      to Decorator, but the two                                                    Our new pattern.
                                                             a                                                                         as                                                         Proxy acts                                      A                                   algorithms,   Patterns                     of                       familyOO                                                                                         patterns differ in their purpose.             a                      one-to-many               a                                                                          defines                                                                      for                                                                          The                                                                                           Decorator                                                                                                           Pattern                                                                                                 adds      -                          them                defines                                                                 representative         -                              an                             additional                           that Strategy                          so                  and                 Attach                               an                  one,           -                  -                       makesobjects   Observer            each                                    algorithm                                                                                         behavior                                                                                                                to                                                                                      an                                                                                                                     object,                                                                                                                   while                              Define                                                                           object.                   -                              Providedynamically.                          the                                     its             between                                                          another              Factory                            lets                                         one                                      all                           of  encapsulates                        object    Decorator                                       has                 an                                  but                            state,               to                 Strategy                                        only             Method                                 families    dependency                                              it.      Abstract                                   use                                       class                                    object,                   changes                     a                                                                                   Proxy                                                                                                        controls                                                                                                     access.                         an                           that        Factory             object               for       responsibilities                         Ensure                             flexible   interchangeable.                      creatingclients               -                                 of                            updated                                           request               a                                 without        one                         creating                          a                      and                from                                        point                                to                 for    when         interface                 provide                            objects                                        class                                      global                                 extending                     a           Singleton            interface                 -                         forEncapsulates                            which              are                                             request                  depedentnotified                           a      Decoratorsindependently   vary                          provide             or                                      you                       decide                                                                                                   classes.                  and                       subclassing                                                                                           Java’s                                                                                                                            built-in                                                                                                       support                                                                                                                                       for     dependents                                         lets         related                                       letting              to          Command                                Encapsulates                 subclasses                  -               instance                       concrete           let                         Method                           thereby                                         you                                              request                   their       alternative                            a                        object,                      Factory                           it.                                         different             Adapter                an                to      automatically           specifying                                                                                   Proxy                                                                                    can                                                                                                                build                                                                                         a                                                                                               dynamic                                 theletting               as                                                           its                             towith                              thereby                                  Encapsulates               access                   -                                                   alter              instantiate.                                  clients                                           you                                      to                          object,                                            different        functionality.                                      and                           instantiation                 as                                             lettingobject                                   with               Facadean                               an                                          requests,                 parameterize                 defer                                                                                       proxy                                                                                                   class                                                                                      on                                                                                  demand                                                                                               and                                     clients                                 thereby                                                          changes.                                  log                                 Allow                    -                                             or                class                         or                                        and        a                                               state                             object,                                               different                         queue                                                surrogate                 Statean                   as                                            requests,                    parameterize                             a                                             internalwith                                     log                    requests,                           or                                        clients                                                          its                                      Provideits                                                                                           dispatch                                                                                                                                            all                                                                                                                        calls                                                                                          on                                                                                                                                                                                                              it to                                                                                                a                                              to                                      operations.                            when                            queue               subclasses.                                              change                                          andobject                                    to                          undoable                          behavior                    Proxy                                                requests,                       parameterize                       requests,                                         another                                      appear                      -operations.                  support                              or                                        logfor                                           will                                                                                         handler                                                                                                               of                                                                                                 your                                                                                                        choosing.                              queue                            undoable                             object                                placeholder                   The                          requests,                     support                                                     it.                                            operations.                                  to                               undoableaccess                       supportclass.control                                                               Like any wrapper, proxies
                                                                                                                           will increase the number of
                                                                                         classes and objects in your
                                                                                           designs.


                                                                     you are here 4      485


---

## PDF page 524

exercise solutions


                        The NonOwnerInvocationHandler works just like the OwnerInvocationHandler except
                                that it allows calls to setGeekRating() and it disallows calls to any other set method.
                            Here’s our solution:

       import java.lang.reflect.*;
       public class NonOwnerInvocationHandler implements InvocationHandler {
           Person person;
           public NonOwnerInvocationHandler(Person person) {
               this.person = person;
           }
           public Object invoke(Object proxy, Method method, Object[] args)
                   throws IllegalAccessException {
               try {
                   if (method.getName().startsWith("get")) {
                       return method.invoke(person, args);
                   } else if (method.getName().equals("setGeekRating")) {
                       return method.invoke(person, args);
                   } else if (method.getName().startsWith("set")) {
                       throw new IllegalAccessException();
                   }
               } catch (InvocationTargetException e) {
                   e.printStackTrace();
               }
               return null;
           }
       }
       Design Puzzle Solution

                                  The ImageProxy class appears to have two states that are controlled
                                     by conditional statements. Can you think of another pattern that might
                                        clean up this code? How would you redesign ImageProxy?

        Use the State Pattern: implement two states, ImageLoaded and ImageNotLoaded. Then put
          the code from the if statements into their respective states. Start in the ImageNotLoaded state
        and then transition to the ImageLoaded state once the ImageIcon had been retrieved.


486      Chapter 11


---

## PDF page 525

the proxy pattern


                       While it is a little complicated, there isn’t much to creating a dynamic
                          proxy. Why don’t you write getNonOwnerProxy(), which returns a
                       proxy for the NonOwnerInvocationHandler? Here’s our solution:

   Person getNonOwnerProxy(Person person) {

       return (Person) Proxy.newProxyInstance(
               person.getClass().getClassLoader(),
               person.getClass().getInterfaces(),
               new NonOwnerInvocationHandler(person));
   }


    Design Patterns Crossword Solution


              1                      2                 3                          4         G               I           R                V
5                                                                   6A  P H  E  X  T W  I N       M     M         I
                                                               7         E             V            I   W  E  B  P  R O  X  Y
         8      S  K  E  L  E  T O N        R       T       T
                                             9        S              C      P     E      H      U
                    A     R    G      O      A
                      T    O     I       D         L
                                                                                                   10                           I     T    S         I                   R
                           11                                                    12                      P  R O  T  E  C  T  I O N       D          E
                                                                                 13                   N     C     R       V        E N  I  G M A
                   H    T     Y      O        C        O
                       14                                                    15             D  Y N A M  I  C           C    Z O O       T
                   N    O           A        R           E
                     D    N            T      A
         16                                                                  17      V  I  R  T U A  L                      I    S  T U  B
                        E               O      O
              18                              19        D  E  T O U  R    S U  S  P  E N  D  E  R  S


                                                             you are here 4      487


---

## PDF page 526

exercise solutions


                  SOlUTion


                Match each pattern with its description:

          Pattern              Description

                                          Wraps another object                Decorator
                                           and provides a different
                                                    interface to it.

                                          Wraps another object               Facade
                                           and provides additional
                                                behavior for it.

                                          Wraps another object               Proxy
                                                          to control access to it.

                                          Wraps a bunch of
               Adapter                           objects to simplify
                                                          their interface.


488      Chapter 11


---

## PDF page 527

the proxy pattern

       Ready Bake             The code for the Album Cover Viewer
       Code


package headfirst.designpatterns.proxy.virtualproxy;

import java.net.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
public class ImageProxyTestDrive {
    ImageComponent imageComponent;
    JFrame frame = new JFrame("Album Cover Viewer");
    JMenuBar menuBar;
    JMenu menu;
    Hashtable<String, String> albums = new Hashtable<String, String>();

    public static void main (String[] args) throws Exception {
        ImageProxyTestDrive testDrive = new ImageProxyTestDrive();
    }

    public ImageProxyTestDrive() throws Exception{
        albums.put("Buddha Bar","http://images.amazon.com/images/P/B00009XBYK.01.LZZZZZZZ.
jpg");
        albums.put("Ima","http://images.amazon.com/images/P/B000005IRM.01.LZZZZZZZ.jpg");
        albums.put("Karma","http://images.amazon.com/images/P/B000005DCB.01.LZZZZZZZ.
gif");
        albums.put("MCMXC a.D.","http://images.amazon.com/images/P/B000002URV.01.LZZZZZZZ.
jpg");
        albums.put("Northern Exposure","http://images.amazon.com/images/P/B000003SFN.01.
LZZZZZZZ.jpg");
        albums.put("Selected Ambient Works, Vol. 2","http://images.amazon.com/images/P/
B000002MNZ.01.LZZZZZZZ.jpg");

        URL initialURL = new URL((String)albums.get("Selected Ambient Works, Vol. 2"));
        menuBar = new JMenuBar();
        menu = new JMenu("Favorite Albums");
        menuBar.add(menu);


                                                                       you are here 4      489


---

## PDF page 528

ready-bake code: album cover viewer

                                 The code for the Album Cover       Ready Bake
                                              Viewer, continued...       Code

        frame.setJMenuBar(menuBar);

        for(Enumeration e = albums.keys(); e.hasMoreElements();) {
            String name = (String)e.nextElement();
            JMenuItem menuItem = new JMenuItem(name);
            menu.add(menuItem);
            menuItem.addActionListener(event -> {
                imageComponent.setIcon(
                     new ImageProxy(getAlbumUrl(event.getActionCommand())));
                frame.repaint();
            });
        }

        // set up frame and menus

        Icon icon = new ImageProxy(initialURL);
        imageComponent = new ImageComponent(icon);
        frame.getContentPane().add(imageComponent);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800,600);
        frame.setVisible(true);

    }
    URL getAlbumUrl(String name) {
        try {
            return new URL((String)albums.get(name));
        } catch (MalformedURLException e) {
            e.printStackTrace();
            return null;
        }
    }
}


490      Chapter 11


---

## PDF page 529

the proxy pattern

                                 The code for the Album Cover       Ready Bake
                                              Viewer, continued...       Code

package headfirst.designpatterns.proxy.virtualproxy;
import java.net.*;
import java.awt.*;
import javax.swing.*;
class ImageProxy implements Icon {
    volatile ImageIcon imageIcon;
    final URL imageURL;
    Thread retrievalThread;
    boolean retrieving = false;
    public ImageProxy(URL url) { imageURL = url; }
    public int getIconWidth() {
        if (imageIcon != null) {
            return imageIcon.getIconWidth();
        } else {
            return 800;
        }
    }
    public int getIconHeight() {
        if (imageIcon != null) {
            return imageIcon.getIconHeight();
        } else {
            return 600;
        }
    }
    synchronized void setImageIcon(ImageIcon imageIcon) {
        this.imageIcon = imageIcon;
    }
    public void paintIcon(final Component c, Graphics  g, int x,  int y) {
        if (imageIcon != null) {
            imageIcon.paintIcon(c, g, x, y);
        } else {
            g.drawString("Loading album cover, please wait...", x+300, y+190);
            if (!retrieving) {
                retrieving = true;

                                                                       you are here 4      491


---

## PDF page 530

ready-bake code: album cover viewer

                          The code for the Album Cover Viewer,       Ready Bake
                                                             continued...       Code

                retrievalThread = new Thread(new Runnable() {
                    public void run() {
                        try {
                            setImageIcon(new ImageIcon(imageURL, "Album Cover"));
                            c.repaint();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                });
                retrievalThread.start();
            }
        }
    }
}

package headfirst.designpatterns.proxy.virtualproxy;
import java.awt.*;
import javax.swing.*;
class ImageComponent extends JComponent {
    private Icon icon;
    public ImageComponent(Icon icon) {
        this.icon = icon;
    }
    public void setIcon(Icon icon) {
        this.icon = icon;
    }
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        int w = icon.getIconWidth();
        int h = icon.getIconHeight();
        int x = (800 - w)/2;
        int y = (600 - h)/2;
        icon.paintIcon(this, g, x, y);
    }
}


492      Chapter 11
