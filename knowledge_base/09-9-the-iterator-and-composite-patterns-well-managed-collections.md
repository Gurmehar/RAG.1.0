# 9: the Iterator and Composite Patterns: Well-Managed Collections

_Extracted from PDF pages 355-418. Text only; images and diagrams are not embedded._


---

## PDF page 355

9 the Iterator and Composite Patterns
      Well-Managed
            Collections


           You bet I keep
          my collections well
             encapsulated!


      There are lots of ways to stuff objects into a collection.
        Put them into an Array, a Stack, a List, a hash map—take your pick. Each has its
       own advantages and tradeoffs. But at some point your clients are going to want
          to iterate over those objects, and when they do, are you going to show them your
         implementation? We certainly hope not! That just wouldn’t be professional. Well, you
          don’t have to risk your career; in this chapter you’re going to see how you can allow
         your clients to iterate through your objects without ever getting a peek at how you store
         your objects. You’re also going to learn how to create some super collections of objects
          that can leap over some impressive data structures in a single bound. And if that’s not
        enough, you’re also going to learn a thing or two about object responsibility.


                                                                          this is a new chapter      317


---

## PDF page 356

a business merger

Breaking News: Objectville Diner and
Objectville Pancake House Merge
That’s great news! Now we can get those delicious pancake breakfasts at the
Pancake House and those yummy lunches at the Diner all in one place. But there
seems to be a slight problem...


                                                                                ...but we can’t agree on how to implement
                                                            our menus. That joker over there used an
          They want to use my Pancake House                                                             ArrayList to hold his menu items, and I
          menu as the breakfast menu and                                                         used an Array. Neither one of us is willing to
           the Diner’s menu as the lunch menu.                                                         change our implementations...we just have
          We’ve agreed on an implementation                                                            too much code written that depends on
           for the menu items...                                                                 them.


            Lou
                                                              Mel


318      Chapter 9


---

## PDF page 357

the iterator and composite patterns

Check out the Menu Items
At least Lou and Mel agree on the                         Objectville                                           Diner                                                                  Vegetarian BLTimplementation of the MenuItems. Let’s
                                                                                          (Fakin’)check out the items on each menu, and                                                                      Bacon with lettuce & tomato on      2.99                                                                 whole                                                                    wheatalso take a look at the implementation.                   BLT
                                                               Bacon                                                                           with                                                          Objectville                                                                                                                  2.99                                                                                              lettuce & tomato                                                   Pancake                                                      Soup                                                    House                                                                           on whole wheat                                                                   of the                                                               day                                                                                     K&B’s                                                                                     Pancake                                               A                                                                bowl                                                                             of                                                                                                         Breakfast                                                                                                                 3.29                                                                             the soup                                                                                       of the day,                                                                                                      with                                                                                                                                        2.99                                                                                              withPancakes                                                  a                                                                                                           scrambled                                                                               side                                                                            of                                                                             potato                                                                                                              eggs and toast                                                                                     salad             The Diner menu has lots of lunch                                                       Hot                                                   Dog                                       House                                                                                      Regular                               Pancake                                                                                       Pancake                          the                          while                                                                                                          Breakfast                   items,                                              A                                                                                            Pancakes                                                                   hot dog,                                                                                                     with                                                                                                                                       2.99                                                                             with                                          items.                                                                                                               3.05fried                                                                                                                       eggs,                                                                                            sauerkraut,                     of breakfast                                                                                                                sausage                                                                                                                            relish,                    consists                                                                                                          onions,                                                                 topped                                                                          with                                   a                                      name,                                                                                cheese                             a                                 has                            item                                                                                        Blueberry                     menu                Every                                                                                          Pancakes                                                       Steamed                                                                      Veggies                                                               and                                                                                           Pancakes                                                                    Brown                                          price.                          a                                                                                                                                      3.49                                                                               made                                                                                           Rice                          and                                                                                                          with                                              A                                                                                                                              fresh                    description,                                                                 medley                                                                                                              3.99                                                                             of                                                                             and                                                                                                                                           blueberries,                                                                        steamed                                                                                                         blueberry                                                                                                            syrup                                                                                            vegetables                                                                                                 over                                                                                      brown                                                                                                                                 rice
                                                                                         Waffles
                                                                                                    Waffles public        class              MenuItem {                                                                                                                                     3.59                                                                                                  with your choice of                                                                                          or                                                                                                                                    blueberries     String            name;                                                                                                           strawberries
     String description;
     boolean vegetarian;
     double price;
     public MenuItem(String name,
                     String description,
                     boolean vegetarian,
                                    A                     double                            price)                                                       MenuItem                                                                                  consists                                                                of                                                              a                                                                                  name,                                                                   a     {                                             a                                                                flag                                                                                                       description,                                                         to indicate                                                                            if                                                                      the                                                                               item                                                                                                              is         this.name                  =                     name;                                                   and                                                                                                   vegetarian,                                                a price.                                                               You                                                                              pass                                                                                                      all         this.description                         =                                                                                 these                                                                                                    values                                                                                                  into the                            description;           constructor                                                             to         this.vegetarian = vegetarian;                                  initialize the                                                                                 MenuItem.         this.price = price;
     }
     public String getName() {
         return name;
     }
                                                     These getter methods let you access     public            String                   getDescription() {                                                     the fields of the menu item.         return                description;
     }
     public double getPrice() {
         return price;
     }
     public boolean isVegetarian() {
         return vegetarian;
     }
 }

                                                                       you are here 4      319


---

## PDF page 358

two menu implementations

Lou and Mel’s Menu implementations
                                                              I used an ArrayList
Now let’s take a look at what Lou and Mel are                        so I can easily expand
                                                       my menu.arguing about. They both have lots of time and
code invested in the way they store their menu
items in a menu, and lots of other code that
depends on it.                             Here’s Lou’s implementation of
                        the Pancake House menu.
 public class PancakeHouseMenu {                        Lou’s using an ArrayList
     List<MenuItem> menuItems;                                class to store his menu items.
     public PancakeHouseMenu() {
         menuItems = new ArrayList<MenuItem>();
         addItem("K&B's Pancake Breakfast",
             "Pancakes with scrambled eggs and toast",                                                                Each menu item is added to the             true,                                                                      ArrayList here, in the constructor.             2.99);
                                                                                a                                                                                             name,                                                                                        has a                                                                      MenuItem                                                                Each         addItem("Regular                          Pancake                                  Breakfast",                                                                                                                                   it’s a                                                                                       not                                                                                     or                                                                               whether                                                                                    description,             "Pancakes with                            fried                                  eggs, sausage",             false,                                                      vegetarian item, and the price.
             2.99);
         addItem("Blueberry Pancakes",
             "Pancakes made with fresh blueberries",
             true,
             3.49);
         addItem("Waffles",
             "Waffles with your choice of blueberries or strawberries",
             true,
             3.59);
     }                                                                 To add a menu item, Lou creates a new     public void addItem(String name, String description,    MenuItem object, passing in each argument,                         boolean vegetarian, double price)   and then adds it to the ArrayList.
     {
         MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
         menuItems.add(menuItem);
     }                                                      The getMenuItems() method returns the
                                                                                            list of menu items.     public ArrayList<MenuItem> getMenuItems() {
         return menuItems;     }                                     Lou has a bunch of other menu code that                                                                                  implementation. He                                                    depends on the ArrayList     // other menu methods here               doesn’t want to have to rewrite all that code! }

320      Chapter 9


---

## PDF page 359

the iterator and composite patterns


                                    Haah! An ArrayList...I used a
                             REAL Array so I can control the
                                maximum size of my menu.


                                                                   of the Diner menu.                                                                          implementation                                           And here’s Mel’s
public class DinerMenu {                                                   Mel takes a different approach; he’s using an Array    static final int MAX_ITEMS = 6;                                                                        class so he can control the max size of the menu.    int numberOfItems = 0;
    MenuItem[] menuItems;
    public DinerMenu() {                                     Like Lou, Mel creates his menu items in the
        menuItems = new MenuItem[MAX_ITEMS];              constructor, using the addItem() helper method.
        addItem("Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat", true, 2.99);
        addItem("BLT",
            "Bacon with lettuce & tomato on whole wheat", false, 2.99);
        addItem("Soup of the day",
            "Soup of the day, with a side of potato salad", false, 3.29);
        addItem("Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            false, 3.05);
        // a couple of other Diner Menu items added here    addItem() takes all the parameters
    }                                                                        necessary to create a MenuItem and                                                                                   instantiates one. It also checks to make    public void addItem(String name, String description,                                                                                sure we haven’t hit the menu size limit.                         boolean vegetarian, double price)
    {
        MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
        if (numberOfItems >= MAX_ITEMS) {
            System.err.println("Sorry, menu is full!  Can't add item to menu");
        } else {                                                          Mel specifically wants to keep his menu            menuItems[numberOfItems] = menuItem;                                                                 under a certain size (presumably so he            numberOfItems = numberOfItems + 1;                                                                       doesn’t have to remember too many recipes).        }
    }
                                                  getMenuItems() returns the array of menu items.    public MenuItem[] getMenuItems() {
        return menuItems;
    }
                                             Like Lou, Mel has a bunch of code that depends on the implementation
    // other menu methods here                                          of his menu being an Array. He’s too busy cooking to rewrite all of this.}

                                                                      you are here 4      321


---

## PDF page 360

java-enabled waitress

What’s the problem with having two different
menu representations?
                                                                                                   isgettingTo see why having two different menu representations complicates                                Waitress                                                              The
things, let’s try implementing a client that uses the two menus.                                                                                         Java-enabled.
Imagine you have been hired by the new company formed by the
merger of the Diner and the Pancake House to create a Java-enabled
waitress (this is Objectville, after all). The spec for the Java-enabled
waitress specifies that she can print a custom menu for customers on
demand, and even tell you if a menu item is vegetarian without having
to ask the cook—now that’s an innovation!
Let’s check out the spec for the waitress, and then step through what it
might take to implement her...


The Java-Enabled Waitress Specification

                                       "Alice"                              code-name                    Waitress:       Java-Enabled
        printMenu()                                     breakfast and         - prints every item on the             lunch menus
         printBreakfastMenu()                         breakfast items         - prints just
         printLunchMenu()                                                                                 for                                                                                        spec          - prints just lunch items                          The                                                                                         Waitress                                                                       the
          printVegetarianMenu()                                   menu items                          vegetarian          - prints all

                                                true          isItemVegetarian(name)                                         returns           - given the name of an item,                                           otherwise,                               vegetarian,              if the items is
                returns false


322      Chapter 9


---

## PDF page 361

the iterator and composite patterns

Implementing the spec: our first attempt


Let’s start by stepping through how we’d implement the printMenu() method:

  1  To print all the items on each menu, you’ll need to call the getMenuItems()
      method on the PancakeHouseMenu and the DinerMenu to retrieve their           The method looks        respective menu items. Note that each returns a different type:                      the same, but the                                                                                                       returning                                                                                                               calls are
                                                                                            different types.      PancakeHouseMenu pancakeHouseMenu = new PancakeHouseMenu();
      ArrayList<MenuItem> breakfastItems = pancakeHouseMenu.getMenuItems();

       DinerMenu dinerMenu = new DinerMenu();
                                                                 The implementation is showing       MenuItem[] lunchItems = dinerMenu.getMenuItems();                                                                                    through: breakfast items are
                                                                                                   in an ArrayList, and lunch
                                                                                   items are in an Array.
  2  Now, to print out the items from the PancakeHouseMenu, we’ll loop through the
        items on the breakfastItems ArrayList. And to print out the Diner items, we’ll loop
       through the Array.                                                       Now, we have to
                                                                                       implement two
         for (int i = 0; i < breakfastItems.size(); i++) {                different loops to
             MenuItem menuItem = breakfastItems.get(i);                    step through the two                                                                                            implementations of the             System.out.print(menuItem.getName() + " ");                                                                               menu items...             System.out.println(menuItem.getPrice() + " ");
                                                                                                                       ...one loop for the             System.out.println(menuItem.getDescription());                                                                                                   ArrayList...         }
                                                                                                                ...and another for         for (int i = 0; i < lunchItems.length; i++) {
                                                                                    the Array.             MenuItem menuItem = lunchItems[i];
             System.out.print(menuItem.getName() + " ");
             System.out.println(menuItem.getPrice() + " ");
             System.out.println(menuItem.getDescription());
         }

  3   Implementing every other method in the Waitress is going to be a variation of
         this theme. We’re always going to need to get both menus and use two loops to
         iterate through their items. If another restaurant with a different implementation
           is acquired, then we’ll have three loops.


                                                                       you are here 4      323


---

## PDF page 362

what’s the goal


          Based on our implementation of printMenu(), which of the following apply?


   ❏  A. We are coding to the          ❏  D. The Waitress needs to know how each
           PancakeHouseMenu and DinerMenu         menu represents its internal collection of
             concrete implementations, not to an          menu items; this violates encapsulation.
               interface.                         ❏  E. We have duplicate code: the printMenu()
   ❏  B. The Waitress doesn’t implement the            method needs two separate loops to
              Java Waitress API and so she isn’t                   iterate over the two different kinds of
             adhering to a standard.                       menus. And if we added a third menu,
                                                         we’d have yet another loop.   ❏  C. If we decided to switch from using
           DinerMenu to another type of menu   ❏   F. The implementation isn’t based on
               that implemented its list of menu items      MXML (Menu XML) and so isn’t as
             with a hash table, we’d have to modify            interoperable as it should be.
            a lot of code in the Waitress.


 What now?

  Mel and Lou are putting us in a difficult position. They don’t want to change their
  implementations because it would mean rewriting a lot of code that is in each respective
  menu class. But if one of them doesn’t give in, then we’re going to have the job of
  implementing a Waitress that will be hard to maintain and extend.
   It would really be nice if we could find a way to allow them to implement the same
   interface for their menus (they’re already close, except for the return type of the
  getMenuItems() method). That way we can minimize the concrete references in the
   Waitress code and also hopefully get rid of the multiple loops required to iterate over
  both menus.
  Sound good? Well, how are we going to do that?


324      Chapter 9


---

## PDF page 363

the iterator and composite patterns

Can we encapsulate the iteration?

If we’ve learned one thing in this book, it’s to encapsulate what varies. It’s
obvious what is changing here: the iteration caused by different collections of
objects being returned from the menus. But can we encapsulate this? Let’s work
through the idea...


 1  To iterate through the breakfast items, we use the size() and get()
     methods on the ArrayList:

 for (int i = 0; i < breakfastItems.size(); i++) {
     MenuItem menuItem = breakfastItems.get(i);
}
                  get(1)            get(2)   get(3)           get() helps us step
                get(0)                                       through each item.
                          ArrayList

                                                     An ArrayList
                                                         of MenuItems                     MenuItem MenuItem MenuItem  MenuItem
                                                      1       2       3        4


 2  And to iterate through the lunch items we use the Array length field and
     the array subscript notation on the MenuItem Array.                                                               Array

                                                                      lunchItems[0]                                                                                                                                                                 1for (int i = 0; i < lunchItems.length; i++) {                  MenuItem
                                                                      lunchItems[1]    MenuItem menuItem = lunchItems[i];                                          2
                                                                      MenuItem}                                                                    lunchItems[2]
                                                                                                                       3
                                                                    MenuItem                                                                     lunchItems[3]                                       We use the array
                                                                                                                       4                                                         subscripts to step
                                                                          MenuItem                                                  through items.
                                                              An Array of
                                                                           MenuItems.


                                                                       you are here 4      325


---

## PDF page 364

encapsulating iteration

 3  Now what if we create an object, let’s call it an Iterator,
      that encapsulates the way we iterate through a                         We ask the breakfastMenu
       collection of objects? Let’s try this on the ArrayList:                       for an iterator of its
                                                                                      MenuItems.
   Iterator iterator = breakfastMenu.createIterator();
                                                           And while there are more items left...
   while (iterator.hasNext()) {
       MenuItem menuItem = iterator.next();
   }                                             next()                                                                                                  ...we get the next item.


                                                                         get(2)
                                                                                        get(3)
                 Iterator         get(1)
                                                      get(0)             ArrayList
      The client just calls hasNext()
       and next(); behind the scenes the
        iterator calls get() on the ArrayList.
                                                   MenuItem MenuItem MenuItem  MenuItem
                                                                                                                             1       2       3        4

 4    Let’s try that on the Array too:
   Iterator iterator = lunchMenu.createIterator();
   while (iterator.hasNext()) {
       MenuItem menuItem = iterator.next();
   }
        Wow, this code                                   next()                      Array
            is exactly the
         same as the                                                   lunchItems[0]          1         breakfastMenu                                                      MenuItem
          code.                                                         lunchItems[1]
                                                                                                                       2
                             to       Same situation here: the client just calls     Iterar                         MenuItem                                                                      lunchItems[2]
                                                                                                                       3        hasNext() and next(); behind the scenes,
                                                                    MenuItem        the iterator indexes into the Array.                                lunchItems[3]
                                                                                                                       4
                                                                          MenuItem


326      Chapter 9


---

## PDF page 365

the iterator and composite patterns

Meet the Iterator Pattern

Well, it looks like our plan of encapsulating iteration just might
actually work; and as you’ve probably already guessed, it is a
Design Pattern called the Iterator Pattern.
The first thing you need to know about the Iterator Pattern is that
it relies on an interface called Iterator. Here’s one possible Iterator
interface:
                             The hasNext() method
                                              tells us if there are
                                  more elements in the
                 <<interface>>                                      aggregate to iterate
                       Iterator                                       through.
             hasNext()
               next()
                               The next() method
                                        returns the next
                                       object in the
                                         aggregate.

Now, once we have this interface, we can implement Iterators for
any kind of collection of objects: arrays, lists, hash maps ... pick your
favorite collection of objects. Let’s say we wanted to implement the                                                             When we sayIterator for the Array used in the DinerMenu. It would look like this:                                                      COLLECTION we just mean a group
                                                                     of objects. They might be stored in
                                                                     very different data structures like lists,
                <<interface>>                                                        arrays, or hash maps, but they’re still
                      Iterator                                                                collections. We also sometimes call
            hasNext()                                                               these AGGREGATES.
              next()


                             DinerMenuIterator is an
              DinerMenuIterator                               implementation of Iterator
            hasNext()                that knows how to iterate
              next()                    over an array of MenuItems.


Let’s go ahead and implement this Iterator and incorporate it into
DinerMenu to see how this works...


                                                                       you are here 4      327


---

## PDF page 366

using iterator

Adding an Iterator to DinerMenu

To add an iterator to the DinerMenu, we first need to define the Iterator interface:
                                           Here are our two methods:
                                    The hasNext() method returns a boolean                                                    indicating whether or not there are  public interface Iterator {                                         more elements to iterate over...
      boolean hasNext();
      MenuItem next();                     ...and the next() method  }                                          returns the next element.

And now we need to implement a concrete Iterator that works for the Diner menu:
                                                          We implement the
                                                                            Iterator interface.
  public class DinerMenuIterator implements Iterator {            maintains the                                                                               position      MenuItem[] items;                                                        position of the                                                                     current      int position = 0;                                              iteration over the array.

      public DinerMenuIterator(MenuItem[] items) {
                                                             The constructor takes the          this.items = items;                                                                         array of menu items we are      }                                                                                  going to iterate over.
      public MenuItem next() {
          MenuItem menuItem = items[position];           The next() method returns the
                                                                    next item in the array and          position = position + 1;                                                                          increments the position.          return menuItem;
      }

      public boolean hasNext() {
          if (position >= items.length || items[position] == null) {
              return false;
          } else {
              return true;                                                                         Because the diner chef went ahead and
          }                           The hasNext() method checks to see      allocated a max sized array, we need to                                     if we’ve seen all the elements of the     check not only if we are at the end of      }                                 array and returns true if there are     the array, but also if the next item is null,  }                           more to iterate through.                                                                           which indicates there are no more items.

328      Chapter 9


---

## PDF page 367

the iterator and composite patterns

Reworking the DinerMenu with Iterator

Okay, we’ve got the iterator. Time to work it into the DinerMenu; all we need to do is
add one method to create a DinerMenuIterator and return it to the client:

         public class DinerMenu {
             static final int MAX_ITEMS = 6;
             int numberOfItems = 0;
             MenuItem[] menuItems;

             // constructor here

             // addItem here                                                                        We’re not going to need the getMenuItems()
                                                             method anymore; in fact, we don’t want it
             public MenuItem[] getMenuItems() {           because it exposes our internal implementation!
                 return menuItems;
             }

             public Iterator createIterator() {
                 return new DinerMenuIterator(menuItems);                                                                                    Here’s the createIterator() method.
             }                                                                 It creates a DinerMenuIterator
                                                                  from the menuItems array and
             // other menu methods here                           returns it to the client.
         }
                        We’re returning the Iterator interface. The client
                         doesn’t need to know how the MenuItems are maintained
                             in the DinerMenu, nor does it need to know how the
                      DinerMenuIterator is implemented. It just needs to use
                      the iterators to step through the items in the menu.


                 Go ahead and implement the PancakeHouseIterator yourself and make the changes
                    needed to incorporate it into the PancakeHouseMenu.


                                                                       you are here 4      329


---

## PDF page 368

fixing the waitress

Fixing up the Waitress code

Now we need to integrate the iterator code into the
Waitress class. We should be able to get rid of some
of the redundancy in the process. Integration is pretty
straightforward: first we create a printMenu() method
that takes an Iterator; then we use the createIterator()
method on each menu to retrieve the Iterator and                  New and
pass it to the new method.                                             improved with
                                                                             Iterator.

  public class Waitress {
      PancakeHouseMenu pancakeHouseMenu;                      In the constructor the Waitress
      DinerMenu dinerMenu;                                             class takes the two menus.
      public Waitress(PancakeHouseMenu pancakeHouseMenu, DinerMenu dinerMenu) {
          this.pancakeHouseMenu = pancakeHouseMenu;
          this.dinerMenu = dinerMenu;
      }                                                             The printMenu()                                                                            method now creates                                                                                                         iterators, one for      public void printMenu() {                                         two                                                                                    each menu...          Iterator pancakeIterator = pancakeHouseMenu.createIterator();
          Iterator dinerIterator = dinerMenu.createIterator();
          System.out.println("MENU\n----\nBREAKFAST");                                                                                                   ...and then calls the          printMenu(pancakeIterator);                                                                                  overloaded printMenu()          System.out.println("\nLUNCH");                                                                              with each iterator.
          printMenu(dinerIterator);
      }
                                                                  Test if there are
                                                                any more items.         The overloaded      private void printMenu(Iterator iterator) {                                                                                           printMenu()          while (iterator.hasNext()) {                        Get the                                                                                method uses                                                                         next item.              MenuItem menuItem = iterator.next();                                                                                     the Iterator to              System.out.print(menuItem.getName() + ", ");                                                                                               step through
              System.out.print(menuItem.getPrice() + " -- ");              the menu items
              System.out.println(menuItem.getDescription());               and print them.
          }
      }                                                                Use the item to
      // other methods here         Note that we’re down      get name, price,                                                               and description                                         to one loop.  }                                                               and print them.


330      Chapter 9


---

## PDF page 369

the iterator and composite patterns

Testing our code

It’s time to put everything to a test. Let’s write some
test drive code and see how the Waitress works...

                                                                                   First we create the new menus. public class MenuTestDrive {
     public static void main(String args[]) {
         PancakeHouseMenu pancakeHouseMenu = new PancakeHouseMenu();
         DinerMenu dinerMenu = new DinerMenu();
                                                                                  Then we create a         Waitress waitress = new Waitress(pancakeHouseMenu, dinerMenu);                                                                                                      Waitress and pass
                                                                                              her the menus.
         waitress.printMenu();
     }                                   Then we print them. }

Here’s the test run...


    File Edit  Window Help
 % java DinerMenuTestDrive
 MENU                                                                                     First we iterate
 ----                                                                             through the                                                                                      pancake menu... BREAKFAST
 K&B’s Pancake Breakfast, 2.99 -- Pancakes with scrambled eggs and toast
 Regular Pancake Breakfast, 2.99 -- Pancakes with fried eggs, sausage               ...and then
 Blueberry Pancakes, 3.49 -- Pancakes made with fresh blueberries                the lunch
 Waffles, 3.59 -- Waffles with your choice of blueberries or strawberries       menu, all                                                                                                     with the
                                                                                                 same LUNCH                                                                                                                 iteration
 Vegetarian BLT, 2.99 -- (Fakin’) Bacon with lettuce & tomato on whole wheat   code.
 BLT, 2.99 -- Bacon with lettuce & tomato on whole wheat
 Soup of the day, 3.29 -- Soup of the day, with a side of potato salad
 Hot Dog, 3.05 -- A hot dog, with sauerkraut, relish, onions, topped with cheese
 Steamed Veggies and Brown Rice, 3.99 -- Steamed vegetables over brown rice
 Pasta, 3.89 -- Spaghetti with marinara sauce, and a slice of sourdough bread
 %


                                                                       you are here 4      331


---

## PDF page 370

comparing our implementations

What have we done so far?                 Woohoo! No code                                                            changes other
                                                           than adding the
For starters, we’ve made our Objectville cooks                                                           createIterator() method.
very happy. They settled their differences and
kept their own implementations. Once we gave
them a PancakeHouseMenuIterator and a
DinerMenuIterator, all they had to do was add a
createIterator() method and they were finished.
We’ve also helped ourselves in the process. The
Waitress will be much easier to maintain and
extend down the road. Let’s go through exactly
what we did and think about the consequences:
                                                                              Veggie burger


            Hard-to-Maintain                         New, Hip
         Waitress Implementation             Waitress Powered by Iterator

         The Menus are not well                       The Menu implementations are now
           encapsulated; we can see the                      encapsulated. The Waitress has
           Diner is using an ArrayList and the               no idea how the Menus hold their
         Pancake House an Array.                              collection of menu items.

       We need two loops to iterate through                    All we need is a loop that
            the MenuItems.                                     polymorphically handles any
                                                                     collection of items as long as it
                                                         implements Iterator.

         The Waitress is bound to concrete               The Waitress now uses an interface
           classes (MenuItem[] and ArrayList).                     (Iterator).


         The Waitress is bound to two different             The Menu interfaces are now exactly
           concrete Menu classes, despite their                 the same and, uh oh, we still don’t
            interfaces being almost identical.                  have a common interface, which
                                                means the Waitress is still bound to
                                                        two concrete Menu classes. We’d
                                                                     better fix that.

332      Chapter 9


---

## PDF page 371

the iterator and composite patterns

Reviewing our current design...

Before we clean things up, let’s get a bird’s-eye view of our current design.


                       the        The Iterator allows the Waitress to be decoupled                 implement      two menus                                                                              concrete                                                                     the These                                                              of                                                          implementation                                                      actual                                           the                                   from                        but                  methods,            set of                                                                                                                         is           We’re now using a                                                                    a Menu same exact                                                                                if                                                         need to know                                                       doesn’t                                            She                                                    classes.                          same                      the             implementing                                                                                 common       aren’t                                                                                  with                                                                              or                                                                                                        Iterator they                                                                       ArrayList,                                                                an                                                             Array,                                                       an                                                    with                               this        implemented                        fix                   to                  going                                                   ®           We’re                                                                                                  interface                                                                                  can                                                                                      she  interface.                                                                                                             is that                                                                 about                                                                  cares                                                               she                                                                  All                                                       notes.                                          Post-it                          any                   from               Waitress                                                                                  and         the                                                                                                       we’ve      free  and                                                                            iterating.                                                             her                                                    do                                                      to                                       get an Iterator                         Menus.                 concrete             on                                                                                           implemented                                                                                         two  dependencies
                                                                                            concrete classes.


                      PancakeHouseMenu                           Waitress                              <<interface>>
                                                                                                                                       Iterator
                        menuItems                                        printMenu()
                                                                                                                           hasNext()
                                 createIterator()                                                                                                                                           next()

                            DinerMenu
                         menuItems

                                 createIterator()                                                   PancakeHouseMenuIterator         DinerMenuIterator

                                                                                                          hasNext()                           hasNext()
                                                                                                                        next()                                   next()


                                                                         and DinerMenu                                                                 PancakeHouseMenu                                                                                          createIterator()     Note that the iterator gives us a way to                                                                    the new                                                                   implement                                                                                                       creating                                                                                                 responsible for      step through the elements of an aggregate                                                                     they are                                                                method;     without              forcing                                                                                                    respective menu                   the                         aggregate                                to                                      clutter                                                                         for their                                                     its                                                                           iterator                                                            the     own          interface                  with                    a                         bunch                           of                               methods                                       to                                                                                 implementations.                                                                           items’      support              traversal                   of                              its                              elements.                                       It also                                                  allows     the implementation of the iterator to live
     outside of the aggregate; in other words, we’ve     encapsulated the iteration.


                                                                       you are here 4      333


---

## PDF page 372

using java’s iterator

Making some improvements...

Okay, we know the interfaces of PancakeHouseMenu and DinerMenu are exactly the same
and yet we haven’t defined a common interface for them. So, we’re going to do that and clean
up the Waitress a little more.
You may be wondering why we’re not using the Java Iterator interface—we did that so you
could see how to build an iterator from scratch. Now that we’ve done that, we’re going to
switch to using the Java Iterator interface, because we’ll get a lot of leverage by implementing
that instead of our home-grown Iterator interface. What kind of leverage? You’ll soon see.
First, let’s check out the java.util.Iterator interface:
                                                            This looks just like our previous definition...                                                   <<interface>>
                                                               Iterator
                                                     hasNext()
                                                            next()                                                                       ...except we have an additional method that                                                   remove()                                                                      allows us to remove the last item returned
                                                       by the next() method from the aggregate.


This is going to be a piece of cake: we just need to change the interface that both
PancakeHouseMenuIterator and DinerMenuIterator extend, right? Almost...actually, it’s even
easier than that. Not only does java.util have its own Iterator interface, but ArrayList has an
 iterator() method that returns an iterator. In other words, we never needed to implement our
own iterator for ArrayList. However, we’ll still need our implementation for the DinerMenu
because it relies on an Array, which doesn’t support the iterator() method.


     What if I don’t want to provide the ability to remove            How does remove() behave under multiple threads thatQ:                       Q:
something from the underlying collection of objects?           may be using different iterators over the same collection of
                                                                objects?
     The remove() method is considered optional. You don’t haveA: to provide remove functionality. But you should provide the method          The behavior of the remove() method is unspecified if the                          A:because it’s part of the Iterator interface. If you’re not going to            collection changes while you are iterating over it. So you should be
allow remove() in your iterator, you’ll want to throw the runtime           careful in designing your own multithreaded code when accessing a
exception java.lang.UnsupportedOperationException. The Iterator        collection concurrently.
API documentation specifies that this exception may be thrown
 from remove() and any client that is a good citizen will check for this
exception when calling the remove() method.


334      Chapter 9


---

## PDF page 373

the iterator and composite patterns

Cleaning things up with java.util.Iterator

Let’s start with the PancakeHouseMenu. Changing it over to
java.util.Iterator is going to be easy. We just delete the
PancakeHouseMenuIterator class, add an import java.util.Iterator
to the top of PancakeHouseMenu, and change one line of the
PancakeHouseMenu:

   public Iterator<MenuItem> createIterator() {
                                                                           Instead of creating our own iterator       return menuItems.iterator();                                                                         now, we just call the iterator()   }                                                               method on the menuItems ArrayList
                                                                     (more on this in a bit).
And that’s it, PancakeHouseMenu is done.
Now we need to make the changes to allow DinerMenu to work with java.util.Iterator.

                                                                             First we import java.util.Iterator, the
   import java.util.Iterator;                                       interface we’re going to implement.
   public class DinerMenuIterator implements Iterator<MenuItem> {
       MenuItem[] items;
       int position = 0;
       public DinerMenuIterator(MenuItem[] items) {
           this.items = items;
       }                                                          None of our current
                                                                     implementation changes...       public MenuItem next() {
           //implementation here
       }
                                                              Remember, the remove() method is optional       public boolean hasNext() {                                                                                      in the Iterator interface. Having our waitress           //implementation here                                                                 remove menu items really doesn’t make sense,       }                                                                          so we’ll just throw an exception if she tries.
       public void remove() {
           throw new UnsupportedOperationException
                       ("You shouldn't be trying to remove menu items.");
       }
   }


                                                                       you are here 4      335


---

## PDF page 374

reworking the waitress

We are almost there...

Now we just need to give the Menus a common interface and rework the
Waitress a little. The Menu interface is quite simple: we might want to add a
few more methods to it eventually, like addItem(), but for now we’ll let the chefs
control their menus by keeping that method out of the public interface:
                                                                    This is a simple interface that
  public interface Menu {                                          just lets clients get an iterator
      public Iterator<MenuItem> createIterator();       for the items in the menu.
  }
Now we need to add an implements Menu to both the PancakeHouseMenu
and the DinerMenu class definitions and update the Waitress class:

  import java.util.Iterator;                                   Now the Waitress uses the java.util.Iterator as well.
  public class Waitress {                                                                  We need to replace the      Menu pancakeHouseMenu;                                                                                  concrete Menu classes with      Menu dinerMenu;                                                                            the Menu interface.
      public Waitress(Menu pancakeHouseMenu, Menu dinerMenu) {
          this.pancakeHouseMenu = pancakeHouseMenu;
          this.dinerMenu = dinerMenu;
      }
      public void printMenu() {
          Iterator<MenuItem> pancakeIterator = pancakeHouseMenu.createIterator();
          Iterator<MenuItem> dinerIterator = dinerMenu.createIterator();
          System.out.println("MENU\n----\nBREAKFAST");
          printMenu(pancakeIterator);
          System.out.println("\nLUNCH");
          printMenu(dinerIterator);
      }
                                                                                             Nothing changes      private void printMenu(Iterator iterator) {                                                                                                           here.          while (iterator.hasNext()) {
              MenuItem menuItem = iterator.next();
              System.out.print(menuItem.getName() + ", ");
              System.out.print(menuItem.getPrice() + " -- ");
              System.out.println(menuItem.getDescription());
          }
      }
      // other methods here
  }


336      Chapter 9


---

## PDF page 375

the iterator and composite patterns

What does this get us?
The PancakeHouseMenu and DinerMenu classes implement an interface,              This solves the problem
Menu. This allows the Waitress to refer to each menu object using the interface        of the Waitress
rather than the concrete class. So, we’re reducing the dependency between               depending on the
the Waitress and the concrete classes by “programming to an interface, not an            concrete Menus.
implementation.”
Also, the new Menu interface has one method, createIterator(), that is
implemented by PancakeHouseMenu and DinerMenu. Each menu class
assumes the responsibility of creating a concrete Iterator that is appropriate for
its internal implementation of the menu items.

                                                                                from the                                                                                             Waitress                                                        Waitress                                           Now,                                                                          We’ve decoupled                                                                               the menus, so now                                                                     of                                                      to                                                     only needs                                                                             implementation      to iterate                                                                                         Iterator                                                                       an                                                   concerned                                             be                                                                                 use                                                                      can                                                         we                                                                                                without          Here’s               our new                   Menu                               interface.                                                                              menu items                                                                    of                                               Menus and                                                                                                         list                                               with                                                                        any                                                                         over                                                                                                                                  list of         It             specifies                                                                             how the                  the                     new method,                                                                                  about                                                                        know                                                      Iterators.                                                                    to                                                                               having         createIterator().                                                                                     implemented.                                                                           items is


                                  <<interface>>                              Waitress                              <<interface>>
                             Menu                                                                                        Iterator
                                                                                   printMenu()
                                       createIterator()createIterator()                                                                                hasNext()
                                                                                                                                                next()
                                                                                                                           remove()


          PancakeHouseMenu                    DinerMenu                                                                                     PancakeHouseMenuIterator          DinerMenuIterator
          menuItems                             menuItems
                                                                                                           hasNext()                            hasNext()
              createIterator()                                  createIterator()                                           next()                                    next()
                                                                                                       remove()                            remove()
             PancakeHouseMenu and DinerMenu now                                     DinerMenu returns             implement the Menu interface, which                                     a DinerMenuIterator
            means they need to implement the new                                    from its              createIterator() method.                          We’re now using the             createIterator()
                                                          ArrayList iterator           method because
                                                                      supplied by java.util. We         that’s the kind of
                                                               don’t need this anymore.        iterator required
                      Each concrete Menu is responsible                                 to iterate over its
                        for creating the appropriate                                    Array of menu items.
                         concrete Iterator class.


                                                                       you are here 4      337


---

## PDF page 376

iterator pattern defined

Iterator Pattern defined

You’ve already seen how to implement the Iterator
Pattern with your very own iterator. You’ve also seen
how Java supports iterators in some of its collectionoriented classes (ArrayList). Now it’s time to check out
the official definition of the pattern:
                                The Iterator Pattern
    The Iterator Pattern provides a way to                                          allows traversal of the
       access the elements of an aggregate object
       sequentially without exposing its underlying                                         elements of an aggregate
       representation.                            without exposing the
This makes a lot of sense: the pattern gives you a way          underlying implementation.
to step through the elements of an aggregate without
having to know how things are represented under the
covers. You’ve seen that with the two implementations                                              It also places the taskof Menus. But the effect of using iterators in your design
is just as important: once you have a uniform way of                                           of traversal on theaccessing the elements of all your aggregate objects, you
can write polymorphic code that works with any of these                                             iterator object, not
aggregates—just like the printMenu() method, which
doesn’t care if the menu items are held in an Array or                                      on the aggregate,
ArrayList (or anything else that can create an Iterator), as
long as it can get hold of an Iterator.                  which simplifies the
The other important impact on your design is that the                                         aggregate interface andIterator Pattern takes the responsibility of traversing
elements and gives that responsibility to the iterator                                         implementation, andobject, not the aggregate object. This not only keeps
the aggregate interface and implementation simpler,                                           places the responsibility
 it removes the responsibility for iteration from the
aggregate and keeps the aggregate focused on the                                   where it should be.
things it should be focused on (managing a collection of
objects), not on iteration.


338      Chapter 9


---

## PDF page 377

the iterator and composite patterns

The Iterator Pattern Structure

Let’s check out the class diagram to put all the pieces in context...

                                                                          The Iterator interface
Having a common interface for your                                                              provides the interface
aggregates is handy for your client;                                                      that all iterators
it decouples your client from the                                                         must implement, and
implementation of your collection of objects.                                            a set of methods
                                                                                        for traversing over
                          <<interface>>                                   Client                               <<interface>>                         Aggregate                                                                                     Iterator           elements of a collection.                                                                                        Here we’re using the                           createIterator()                                                                                hasNext()
                                                                                                                                    next()                     java.util.Iterator. If
                                                                                                                 remove()                you don’t want to
                                                                                                    use Java’s Iterator
                                                                                                      interface, you can
                                                                                                  always create your own.

                     ConcreteAggregate                                                                   ConcreteIterator
                            createIterator()                                                                                hasNext()
                                                                                                                                     next()
                                        Each                                 remove()
                                            ConcreteAggregate
                                                                 is responsible for
      The ConcreteAggregate                   instantiating a
       has a collection of                     ConcreteIterator that      The ConcreteIterator is
       objects and implements                 can iterate over its             responsible for managing
       the method that                          collection of objects.         the current position of       returns an Iterator for                                                                      the iteration.         its collection.


               The class diagram for the Iterator Pattern looks very similar to another
                   pattern you’ve studied; can you think of what it is? Hint: a subclass
                 decides which object to create.


                                                                       you are here 4      339


---

## PDF page 378

the single responsibility principle

The Single Responsibility Principle

What if we allowed our aggregates to implement their internal
collections and related operations AND the iteration methods?      Every responsibility of
Well, we already know that would expand the number ofmethods in the aggregate, but so what? Why is that so bad?        a class is an area of
Well, to see why, you first need to recognize that when we allow                                              potential change. More
a class to not only take care of its own business (managing
some kind of aggregate) but also take on more responsibilities                                      than one responsibility
(like iteration) then we’ve given the class two reasons to change.
Two? Yup, two: it can change if the collection changes in some      means more than one area
way, and it can change if the way we iterate changes. So once
again our friend CHANGE is at the center of another design        of change.
principle:
                                      This principle guides us to
                Design                           Principle
               A class should                               have only one            keep each class to a single
                    reason to change.                                                responsibility.


We know we want to avoid change in our classes because                                                               Cohesion is a term you’llmodifying code provides all sorts of opportunities for                                                                               hear used as a measure of
problems to creep in. Having two ways to change increases                                                                 how closely a class or a
the probability the class will change in the future, and when                                       Head First    module supports a single
it does, it’s going to affect two aspects of your design.                                                                                   OO Glue     purpose or responsibility.
The solution? The principle guides us to assign each
responsibility to one class, and only one class.                           We say that a module or
                                                                                 class has high cohesion when it
That’s right, it’s as easy as that, and then again it’s not:                                                                                                 is designed around a set of related
separating responsibility in design is one of the most                           functions, and we say it has low
difficult things to do. Our brains are just too good at seeing                 cohesion when it is designed around a
a set of behaviors and grouping them together even when                    set of unrelated functions.
there are actually two or more responsibilities. The only
way to succeed is to be diligent in examining your designs                                                                   Cohesion is a more general conceptand to watch out for signals that a class is changing in more                                                                        than the Single Responsibility Principle,
than one way as your system grows.                                                                            but the two are closely related.
                                                                     Classes that adhere to the principle
                                                                        tend to have high cohesion and are
                                                              more maintainable than classes that
                                                                           take on multiple responsibilities and
                                                                 have low cohesion.


340      Chapter 9


---

## PDF page 379

the iterator and composite patterns


                        Examine these classes and determine which ones
                         have multiple responsibilities.


                                                                                         GumballMachine
                                    Person
                                                                                                                   getCount()
      Game                   setName()                             Phone                      getState()
                                     setAddress()
login()                                                                                            dial()                                  getLocation()                                 setPhoneNumber()
signup()                                                               hangUp()                                      save()
move()                                                                                           talk()                                         load()
fire()                                                                      sendData()
rest()                                                                                       flash()


                                                                                                                             Iterator
        DeckOfCards
                                               ShoppingCart                             hasNext()
    hasNext()                                                                                                      next()
     next()                                             add()                                            remove()
    remove()                                       remove()
    addCard()                                       checkOut()
    removeCard()                                     saveForLater()
     shuffle()


                                           Hard hat area. watch out
                                              for falling assumptions

      2

                          Determine if these classes have low or high cohesion.


        Game                                                                   PlayerActions
   login()                                                                              move()                                 Player                                            GameSession
   signup()                                                                                                                   fire()                              getHighScore()
  move()                                                                   login()                                       rest()                           getName()
                                                           signup()
    fire()
   rest()
   getHighScore()
  getName()


                                                             you are here 4      341


---

## PDF page 380

no dumb questions


                                        hand them an operation and tell them to       I’ve seen other books show the                                                                                              If I’m using Java, won’t I alwaysQ:                                                  iterate, and they do all the work for you.   Q: Iterator class diagram with the methods                                           want to use the java.util.Iterator
 first(), next(), isDone(), and currentItem().                                                    interface so I can use my own iterator
                                            Could I implement an Iterator that     implementations with classes that areWhy are these methods different?    Q:
                                       can go backward as well as forward?        already using the Java iterators?
     Those are the “classic” method namesA: that have been used. These names have                Definitely. In that case, you’d probably          Probably. If you have a common                 A:               A:changed over time and we now have next(),    want to add two methods, one to get to the       Iterator interface, it will certainly make it
 hasNext(), and even remove() in                previous element, and one to tell you when      easier for you to mix and match your own
 java.util.Iterator.                                you’re at the beginning of the collection         aggregates with Java aggregates like
                                                     of elements. Java’s Collection Framework       ArrayList and Vector. But remember, if you
 Let’s look at the classic methods. The           provides another type of iterator interface      need to add functionality to your Iterator
 next() and currentItem() have been merged      called ListIterator. This iterator adds              interface for your aggregates, you can
 into one method in java.util. The isDone()        previous() and a few other methods to the      always extend the Iterator interface.
method has become hasNext(), but we         standard Iterator interface. It is supported
have no method corresponding to first().        by any Collection that implements the List               I’ve seen an Enumeration interface                                  Q:That’s because in Java we tend to just get        interface.                                        in                                                                                        Java; does that implement the Iterator
a new iterator whenever we need to start                                                  Pattern?
 the traversal over. Nevertheless, you can         Who defines the ordering of the                 Q:
see there is very little difference in these         iteration in a collection like Hashtable,                                                               We talked about this in the interfaces. In fact, there is a whole range      which is inherently unordered?     A:                                                                                       Adapter Pattern chapter (Chapter 7). of behaviors you can give your iterators.                                                                        Remember? The java.util.EnumerationThe remove() method is an example of an                                                            Iterators imply no ordering. The               is an older implementation of Iteratorextension in java.util.Iterator.       A:                                                underlying collections may be unordered as      that has since been replaced by java.util.
                                                         in a hash table or in a bag; they may even        Iterator. Enumeration has two methods,
        I’ve heard about “internal” iterators    contain duplicates. So ordering is related       hasMoreElements(), corresponding toQ:
and “external” iterators. What are they?       to both the properties of the underlying          hasNext(), and nextElement(), corresponding
Which kind did we implement in the           collection and to the implementation. In          to next(). However, you’ll probably want to
example?                                      general, you should make no assumptions      use Iterator over Enumeration as more Java
                                            about ordering unless the Collection            classes support it. If you need to convert
    We implemented an external iterator,     documentation indicates otherwise.            from one to another, review Chapter 7 againA:which means that the client controls the                                                where you implemented the adapter for
 iteration by calling next() to get the next            You said we can write                Enumeration and Iterator.                 Q:
element. An internal iterator is controlled      “polymorphic code” using an iterator; can
by the iterator itself. In that case, because     you explain that more?                                 Is using Java’s enhanced for loop                                  Q: it’s the iterator that’s stepping through the                                                     related to iterators?
elements, you have to tell the iterator what                                      When we write methods that take to do with those elements as it goes through A:                                                      Iterators as parameters, we are using             Good question! It is, and to tackle thatthem. That means you need a way to pass                   A:                                             polymorphic iteration. That means we are       question we need to understand anotheran operation to an iterator. Internal iterators                                                 creating code that can iterate over any          interface—that is, Java’s Iterable interface.are less flexible than external iterators                                                    collection as long as it supports Iterator.        This is a good time to do just that...because the client doesn’t have control of                              We don’t care about how the collection
 the iteration. However, some might argue                                                             is implemented, we can still write code to
 that they are easier to use because you just                                                       iterate over it.


342      Chapter 9


---

## PDF page 381

the iterator and composite patterns

Meet Java’s Iterable interface

You’re already up to speed on Java’s Iterator interface, but there’s
another interface you need to meet: Iterable. The Iterable interface
is implemented by every Collection type in Java. Guess what? In your
code using the ArrayList, you’ve already been using this interface.
Let’s take a look at the Iterable interface:
               Here’s the Iterable
               interface.


                           <<interface>>                                                                    <<interface>>
                                                                                                                                Iterator                                 Iterable               The Iterable interface
                               iterator()                            includes an iterator()            next()
                                                                                                                     hasNext()                    + forEach()                    method that returns
                    + spliterator()                                                                  + remove()                                        an iterator that
                                            implements the
                                             Iterator interface.
                           <<interface>>                             Collection                                        You already know about the
                         add()                                                      Iterator interface; that's the
                           addAll()                                                same interface we’ve been using
                             clear()                                                  with our Diner and Pancake
                           contains()                                                                         house iterators.                            containsAll()                   All Collection classes, like
                          equals()                   ArrayList, implement the
                       hashCode()                  Collection interface, which
                         isEmpty()                                            inherits from the Iterable
                               iterator()                                          interface, so all Collection                        remove()                         removeAll()                    classes are Iterables.
                              retainAll()
                             size()
                           toArray()

If a class implements Iterable, we know that the class implements an         The Iterable interface also
iterator() method. That method returns an iterator that implements              includes the spliterator()
the Iterator interface. This interface also includes a default forEach()           method, which provides even
method that can be used as another way to iterate through the                more advanced ways to iterate
collection. In addition to all that, Java even provides some nice                 through a collection.
syntactic sugar for iteration, with its enhanced for loop. Let’s see how
that works.


                                                                       you are here 4      343


---

## PDF page 382

the enhanced for loop

Java’s enhanced for loop

Let’s take an object whose class implements the Iterable interface...why not
the ArrayList collection we used for the Pancake House menu items:
    List<MenuItem> menuItems = new ArrayList<MenuItem>();

We can iterate over ArrayList the way we have been:
    Iterator iterator = menu.iterator();                                                                                 This is the way we've been     while (iterator.hasNext()) {                                                                                     doing iteration over our           MenuItem menuItem = iterator.next();                                                                                                   collections, using an iterator           System.out.print(menuItem.getName() + ", ");                                                                                         along with the hasNext() and           System.out.print(menuItem.getPrice() + " -- ");                                                                                    next() methods.           System.out.println(menuItem.getDescription());
    }

Or, given we know ArrayList is an Iterable, we could use Java’s enhanced
for shorthand:
     for (MenuItem item: menu) {                                       Here we can dispense with
           System.out.print(menuItem.getName() + ", ");           the explicit iterator as the
           System.out.print(menuItem.getPrice() + " -- ");        hasNext() and next() methods.           System.out.println(menuItem.getDescription());
    }


                                                Looks like a great way to use Iterators
                                               that really results in simple code—no more
                                            hasNext() or next() method calls. So, can we
                                          rework our Waitress code to use Iterable and
                                            the enhanced for loop for both menus?


344      Chapter 9


---

## PDF page 383

the iterator and composite patterns

Not so fast; Arrays are not Iterables

We have some bad news: the Diner may not have made the best decision using an
Array as the basis for its menus. As it turns out, Arrays are not Java Collections
and so they don’t implement the Iterable interface. Given that, we can’t as easily
consolidate our Waitress code into one method that takes an Iterable and use it
with both the Pancake House’s breakfastItems and the Diner’s lunchItems. If you
try to change the Waitress’s printMenu() method to take an Iterable instead of an
Iterator, and use the for-each loop instead of the Iterator API, like this:
   public void printMenu(Iterable<MenuItem> iterable) {
         for (MenuItem menuItem : iterable) {
                // print menuItem                                                 This will only work for the
         }                                    ArrayList we’re using for the  }                                            Pancake House menu.

you’ll get a compiler error when you try to pass the lunchItems array to printMenu():
   printMenu(lunchItems);         Compile error! Arrays are not Iterables.
because, again, Arrays don’t implement the Iterable interface.
If you keep both loops in the Waitress code, we’re back to square one: the Waitress is
once again dependent on the aggregate types we’re using to store the menus, and she
has duplicate code: one loop for the ArrayList, and one loop for the Array.
So what do we do? Well, there are many ways to solve this issue, but they are a bit of a
sideshow, as would be refactoring our code. After all, this chapter is about the Iterator
Pattern, not Java’s Iterable interface. But the good news is you know about Iterable, you
know its relationship to Java’s Iterator interface and to the Iterator Pattern. So, let’s keep
moving, as we’ve got a great implementation even if we aren’t taking advantage of a
little syntactic sugar from Java’s for loop.


            You probably noticed the forEach() method in the Iterable menu. It’s used as the basis for
                  Java’s enhanced for loop, but you can also use it directly with Iterables. Here’s how it works:
            Iterable, in this case                                             ...and                                                                                passing a lambda that takes a  Here’s an             House ArrayList          We’re calling forEach()...     menuItem, and just prints it.  our Pancake
  of menu items.             breakfastItems.forEach(item -> System.out.println(item));
                                                                          So this code will print every
                                                                                  item in the collection.


                                                                       you are here 4      345


---

## PDF page 384

a new acquisition


                             Good thing you’re
                            learning about the Iterator
                         Pattern because I just heard that
                        Objectville Mergers and Acquisitions
                      has done another deal...we’re merging
                       with Objectville Café and adopting their
                           dinner menu.


                    Wow, and we thought things
                        were already complicated.
                   Now what are we going to do?
                                                       Come on, think positively.
                                                                   I’m sure we can find a way to
                                                            work them into the Iterator
                                                                        Pattern.


346      Chapter 9


---

## PDF page 385

the iterator and composite patterns

Taking a look at the Café Menu

Here’s the café menu. It doesn’t look like too much trouble to integrate the
CafeMenu class into our framework...let’s check it out.
                                                     our new Menu                                                implement                                          doesn’t                           CafeMenu                                                                                    storing their menu items in a HashMap.                                   interface, but this is easily fixed. The café is                                                         Does that support Iterator? We’ll see shortly... public class CafeMenu {
     Map<String, MenuItem> menuItems = new HashMap<String, MenuItem>();
                                                                   Like the other Menus, the menu items     public CafeMenu() {                                                                     are initialized in the constructor.         addItem("Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            true, 3.99);
         addItem("Soup of the day",
            "A cup of the soup of the day, with a side salad",
            false, 3.69);
         addItem("Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            true, 4.29);
    }                                                                         Here’s where we create a new MenuItem                                                                 and add it to the menuItems HashMap.     public void addItem(String name, String description,
                         boolean vegetarian, double price)
    {
         MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
         menuItems.put(name, menuItem);
                                                            menuItem object.    }                   The key is the itemThename.value is the
     public Map<String, MenuItem> getMenuItems() {
        return menuItems;
    }                                               We’re not going to need this anymore.}


                                             Before looking at the next page, quickly jot down the three
                                              things we have to do to this code to fit it into our framework:

        1.

     2.

      3.


                                                                       you are here 4      347


---

## PDF page 386

reworking the menu code

Reworking the Café Menu code

Let’s rework the CafeMenu code. We’re going to take care of implementing the
Menu interface, and we also need to deal with creating an Iterator for the values
stored in the HashMap. Things are a little different than when we did the same
for the ArrayList; check it out...
                                                 CafeMenu implements the Menu interface, so the
                                                            Waitress can use it just like the other two Menus.
  public class CafeMenu implements Menu {
     Map<String, MenuItem> menuItems = new HashMap<String, MenuItem>();
                                                                         We’re using HashMap because it’s a common     public CafeMenu() {                                                                 data structure for storing values.         // constructor code here
     }
     public void addItem(String name, String description,
                          boolean vegetarian, double price)
     {
         MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
         menuItems.put(name, menuItem);
     }                                                                   Just like before, we can get rid of getItems()     public Map<String, MenuItem> getMenuItems() {       so we don’t expose the implementation of
         return menuItems;                                    menuItems to the Waitress.
     }
                                                       And here’s where we implement the     public Iterator<MenuItem> createIterator() {                                                                       createIterator() method. Notice that         return menuItems.values().iterator();                                                                        we’re not getting an Iterator for the     }                                                                    whole HashMap, just for the values. }
      Code Up Close
                              HashMap is a little more complex than ArrayList because it supports both
                                    keys and values, but we can still get an Iterator for the values (which are
                                        the MenuItems).

    public Iterator<MenuItem> createIterator() {
        return menuItems.values().iterator();                                                                                                 violating                                                                  Are we
    }                                                                   the Principle of                                                                        Knowledge                                                                         Least                                                                  What can      First we get the values of the              Luckily that collection supports the        here?                                                                              about it?     HashMap, which is just a collection of       iterator() method, which returns a       we do        all the objects in the HashMap.            object of type java.util.Iterator.


348      Chapter 9


---

## PDF page 387

the iterator and composite patterns

Adding the Cafe‘ Menu to the Waitress

Now it’s time to modify the Waitress to support our new Menu. Now that the
Waitress expects Iterators, it should be straightforward:
  public class Waitress {             The café menu is passed into the Waitress                                                          in the constructor with the other menus,     Menu pancakeHouseMenu;                                          and we stash it in an instance variable.     Menu dinerMenu;
     Menu cafeMenu;

     public Waitress(Menu pancakeHouseMenu, Menu dinerMenu, Menu cafeMenu) {
         this.pancakeHouseMenu = pancakeHouseMenu;
         this.dinerMenu = dinerMenu;
         this.cafeMenu = cafeMenu;
     }

     public void printMenu() {
         Iterator<MenuItem> pancakeIterator = pancakeHouseMenu.createIterator();
         Iterator<MenuItem> dinerIterator = dinerMenu.createIterator();
         Iterator<MenuItem> cafeIterator = cafeMenu.createIterator();
                                                                                           We’re using the café’s
         System.out.println("MENU\n----\nBREAKFAST");                   menu for our dinner
                                                                                          menu. All we have to do         printMenu(pancakeIterator);                                                                                     to print it is create the         System.out.println("\nLUNCH");                                                                                                  iterator, and pass it to
         printMenu(dinerIterator);                                              printMenu(). That’s it!
         System.out.println("\nDINNER");
         printMenu(cafeIterator);
     }

     private void printMenu(Iterator iterator) {
         while (iterator.hasNext()) {
                                                                                      Nothing changes here.             MenuItem menuItem = iterator.next();
             System.out.print(menuItem.getName() + ", ");
             System.out.print(menuItem.getPrice() + " -- ");
             System.out.println(menuItem.getDescription());
         }
     }
 }

                                                                       you are here 4      349


---

## PDF page 388

testing the new menu

Breakfast, lunch, AND dinner

Let’s update our test drive to make sure this all works.
  public class MenuTestDrive {
     public static void main(String args[]) {
         PancakeHouseMenu pancakeHouseMenu = new PancakeHouseMenu();     Create a CafeMenu...
         DinerMenu dinerMenu = new DinerMenu();
         CafeMenu cafeMenu = new CafeMenu();                                                                                                        ...and pass it to the waitress.
         Waitress waitress = new Waitress(pancakeHouseMenu, dinerMenu, cafeMenu);
         waitress.printMenu();        Now, when we print we should see all three menus. }

Here’s the test run; check out the new dinner menu from the Café!


   File Edit  Window Help
 % java DinerMenuTestDrive                                                          First we iterate
                                                                                      through the MENU                                                                                       pancake menu... ----
 BREAKFAST
 K&B's Pancake Breakfast, 2.99 -- Pancakes with scrambled eggs and toast
 Regular Pancake Breakfast, 2.99 -- Pancakes with fried eggs, sausage
 Blueberry Pancakes, 3.49 -- Pancakes made with fresh blueberries                                                                                                                                ...and then
 Waffles, 3.59 -- Waffles with your choice of blueberries or strawberries      the diner
                                                                                                                          menu...
 LUNCH
 Vegetarian BLT, 2.99 -- (Fakin') Bacon with lettuce & tomato on whole wheat
 BLT, 2.99 -- Bacon with lettuce & tomato on whole wheat
 Soup of the day, 3.29 -- Soup of the day, with a side of potato salad
 Hot Dog, 3.05 -- A hot dog, with sauerkraut, relish, onions, topped with cheese
 Steamed Veggies and Brown Rice, 3.99 -- Steamed vegetables over brown rice
 Pasta, 3.89 -- Spaghetti with marinara sauce, and a slice of sourdough bread
                                                                                                                            ...and finally
 DINNER                                                                                     the new café
 Soup of the day, 3.69 -- A cup of the soup of the day, with a side salad    menu, all with
 Burrito, 4.29 -- A large burrito, with whole pinto beans, salsa, guacamole the same
 Veggie Burger and Air Fries, 3.99 -- Veggie burger on a whole wheat bun,      iteration code.
  lettuce, tomato, and fries
 %

350      Chapter 9


---

## PDF page 389

the iterator and composite patterns

What did we do?                                         ArrayList

                      We wanted to give the
                             Waitress an easy way to                      MenuItem MenuItem MenuItem  MenuItem
                                                                                                                                       1       2       3        4                            iterate over menu items...                                          Our menu items had two                                                                implementations                                                    different                                                            different            Array                                            and two                                                        for iterating.                                                       interfaces
                                  ...and we didn’t want her to                                                          1 MenuItem
                         know about how the menu
                                                                                                          2                            items are implemented.                             MenuItem

                                                                                                          3
                                                             MenuItem

                                                                                                          4
                                                                  MenuItem
We decoupled the Waitress....
                                                                ArrayList has a                                                                                           iterator...           So we gave the Waitress an                                  built-in                                                              ArrayList             Iterator for each kind of
            group of objects she needed
            to iterate over...                 ...one for
                                              ArrayList...
                                                       MenuItem MenuItem MenuItem  MenuItem
                                                                                                                                       1       2       3        4

                      next()
                                                                                   ...Array
                 Iterator                           doesn’t have    Array
                                                                 a built-in
                                                          ...and one for Array.             Iterator so           1
                                                                MenuItem                           next()                                 we built our
                                                                          own.
                                                                                                           2
                                                               MenuItem
                  Iterator                                                 3
                                                             MenuItem
                       Now she doesn’t have to worry about which
                                                                                                           4
                              implementation we used; she always uses the same             MenuItem                                interface — Iterator — to iterate over menu items.
                                 She’s been decoupled from the implementation.

                                                                       you are here 4      351


---

## PDF page 390

a more extensible waitress

...and we made the Waitress more extensible
                                                                    We easily added another                 By giving her an Iterator,                                               of menu                                                                                           implementation                  we have decoupled her                                                                                                  items, and since we                   from the implementation                                                                                         provided an Iterator,                   of the menu items, so we                                                                               the Waitress knew what                     can easily add new Menus                                          HashMap   to do.                        if we want.

                         next()                                                                                                 key   MenuItem


                                                                                                                                                                         key   MenuItem
                r
                     Iterato                 Which                              is                         better                               for                                        her,                                                                                                                                                                         key   MenuItem                                                                                     Making                                                                                          an                   because                                                                                                           Iterator                     now                             she can                                     use                                   the                                                                                       for                                                                                       the                 same                                                                                       HashMap                     code                        to                                                                                                            values was easy;                                iterate over                                                                         key   MenuItem                 any group of                                  objects.                             And                                             when you call                      it’s better for                               us                                   because                                                                                                            values.iterator()               the implementation                                       details                                                 you                  aren’t                                                                                        get an Iterator.                        exposed.

But there’s more!
       Java gives you a lot of “Collection”
         classes that allow you to store
       and retrieve groups of objects;
       for example, Vector and
        LinkedList.                                                  LinkedList

                                  Vector          Most have different
                                                    MenuItem MenuItem MenuItem  MenuItem             interfaces.

         But almost all of        Menu1Item Menu2Item Menu3Item  Menu4Item
          them support a          way to obtain an                                            ...and more!
              Iterator.
                               And if they don’t support
                                         Iterator, that’s okay, because now
                                     you know how to build your own.

352      Chapter 9


---

## PDF page 391

the iterator and composite patterns

Iterators and Collections

We’ve been using a couple of classes that are part of the Java Collections Framework.
This “framework” is just a set of classes and interfaces, including ArrayList, which
we’ve been using, and many others like Vector, LinkedList, Stack, and PriorityQueue.
Each of these classes implements the java.util.Collection interface, which contains a
bunch of useful methods for manipulating groups of objects.
Let’s take a quick look at the interface:

       <<interface>>                Don’t forget the
           Iterable                                  Collection interface
   iterator()                               implements the  + forEach()                                              HashMap is one of                                 Iterable interface.  + spliterator()                                                 a few classes that
                                                                      indirectly                                                      kinds                                                               all                                             there’s                                            see,                               can                            you                      As                                                             supports Iterator.                                            add                                              can                                         You                                            here.                                  stuff                           good                      of
      <<interface>>                                                              As you saw when we                        and remove elements from your        Collection                                                           implemented the CafeMenu, you                                collection without even knowing  add()                                    implemented.                      could get an Iterator from it, but  addAll()                   how it’s                                                                   only by first retrieving its Collection
  clear()                                                                   called values. If you think about it,  contains()                                 Here’s our old friend, the                     this makes sense: the HashMap  containsAll()  equals()                           iterator() method. With this               holds two sets of objects: keys and
 hashCode()                      method, you can get an Iterator            values. If we want to iterate over
  isEmpty()                       for any class that implements                    its values, we first need to retrieve
  iterator()                       the Collection interface.                them from the HashMap, and then
 remove()                                                               obtain the iterator.  removeAll()
  retainAll()
  size()                     Other handy methods include
  toArray()                           size(), to get the number of
                              elements, and toArray() to turn                           your collection into an array.
                                                  The nice thing about Collections and
                                                         Iterators is that each Collection object
                                                    knows how to create its own Iterator. Calling
                                                                iterator() on an ArrayList returns a concrete
                                                      Iterator made for ArrayLists, but you never need
                                                       to see or worry about the concrete class it uses;
                                                        you just use the Iterator interface.


                                                                       you are here 4      353


---

## PDF page 392

code magnets

      Code Magnets
             The Chefs have decided that they want to be able to alternate their lunch menu items; in other words,
               they will offer some items on Monday, Wednesday, Friday, and Sunday, and other items on Tuesday,
               Thursday, and Saturday. Someone already wrote the code for a new “Alternating” DinerMenu Iterator so
                that it alternates the menu items, but she scrambled it up and put it on the fridge in the Diner as a joke.
            Can you put it back together? Some of the curly braces fell on the floor and they were too small to pick
               up, so feel free to add as many of those as you need.

     MenuItem menuItem = items[position];
     position = position + 2;
     return menuItem;

    import java.util.Iterator;
    import java.util.Calendar;
    public Object next() {   }
    public AlternatingDinerMenuIterator(MenuItem[] items)

       this.items = items;
       position = Calendar.DAY_OF_WEEK % 2;

   implements Iterator<MenuItem>  public void remove() {
   MenuItem[] items;
   int position;                            public class AlternatingDinerMenuIterator                   }
  public boolean hasNext() {
          throw new UnsupportedOperationException(
              "Alternating Diner Menu Iterator does not support remove()");
  if (position >= items.length || items[position] == null) {
      return false;
  } else {
      return true;                                              }
  }

354      Chapter 9


---

## PDF page 393

the iterator and composite patterns

                                    Is the Waitress ready for prime time?

                                         The Waitress has come a long way, but you’ve gotta admit
                                                       those three calls to printMenu() are looking kind of ugly.
                                                             Let’s be real—every time we add a new menu we’re going to
                                                  have to open up the Waitress implementation and add more
                                                       code. Can you say “violating the Open Closed Principle”?

                                                                          Three createIterator() calls.

             public void printMenu() {
                 Iterator<MenuItem> pancakeIterator = pancakeHouseMenu.createIterator();
                 Iterator<MenuItem> dinerIterator = dinerMenu.createIterator();
                 Iterator<MenuItem> cafeIterator = cafeMenu.createIterator();

                 System.out.println("MENU\n----\nBREAKFAST");
                 printMenu(pancakeIterator);
                                                                        Three calls to                 System.out.println("\nLUNCH");                                                                                  printMenu.                 printMenu(dinerIterator);

                 System.out.println("\nDINNER");
                 printMenu(cafeIterator);
             }                                            Every time we add or remove a menu , we’re going
                                             to have to open this code up for changes.

It’s not the Waitress’s fault. We’ve done a great job of decoupling the menu implementation
and extracting the iteration into an iterator. But we still are handling the menus with
separate, independent objects—we need a way to manage them together.


     The Waitress still needs to make three calls to printMenu(), one for each menu. Can you
       think of a way to combine the menus so that only one call needs to be made? Or perhaps
      so that one Iterator is passed to the Waitress to iterate over all the menus?


                                                                       you are here 4      355


---

## PDF page 394

a new design


                                    This isn’t so bad. All
                        we need to do is package the
                         menus up into an ArrayList and then
                             iterate through each Menu. The code in
                         the Waitress is going to be simple and it
                                    will handle any number of menus.


Sounds like the chef is on to something. Let’s give it a try:
    public class Waitress {                                             Now we just take a list        List<Menu> menus;                                                    of menus, instead of
                                                          each menu separately.        public Waitress(List<Menu> menus) {
           this.menus = menus;
        }
                                                                      And we iterate through the
        public void printMenu() {                                              menus, passing each menu’s
           Iterator<Menu> menuIterator = menus.iterator();             iterator to the overloaded
           while(menuIterator.hasNext()) {                                printMenu() method.
                  Menu menu = menuIterator.next();
                  printMenu(menu.createIterator());
           }
        }
        void printMenu(Iterator<MenuItem> iterator) {
           while (iterator.hasNext()) {                            No code
                  MenuItem menuItem = iterator.next();                    changes here.
                  System.out.print(menuItem.getName() + ", ");
                  System.out.print(menuItem.getPrice() + " -- ");
                  System.out.println(menuItem.getDescription());
           }
        }
    }

This looks pretty good, although we’ve lost the names of the menus,
but we could add the names to each menu.

356      Chapter 9


---

## PDF page 395

the iterator and composite patterns

Just when we thought it was safe...
                                                                 I just heard the Diner is
Now they want to add a dessert submenu.                                   going to be creating a dessert
                                                           menu that is going to be an insert
Okay, now what? Now we have to support not only multiple                                                                              into their regular menu.
menus, but menus within menus.
It would be nice if we could just make the dessert menu an
element of the DinerMenu collection, but that won’t work as it is
now implemented.
What we want (something like this):


                             All Menus


                u
              Men               e                  DinerMenu CafeMenu                     Here’s our ArrayList            PancakeHous
                                   1       2       3                    that holds the menus
                                                                  of each restaurant.


                                                    Café Menu     Pancake Menu
                              Diner Menu                                                              key   MenuItem
                                              Array
   MenuItem MenuItem MenuItem  MenuItem                                1                                                                                                                                                                                                                              key   MenuItem
          1       2       3        4                 MenuItem

                                                            2                                                                                               key   MenuItem                                    MenuItem                                  HashMap

                                                                                                                                                                                                                              key   MenuItem                                                            3  ArrayList    Dessert Menu                                   MenuItem

                                                            4
                                        1
                   MenuItem               MenuItem

                              2
                   MenuItem                      We need for Diner Menu to hold a submenu,
                              3                              but we can’t actually assign a menu to a
                  MenuItem                       MenuItem array because the types are
                              4                                  different, so this isn’t going to work.
                    MenuItem

       won’t         We can’t assign a dessert menu to a    this But                   MenuItem array. work!                       Time for a change!


                                                                       you are here 4      357


---

## PDF page 396

time to refactor

What do we need?

The time has come to make an executive decision to
rework the chef’s implementation into something that
is general enough to work over all the menus (and now
submenus). That’s right, we’re going to tell the chefs that
the time has come for us to reimplement their menus.
The reality is that we’ve reached a level of complexity
such that if we don’t rework the design now, we’re never
going to have a design that can accommodate further
acquisitions or submenus.
So, what is it we really need out of our new design?
  •   We need some kind of a tree-shaped structure that
      will accommodate menus, submenus, and menu
      items.
  •   We need to make sure we maintain a way to traverse
     the items in each menu that is at least as convenient
     as what we’re doing now with iterators.
  •   We may need to traverse the items in a more flexible
     manner. For instance, we might need to iterate over
     only the Diner’s dessert menu, or we might need to                                                                  There comes a time when we
      iterate over the Diner’s entire menu, including the                                                                 must refactor our code in order
      dessert submenu.                                                                         for it to grow. To not do so would
                                                                             leave us with rigid, inflexible code
                                                                        that has no hope of ever sprouting
                                                                       new life.


358      Chapter 9


---

## PDF page 397

the iterator and composite patterns
                   representBecause we need to                   and menu              submenus,menus, nested                     fit them               naturally items, we can                         s               structure. in a tree-like               AllMenu

              We need to
                    enu      M  accommodate
       e                                  inerMenu   PancakeHous                     Menus...       D                                                                          ...and submenus...  CaféMenu


                            u       MenuItem  MenuItem  MenuItem                            en MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertM

                                                                                                 ...and menu items.
                                  MenuItem  MenuItem  MenuItem                            MenuItem
  We still need to be able                  all the items      traverse  to                                                 We also need                                                                  to be able to          tree.                                                                     traverse    in the                                                                  more                                                                                                flexibly, for                                                                         instance over one                                                                                 menu.                                          AllMenus


                                              nu                     PancakeHouseMenu            DinerMe                                                             CafeMenu                  DessertMenu

                          MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertMenu       MenuItem  MenuItem  MenuItem

                                                               MenuItem   MenuItem  MenuItem  MenuItem
                                                     MenuItem   MenuItem  MenuItem  MenuItem


     How would you handle this new wrinkle to our design
       requirements? Think about it before turning the page.


                                                                       you are here 4      359


---

## PDF page 398

composite pattern defined

The Composite Pattern defined

That’s right; we’re going to introduce another pattern
to solve this problem. We didn’t give up on Iterator—it                                    Here’s a tree                                                                                                          structure.will still be part of our solution—however, the problem
of managing menus has taken on a new dimension that         Elements with
Iterator doesn’t solve. So, we’re going to step back and            child elements
solve it with the Composite Pattern.                           are called nodes.
We’re not going to beat around the bush on this
pattern; we’re going to go ahead and roll out the official                                                  Node
definition now:


                                                                Leaf                                      Leaf    The Composite Pattern allows you to
     compose objects into tree structures to                                       Leaf
     represent part-whole hierarchies. Composite
       lets           clients treat                      individual                                 objects and                                                                             Elements without children     compositions                    of                       objects uniformly.                                                                               are called leaves.

Let’s think about this in terms of our menus: this pattern
gives us a way to create a tree structure that can handle
a nested group of menus and menu items in the same
structure. By putting menus and items in the same
structure we create a part-whole hierarchy—that is, a
tree of objects that is made of parts (menus and menu
items) but that can be treated as a whole, like one big
über menu.                                       We can represent
                                                           our Menu and
Once we have our über menu, we can use this                  MenuItems in a
pattern to treat “individual objects and compositions             tree structure.uniformly.” What does that mean? It means if we have
a tree structure of menus, submenus, and perhaps                      Menu
subsubmenus along with menu items, then any menu
is a “composition” because it can contain both other
menus and menu items. The individual objects are just
the menu items—they don’t hold other objects. As you’ll                                                                            enuItem                                  MenuItem               M
see, using a design that follows the Composite Pattern                                       MenuItemis going to allow us to write some simple code that can
apply the same operation (like printing!) over the entire
menu structure.                                                            Menus are nodes and                                                                                          are leaves.                                                                             MenuItems


360      Chapter 9


---

## PDF page 399

the iterator and composite patterns

                         arbitrarily      We can create
        complex trees.
                            AllMenus              Menus

                                  Submenu                                  enu
                          DinerMenu        PancakeHouseM                                               CafeMenu
                                 The Composite Pattern        MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertMenu       MenuItem  MenuItem  MenuItem
   MenuItems                                    allows us to build
                                   MenuItem   MenuItem  MenuItem  MenuItem
                                              structures of objects in
                                          the form of trees that
      And treat them as a whole...                       contain both compositions
                                             of objects and individual                          AllMenus              Menus
                                               objects as nodes.
                                Submenu                               enu
                        DinerMenu       PancakeHouseM                                             CafeMenu
                                        Using a composite
      MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertMenu       MenuItem  MenuItem  MenuItem
                                                structure, we can apply
 MenuItems                     MenuItem   MenuItem  MenuItem  MenuItem                                          the same operations over
                                                    ....or as parts.             both composites and
                                             individual objects. In
         can be            print()                       other words, in mostOperations                whole...      to theapplied                                         cases we can ignore the
                            AllMenus              Menus                                            differences between
                                  Submenu                                  enu
                          DinerMenu        PancakeHouseM                                               CafeMenu            compositions of objects
                                    and individual objects.
        MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertMenu       MenuItem  MenuItem  MenuItem
   MenuItems                                                                     parts.                                   MenuItem   MenuItem  MenuItem  MenuItem               the                                                           print()     ...or

                                                                      you are here 4      361


---

## PDF page 400

composite pattern class diagram

                                                    defines an                                    Component                            The                                                                 in the     The                                                               all objects                                                                    Component                                          for                                                                      may                                      interface                                                                                          implement                                               the composite                                                       a default The Client uses the                                           both                                                                                    behavior                                                                                  for                   to                                                                                                 add(),                                         composition:             interface  Component                                                                             remove(), getChild() and its                 objects in          and leaves.           the   manipulate                                                                  operations.
  the composition.


                                 Client                                 Component

                                                                                         operation()
                                                                         add(Component)
  Note that the leaf also                                   remove(Component)getChild(int)
   inherits methods like add(),   remove(), and                 getChild(),  which don’t                necessarily make a  lot of sense for a leaf node.  We’re going to come back to                         Leaf                      Composite  this issue.
                                                                       operation()                        add(Component)
                                                                                                          also          A leaf has no                                               remove(Component)getChild(int)                                                               The Composite                                                                             Leaf-                                                                                                               operation()                                                                                the                   children.                                                                                        implements                                                                                                         operations.                                                                                        related      of                                                                                     some                                                                               that                                                                      Note                                                                                   make                A leaf defines the behavior for                                                                       may not                                                                                   these                                                                                                    Composite,                      the elements in the composition.                                 on a                                                                                           sense                                                                                                              is to                         It does this                                                                                  role                                by                                                                                              case an                                       implementing                                                                  Composite’s                                               the    The                                                                                that                                                                            so in                                                                                 be                                                                       the                         operations                               the                                                                                         might                                     Composite                                                                     behavior of                                                    supports.                                                            define                                                                                          exception                                                          components having children and     generated.                                                       to store child components.


     Component, Composite, Trees? I’m confused.                How does this relate to iterators?Q:                       Q:

    A composite contains components. Components come in             Remember, we’re taking a new approach. We’re going toA:                        A:two flavors: composites and leaf elements. Sound recursive? It is.       re-implement the menus with a new solution: the Composite Pattern.
A composite holds a set of children; those children may be other       So don’t look for some magical transformation from an iterator to a
composites or leaf elements.                                         composite. That said, the two work very nicely together. You’ll soon
                                                              see that we can use iterators in a couple of ways in the composite
When you organize data in this way you end up with a tree structure     implementation.
(actually an upside-down tree structure) with a composite at the root
and branches of composites growing up to leaves.

362      Chapter 9


---

## PDF page 401

the iterator and composite patterns

Designing Menus with Composite

So, how do we apply the Composite Pattern to our menus? To start with, we need to create a
component interface; this acts as the common interface for both menus and menu items and allows
us to treat them uniformly. In other words, we can call the same method on menus or menu items.
Now, it may not make sense to call some of the methods on a menu item or a menu, but we can deal
with that, and we will in just a moment. But for now, let’s take a look at a sketch of how the menus
are going to fit into a Composite Pattern structure:

                                                     MenuComponent represents the interface
                 to use the                            for both MenuItem and Menu. We’ve used an               is going                     to access                         abstract class here because we want to provide The Waitress    interface  MenuComponent           and MenuItems.                                default implementations for these methods.  both Menus


                         Waitress                              MenuComponent

                                                                       getName()
                                                                                     getDescription()                          We have some of the same
                                                                                      getPrice()                                 methods you’ll remember
                                                                                     isVegetarian()                                                                            from our previous versions
                                                                                                    print()                                of MenuItem and Menu,
                                                                   add(MenuComponent)                                                                   remove(MenuComponent)                        and we’ve added print(),                                                                                          getChild(int)                                     add(), remove() and       Here are the methods for                                                                                                  getChild(). We’ll describe        manipulating the components.                                                                                         these soon, when we      The components are                                                                                        implement our new Menu       MenuItem and Menu.                                                                               and MenuItem classes.
   Both MenuItem and                    getName()MenuItem                   menuComponentsMenu
  Menu override print().                    getDescription()                        getName()
                                                                getPrice()                                   getDescription()
                                                               isVegetarian()                                    print()
                                                                          print()                               add(MenuComponent)
                                                                                     remove(MenuComponent)
                                                                                                                  getChild(int)
        MenuItem                                                                                        that                                                                                 methods                    overrides                                                                             the                         the                                                                                  overrides                             methods                                                                                   also                                    that                                       make              Menu           sense,                                                                                              remove             and                                                                                   and                     uses                                                                           add                     the                                                                              to                                                                       way                                                                  a                           default                                                                                                 like                                                                                     sense,                                                          make                                    implementations          in                                                                                                                    its                                                                                from          MenuComponent                                                                                            menus!)                         for                                                                             other                              those                                                                              (or                                                                         items                                that                                                            menu                                         don’t        make                                                                                            the                                                                                                        use               sense                                                                                                                       we’ll                        (like                                                                                              addition,                                                                                           In                          add() — it                                   doesn’t                                                                 menuComponents.                                   make                                                                                               to         sense            to                                                                                         methods              add                                                                                      getDescription()                a component                                                                    and                              to                            a                                                               getName()                                        MenuItem...       we                                                                                                         menu.           can                                                                                           the                                                                                 of                only                add                                                                                               description                                                                         and                       components                                                                    name                              to                                                                   the                             a                                                                   return                                     Menu).

                                                                       you are here 4      363


---

## PDF page 402

implementing composite menus

Implementing MenuComponent                All components must implement
                                                   the MenuComponent interface;
Okay, we’re going to start with the MenuComponent abstract         however, because leaves and
class; remember, the role of the menu component is to provide an     nodes have different roles we
interface for the leaves and the composite nodes. Now you might       can’t always define a default
be asking, “Isn’t MenuComponent playing two roles?” It might        implementation for each
well be and we’ll come back to that point. However, for now we’re     method that makes sense.
going to provide a default implementation of the methods so that     Sometimes the best you can do
 if the MenuItem (the leaf) or the Menu (the composite) doesn’t          is throw a runtime exception.
want to implement some of the methods (like getChild() for a leaf
node), it can fall back on some basic behavior:

                    MenuComponent
                        provides default                                  Because some of these methods
                        implementations for                                    only make sense for MenuItems, and
                       every method.                                   some only make sense for Menus,                                                                     the default implementation is
                                                                         UnsupportedOperationException. That
                                                                           way, if MenuItem or Menu doesn’t
  public abstract class MenuComponent {                         support an operation, it doesn’t have
                                                                      to do anything; it can just inherit the
     public void add(MenuComponent menuComponent) {        default implementation.         throw new UnsupportedOperationException();
     }
     public void remove(MenuComponent menuComponent) {
         throw new UnsupportedOperationException();              We’ve grouped together the     }                                                                                “composite” methods — that is,     public MenuComponent getChild(int i) {                                                                       methods to add, remove, and         throw new UnsupportedOperationException();                                                                         get MenuComponents.     }
     public String getName() {
         throw new UnsupportedOperationException();                                                                       Here are the “operation” methods;     }                                                                           these are used by the MenuItems.     public            String                   getDescription()                                    {                                                                                                       use a                                                                                                             also                                                                                     can                                                                        we                                                                             out                                                                              turns                                                                             It         throw               new                   UnsupportedOperationException();                                                                                                      as                                                                                                          too,                                                                           Menu                                                                                                         in                                                                        them                                                                    of                                                                                  couple     }     public double getPrice() {                                                you’ll see in a couple of pages when
         throw new UnsupportedOperationException();          we show the Menu code.
     }
     public boolean isVegetarian() {
         throw new UnsupportedOperationException();
     }                                                                                      print() is an “operation” method
                                                                        that both our Menus and     public void print() {
         throw new UnsupportedOperationException();            MenuItems will implement, but we
     }                                                                         provide a default operation here.
 }

364      Chapter 9


---

## PDF page 403

the iterator and composite patterns

Implementing the MenuItem                      I’m glad we’re going in this
                                                                           direction. I’m thinking this
Okay, let’s give the MenuItem class a shot. Remember,                    is going to give me the flexibility
this is the leaf class in the Composite diagram, and it               I need to implement that crêpe
implements the behavior of the elements of the composite.          menu I’ve always wanted.


public class MenuItem extends MenuComponent {
    String name;                                                               First we need to extend    String description;                                                         MenuComponent    boolean vegetarian;                             the
    double price;                                            interface.
    public MenuItem(String name,                                                    The constructor just takes the                    String description,                                                                 name, description, etc., and                    boolean vegetarian,                                                                   keeps a reference to them all.                    double price)                                                                This is pretty much like our    {
        this.name = name;                                   old MenuItem implementation.
        this.description = description;
        this.vegetarian = vegetarian;
        this.price = price;
    }
    public String getName() {
        return name;
    }                                                                 Here’s our getter
                                                            methods — just like our    public String getDescription() {                                                                  previous implementation.        return description;
    }
    public double getPrice() {
        return price;
    }
                                                              This is different from the previous implementation.    public boolean isVegetarian() {                                                            Here we’re overriding the print() method in the        return vegetarian;                                                       MenuComponent class. For MenuItem this method    }                                                                    prints the complete menu entry: name, description,
    public void print() {                                     price, and whether or not it’s veggie.
        System.out.print("  " + getName());
        if (isVegetarian()) {
            System.out.print("(v)");
        }
        System.out.println(", " + getPrice());
        System.out.println("     -- " + getDescription());
    }
}

                                                                       you are here 4      365


---

## PDF page 404

implementing the new menu class

Implementing the Composite Menu

Now that we have the MenuItem, we just need the composite class, which we’re
calling Menu. Remember, the composite class can hold MenuItems or other Menus.
There’s a couple of methods from MenuComponent this class doesn’t implement,
getPrice() and isVegetarian(), because those don’t make a lot of sense for a Menu.
                 Menu is also a MenuComponent,                   Menu can have any number of children                       just like MenuItem.                                                           of type MenuComponent. We’ll use an                                                                               internal ArrayList to hold these.
 public class Menu extends MenuComponent {
    List<MenuComponent> menuComponents = new ArrayList<MenuComponent>();
    String name;
    String description;                                           This is different than our old
                                                                             implementation: we’re going to give each
    public Menu(String name, String description) {       Menu a name and a description. Before,
        this.name = name;                                   we just relied on having different classes        this.description = description;                      for each menu.    }
    public void add(MenuComponent menuComponent) {
        menuComponents.add(menuComponent);                         Here’s how you add MenuItems or
    }                                                                 other Menus to a Menu. Because                                                                     both MenuItems and Menus are
    public void remove(MenuComponent menuComponent) {        MenuComponents, we just need one
        menuComponents.remove(menuComponent);                 method to do both.
    }                                                                      You can also remove a MenuComponent
                                                                       or get a MenuComponent.    public MenuComponent getChild(int i) {
        return menuComponents.get(i);
    }
                                                         Here are the getter methods for getting the name
    public String getName() {                    and description.
        return name;                                                               Notice, we aren’t overriding getPrice() or    }                                                                 isVegetarian() because those methods don’t make
                                                                  sense for a Menu (although you could argue that    public String getDescription() {                                                                 isVegetarian() might make sense). If someone tries        return description;                                                        to call those methods on a Menu, they’ll get an    }                                                           UnsupportedOperationException.
    public void print() {
        System.out.print("\n" + getName());
        System.out.println(", " + getDescription());                                                                      To print the Menu, we print its        System.out.println("---------------------");                                                                      name and description.    }
}

366      Chapter 9


---

## PDF page 405

the iterator and composite patterns

                                           Wait a sec, I don’t
                                      understand the implementation of print().
                                  I thought I was supposed to be able to apply the
                             same operations to a composite that I could to a leaf. If
                               I apply print() to a composite with this implementation,
                                                 all I get is a simple menu name and description. I don’t
                                   get a printout of the COMPOSITE.


                        Good catch. Because Menu is a composite and contains
                                      both MenuItems and other Menus, its print() method should
                                             print everything it contains. If it doesn’t, we’ll have to iterate
                                      through the entire composite and print each item ourselves.
                                   That kind of defeats the purpose of having a composite
                                              structure.
                                  As you’re going to see, implementing print() correctly is easy
                                       because we can rely on each component to be able to print
                                                            itself. It’s all wonderfully recursive and groovy. Check it out:


Fixing the print() method

public class Menu extends MenuComponent {
    List<MenuComponent> menuComponents = new ArrayList<MenuComponent>();
    String name;
    String description;                                                               All we need to do is change the print() methodabout                                                                                        information                                                                        the                                                                                  only                                                                 not                                                                     it print                                                    make                                                  to                                                                                          components:                                                                              Menu’s    // constructor code here                                                                                   this                                                            of                                                            but all                                                        Menu,                                                              this                                                                       MenuItems.                                                      other Menus and    // other methods here
                                                                      Look! We get to use an Iterator behind    public void print() {                                                                      the scenes of the enhanced for loop. We       System.out.print("\n" + getName());                                                                                  use it to iterate through all the Menu’s       System.out.println(", " + getDescription());                                                                                components...those could be other Menus,       System.out.println("---------------------");                                                                         or they could be MenuItems.
       for (MenuComponent menuComponent : menuComponents) {
           menuComponent.print();                                                                                   Since both Menus and MenuItems       }                                                                             implement print(), we just call    }                                                                                      print() and the rest is up to them.}
       NOTE: If, during this iteration, we encounter another Menu object,
            its print() method will start another iteration, and so on.


                                                                       you are here 4      367


---

## PDF page 406

test drive the menu composite

Getting ready for a test drive...

It’s about time we took this code for a test drive, but we need to update the Waitress code before
we do—after all, she’s the main client of this code:
  public class Waitress {                                                             Yup! The Waitress code really is this simple.      MenuComponent allMenus;                   Now we just hand her the top-level menu                                                              component, the one that contains all the                                                          other menus. We’ve called that allMenus.      public Waitress(MenuComponent allMenus) {
          this.allMenus = allMenus;
      }                                                                              All she has to do to print the entire menu
                                                                          hierarchy — all the menus and all the menu
      public void printMenu() {                              items — is call print() on the top-level menu.
          allMenus.print();
      }                                                                 We’re gonna have one happy Waitress.
  }

Okay, one last thing before we write our test drive. Let’s get an idea of what the menu
composite is going to look like at runtime:

   Every Menu and                                              The top-level menu holds                                                                             all menus and items.  MenuItem implements the
  MenuComponent interface.         Composite


                          AllMenus
           Composite

                            Each Menu
         M                              nu                                                                         Composite           e                               enu   holds items...     DinerMe       PancakeHous                                               ...or items and                       CafeMenu
                                other menus.


                                                                                                                                uItem  MenuItem  MenuItem                               enu       Men      MenuItem  MenuItem  MenuItem     MenuItem  MenuItem  MenuItem  DessertM
                                 Leaf               Leaf                                                              Leaf

                                        MenuItem  MenuItem  MenuItem                                  MenuItem
                                                                    Leaf

368      Chapter 9


---

## PDF page 407

the iterator and composite patterns

Now for the test drive...

Okay, now we just need a test drive. Unlike our previous version, we’re going to
handle all the menu creation in the test drive. We could ask each chef to give us
his new menu, but let’s get it all tested first. Here’s the code:

  public class MenuTestDrive {
      public static void main(String args[]) {                         Let’s first create
          MenuComponent pancakeHouseMenu =                                         all the menu objects.
              new Menu("PANCAKE HOUSE MENU", "Breakfast");
          MenuComponent dinerMenu =
              new Menu("DINER MENU", "Lunch");
          MenuComponent cafeMenu =                                 We also need a top-
              new Menu("CAFE MENU", "Dinner");                                    level menu that we’ll
          MenuComponent dessertMenu =                                   name allMenus.
              new Menu("DESSERT MENU", "Dessert of course!");
          MenuComponent allMenus = new Menu("ALL MENUS", "All menus combined");
                                                                     We’re using the Composite add() method to add          allMenus.add(pancakeHouseMenu);                                                                  each menu to the top-level menu, allMenus.          allMenus.add(dinerMenu);
          allMenus.add(cafeMenu);
                                                             Now we need to add all the menu          // add menu items here                                                                                          items. Here’s one example; for
                                                                          the rest, look at the complete          dinerMenu.add(new MenuItem(                                                                                     source code.              "Pasta",
              "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
              true,              3.89));                                    And we’re also adding a menu to a                                                                        menu. All dinerMenu cares about is that
          dinerMenu.add(dessertMenu);                          everything it holds, whether it’s a menu                                                                     item or a menu, is a MenuComponent.
          dessertMenu.add(new MenuItem(
              "Apple Pie",
              "Apple pie with a flakey crust, topped with vanilla ice cream",
              true,                                                         Add some apple pie to the              1.59));                                                                            dessert menu...
          // add more menu items here
                                                                   Once we’ve constructed our          Waitress waitress = new Waitress(allMenus);                                                                               entire menu hierarchy, we hand
                                                                    the whole thing to the Waitress,          waitress.printMenu();                                                                  and as you’ve seen, it’s as easy as      }                                                                               apple pie for her to print it out. }

                                                                       you are here 4      369


---

## PDF page 408

another test drive

Getting ready for a test drive...
                                                  NOTE: this output is based on the complete source.

    File Edit  Window Help
 % java MenuTestDrive
 ALL MENUS, All menus combined
 ---------------------                                                Here’s all our menus...we printed all
                                                                                  this just by calling print() on the PANCAKE HOUSE MENU, Breakfast                                                                              top-level menu. ---------------------
   K&B’s Pancake Breakfast(v), 2.99
      -- Pancakes with scrambled eggs and toast
   Regular Pancake Breakfast, 2.99
      -- Pancakes with fried eggs, sausage
   Blueberry Pancakes(v), 3.49
      -- Pancakes made with fresh blueberries, and blueberry syrup
   Waffles(v), 3.59
      -- Waffles with your choice of blueberries or strawberries
 DINER MENU, Lunch
 ---------------------
   Vegetarian BLT(v), 2.99
      -- (Fakin’) Bacon with lettuce & tomato on whole wheat
   BLT, 2.99
      -- Bacon with lettuce & tomato on whole wheat
   Soup of the day, 3.29
      -- A bowl of the soup of the day, with a side of potato salad
   Hot Dog, 3.05
      -- A hot dog, with sauerkraut, relish, onions, topped with cheese
   Steamed Veggies and Brown Rice(v), 3.99
      -- Steamed vegetables over brown rice
   Pasta(v), 3.89
      -- Spaghetti with marinara sauce, and a slice of sourdough bread
                                                                               The new DESSERT MENU, Dessert of course! ---------------------                                                                     dessert menu
   Apple Pie(v), 1.59                                                                                                       is printed
      -- Apple pie with a flakey crust, topped with vanilla ice cream      when we are
   Cheesecake(v), 1.99                                                                           printing all the      -- Creamy New York cheesecake, with a chocolate graham crust                                                                                             Diner menu   Sorbet(v), 1.89      -- A scoop of raspberry and a scoop of lime                                 components.
 CAFE MENU, Dinner
 ---------------------
   Veggie Burger and Air Fries(v), 3.99
      -- Veggie burger on a whole wheat bun, lettuce, tomato, and fries
   Soup of the day, 3.69
      -- A cup of the soup of the day, with a side salad
   Burrito(v), 4.29
      -- A large burrito, with whole pinto beans, salsa, guacamole
 %


370      Chapter 9


---

## PDF page 409

the iterator and composite patterns


            What’s the story?
    First you tell us One Class, One
    Responsibility, and now you’re giving us a
pattern with two responsibilities in one class.
The Composite Pattern manages a hierarchy
AND it performs operations related to Menus.


  There is some truth to that observation. We could
    say that the Composite Pattern takes the Single Responsibility
    Principle and trades it for transparency. What’s transparency? Well, by
    allowing the Component interface to contain the child management
    operations and the leaf operations, a client can treat both composites
   and leaves uniformly; so whether an element is a composite or leaf
   node becomes transparent to the client.
   Now, given we have both types of operations in the Component
    class, we lose a bit of safety because a client might try to do something
    inappropriate or meaningless on an element (like try to add a menu
    to a menu item). This is a design decision; we could take the design
    in the other direction and separate out the responsibilities into
    interfaces. This would make our design safe, in the sense that any
    inappropriate calls on elements would be caught at compile time or
    runtime, but we’d lose transparency and our code would have to use
    conditionals and the instanceof operator.
    So, to return to your question, this is a classic case of tradeoff. We
    are guided by design principles, but we always need to observe the
    effect they have on our designs. Sometimes we purposely do things
    in a way that seems to violate the principle. In some cases, however,
    this is a matter of perspective; for instance, it might seem incorrect to
   have child management operations in the leaves (like add(), remove(),
   and getChild()), but then again you can always shift your perspective
   and see a leaf as a node with zero children.


                                             you are here 4      371


---

## PDF page 410

interview with composite

                     Patterns Exposed
                                This week’s interview:
                               The Composite Pattern, on implementation issues

HeadFirst: We’re here tonight speaking with the         HeadFirst: So how do you handle that?
Composite Pattern. Why don’t you tell us a little about                                            Composite: Well, there are a couple of ways to handleyourself, Composite?                                                                                             it; sometimes you can just do nothing, or return null or
Composite: Sure...I’m the pattern to use when you have   false—whatever makes sense in your application. Other
collections of objects with whole-part relationships and      times you’ll want to be more proactive and throw an
you want to be able to treat those objects uniformly.          exception. Of course, then the client has to be willing to
                                                do a little work and make sure that the method call didn’tHeadFirst: Okay, let’s dive right in here...what do you                                                do something unexpected.mean by whole-part relationships?
                                                HeadFirst: But if the client doesn’t know which kind ofComposite: Imagine a graphical user interface (GUI);                                                             object they’re dealing with, how would they ever knowthere you’ll often find a top-level component like a Frame                                                   which calls to make without checking the type?or a Panel, containing other components, like menus,
text panes, scrollbars, and buttons. So your GUI consists    Composite: If you’re a little creative you can structure
of several parts, but when you display it, you generally      your methods so that the default implementations do
think of it as a whole. You tell the top-level component      something that does make sense. For instance, if the client
to display, and count on that component to display all           is calling getChild() on the composite, this makes sense.
its parts. We call the components that contain other       And it makes sense on a leaf too, if you think of the leaf
components, composite objects, and components that don’t      as an object with no children.
contain other components leaf objects.                                                HeadFirst: Ah...smart. But I’ve heard some clients are
HeadFirst: Is that what you mean by treating the objects   so worried about this issue that they require separate
uniformly? Having common methods you can call on         interfaces for different objects so they aren’t allowed to
composites and leaves?                             make nonsensical method calls. Is that still the Composite
                                                           Pattern?Composite: Right. I can tell a composite object to
display or a leaf object to display and it will do the right    Composite: Yes. It’s a much safer version of the
thing. The composite object will display by telling all its     Composite Pattern, but it requires the client to check the
components to display.                                    type of every object before making a call so the object can
                                                   be cast correctly.HeadFirst: That implies that every object has the same
interface. What if you have objects in your composite that   HeadFirst: Tell us a little more about how these
do different things?                                     composite and leaf objects are structured.
Composite: In order for the composite to work         Composite: Usually it’s a tree structure, some kind of
transparently to the client, you must implement the same     hierarchy. The root is the top-level composite, and all its
interface for all objects in the composite; otherwise, the      children are either composites or leaves.
client has to worry about which interface each object                                                HeadFirst: Do children ever point back up to theiris implementing, which kind of defeats the purpose.                                                           parents?Obviously that means that at times you’ll have objects for
which some of the method calls don’t make sense.        Composite: Yes, a component can have a pointer to a
                                                         parent to make traversal of the structure easier. And, if

372      Chapter 9


---

## PDF page 411

the iterator and composite patterns


you have a reference to a child and you need to delete it,
you’ll need to get the parent to remove the child. Having
the parent reference makes that easier too.
HeadFirst: There’s really quite a lot to consider in your
implementation. Are there other issues we should think
about when implementing the Composite Pattern?
Composite: Actually, there are. One is the ordering
of children. What if you have a composite that needs to
keep its children in a particular order? Then you’ll need a
more sophisticated management scheme for adding and
removing children, and you’ll have to be careful about
how you traverse the hierarchy.
HeadFirst: A good point I hadn’t thought of.
Composite: And did you think about caching?
HeadFirst: Caching?
Composite: Yeah, caching. Sometimes, if the
composite structure is complex or expensive to traverse,
it’s helpful to implement caching of the composite nodes.
For instance, if you are constantly traversing a composite
and all its children to compute some result, you could
implement a cache that stores the result temporarily to
save traversals.
HeadFirst: Well, there’s a lot more to the Composite
Patterns than I ever would have guessed. Before we wrap
this up, one more question: what do you consider your
greatest strength?
Composite: I think I’d definitely have to say simplifying
life for my clients. My clients don’t have to worry about
whether they’re dealing with a composite object or a
leaf object, so they don’t have to write if statements
everywhere to make sure they’re calling the right methods
on the right objects. Often, they can make one method
call and execute an operation over an entire structure.
HeadFirst: That does sound like an important benefit.
There’s no doubt you’re a useful pattern to have around
for collecting and managing objects. And, with that, we’re
out of time. Thanks so much for joining us and come
back soon for another Patterns Exposed.

                                                                       you are here 4      373


---

## PDF page 412

crossword puzzle

         Design Patterns Crossword
                Wrap your brain around this composite crossword.

                          1                                   2


                                       3                          4                          5        6

                     7                                        8


            9                                                                   10

                                            11            12

            13                14


                                                              15


            16


                 17


ACROSS                          DOWN
1. Collection and Iterator are in this package.                   2. Has no children.
3. This class indirectly supports Iterator.                         4. Merged with the Diner (two words).
8. Iterators are usually created using this pattern (two          5. The Iterator Pattern decouples the client from the
words).                                                    aggregate’s ________.
12. A class should have only one reason to do this.             6. A separate object that can traverse a collection.
13. We encapsulated this.                                       7. HashMap values and ArrayList both implement this
15. User interface packages often use this pattern for           interface.
their components.                                                9. We Java-enabled her.
16. Name of the principle that states only one                 10. A component can be a composite or this.
responsibility per class (two words).                           11. A composite holds these.
17. This menu caused us to change our entire                12. Third company acquired.
implementation.                                             14. We deleted the PancakeHouseMenuIterator because
                                                                        this class already provides an iterator.


374      Chapter 9


---

## PDF page 413

the iterator and composite patterns


Match each pattern with its description:

   Pattern              Description

      Strategy                          Clients treat collections
                                      of objects and individual
                                       objects uniformly

                                      Provides a way to traverse     Adapter
                                   a collection of objects
                                     without exposing the
                                             collection’s implementation
      Iterator
                                      Simplifies the interface of
                                   a group of classes

                                   Changes the interface of     Facade
                                  one or more classes

                                  Allows a group of objects to
                                be notified when some state     Composite
                                     changes

                                      Encapsulates interchangeable
                                     behaviors and uses delegation to     Observer
                                   decide which one to use


                                                           you are here 4      375


---

## PDF page 414

your design toolbox

         Tools for your Design Toolbox
           Two new patterns for your toolbox—two great ways to
                deal with collections of objects.                             An Iterator allows access to an
                                                                                            aggregate’s elements without
                                                                                       exposing its internal structure.
                                                               An Iterator takes the job of
                                                                                                              iterating over an aggregate     PrinciplesOO Basics                                      and encapsulates it in another OO                                                                                                       object.            what varies          Abstraction    Encapsulate
                                                               When using an Iterator, we                             inheritance.  Encapsulation    Favor composition over                                                                                                       relieve the aggregate of the                      not                  interfaces,           Polymorphism                                                    responsibility of supporting     Program to
      implementations.                  Inheritance                                               operations for traversing its                                designs                       coupled                                                                      data.           for loosely       Strive        that interact.               objects      between                                                       An Iterator provides a                                 extension                                                                    common interface for               should be open for        Classes                       modification.                                                                                                   traversing the items of an       but closed for                   Do not                                                           aggregate, allowing you to use             on abstractions.       Depend                                 classes.                          important                   polymorphism when writing             on concrete        depend                       Yet another  on change                code that makes use of the                                              based                             friends.                    principle                                                                                           items of the aggregate.         Only talk to your                                         in a design.
                                                               The Iterable interface provides         Don’t call us, we’ll call you.                                    reason                                               a means of getting an                      have only one                  should      A class                                                                                                                iterator and enables Java’s         to change.                                                                                enchanced for loop.
                                                               We should strive to assign
                                                                                               only one responsibility to each                                               Another two-for-one     Patterns                                      algorithms,                       of OO                          family                                                                                                      class.               a                        one-to-many                a                                                      chapter.                defines       -                  defines          -                            them                                an                             that                               additional                            so   Strategy                    and                                Provide                   -                   Attach                                 an                     one,            -                          makesobjects    Observer              each                                      algorithm                                Define                                                                                 -                                    dynamically.                                       its                                                                            The                                                                                      Composite                                                                                                              Pattern                                                                                                                     allows               between                            the               Factory                                         all                            of                               lets                                           one     encapsulates                          object     Decorator                                         has                              state,                   an                                    but                                    families      dependency                 to                   Strategy                                          only              Method                                                 it.       Abstract                     changes                                     use                                         class                                       object,                      a                        creating                           an                             that                                                                                                           clients                                                                                                                to treat                                                                                                   composites                                                                                                   and               object         Factory                 for                                              request                              updated                            a          responsibilities                           Ensure                               flexible      interchangeable.                                   without                               clients          one                -                                   of                 a                           creating                        and                  from     when                                          point                                  to           interface                   for                              objects                                           class                                        global                  -                                   extending                      a             Singleton                are              interface                    depedentnotified                           forEncapsulates                              which                                               request                                        you                                                                                                        individual                                                                                                          objects                                                                                                                        uniformly.               or                             a        Decoratorsindependently     vary                            provide                         decide                                          classes.                                         letting                   and       dependents                         subclassing           related                                           lets            Commandprovideto                                  Encapsulates                          concrete                   subclasses                   -                              thereby                 instance             let                           Method                     their                                                requestyou                          object,          alternative                             a                                           different                 an                                            letting                        Factory                             it.                 as              Adapter                                   with        automatically             specifying                  to                                  the                                                                                                    access                                                                 A                                                                             Component                                                                                                                                          is                                                                                              any                                                                                                                      object                              to                                thereby                                               the                                    clients                                    Encapsulates                           to                 access                    -                instantiate.                                             you                                       and                        way                             object,                  a                                             Define                                              different           functionality.                             -                                               letting                              instantiation                                     with                                            requests,                Facadean                   parameterize                     Provideas            -                   defer                                       clients                           or                                   thereby                                     logobject                       Method                                                                                                                in                                                                                a Composite                                                                                                                         structure.                                                            operation,                  class         a                                         an                           queue                                object,                                                 inand                                                 different       Iterator                     anaggregate                    Template                     asan                                               requests,                      parameterize                                        with                      requests,                of                                       log                                          algorithm                                        operations.                             or                              an                                          clients                                      its                          of                                                                     into                                                                             Components                                                                              may                                                                                             be                                                                                                                    other                                            and              elements                              queue                  subclasses.        the                                                           subclasses.                              exposing                                                               objects                              skeletonundoable                                     to                                                  requests,                         parameterize                         requests,                    support                                          logsteps                    without                                           operations.                               or                                                 Compose                                -                                 some                                queue                              undoable                                                                                      composites                                                                                                              or                                                                                                              leaves.                                                               part-whole            sequentially                                                        subclasses                             deferring                            requests,                       support                                              lets                              Composite                                                          represent                                              operations.                     representation                                           to                                                                 treat                             Method                                                         algorithm                                 undoable                                          an            underlying                                                                         clients                                               structures                                     of                           Template                                                               lets                          support                                     tree                                             steps                                                                                                                                                There                                                                                                are                                                                               many                                                                                                       design                                                     of                                                  Composite                                      certain                             redefine                                                                  compositions                                               hierarchies.the algorithm’s                                      changing                                                   objects and                            without     individual                                                tradeoffs in implementing                                                                                      Composite. You need to                               structure   objects uniformly                                                                                       balance transparency and
                                                                                                  safety with your needs.


376      Chapter 9


---

## PDF page 415

the iterator and composite patterns


     Based on our implementation of printMenu(), which of the following apply?


❏  A. We are coding to the          ❏  D. The Waitress needs to know how each
       PancakeHouseMenu and DinerMenu         menu represents its internal collection of
        concrete implementations, not to an          menu items; this violates encapsulation.
          interface.                       ❏  E. We have duplicate code: the printMenu()
❏  B. The Waitress doesn’t implement the            method needs two separate loops to
        Java Waitress API and so she isn’t                   iterate over the two different kinds of
        adhering to a standard.                       menus. And if we added a third menu,
                                                    we’d have yet another loop.❏  C. If we decided to switch from using
       DinerMenu to another type of menu   ❏   F. The implementation isn’t based on
         that implemented its list of menu items      MXML (Menu XML) and so isn’t as
        with a hash table, we’d have to modify            interoperable as it should be.
        a lot of code in the Waitress.


                                        Before looking at the next page, quickly jot down the three
                                         things we have to do to this code to fit it into our framework:
1.  implement the Menu interface
2.  get rid of getItems()
3.  add createIterator() and return an Iterator that can step through the HashMap values


                                                                   you are here 4      377


---

## PDF page 416

exercise solutions

      Code Magnets Solution
            The unscrambled “Alternating” DinerMenu Iterator.


    import java.util.Iterator;
    import java.util.Calendar;
   public class AlternatingDinerMenuIterator   implements Iterator<MenuItem>   }
       MenuItem[] items;
      int position;
       public AlternatingDinerMenuIterator(MenuItem[] items)  }
           this.items = items;
           position = Calendar.DAY_OF_WEEK % 2;
      }
       public boolean hasNext() {
          if (position >= items.length || items[position] == null) {
              return false;
          } else {
              return true;
          }
      }
       public MenuItem next() {
                MenuItem menuItem = items[position];
                position = position + 2;
                return menuItem;
      }                                                                         Notice that this Iterator
                                                                                         implementation does not         public void remove() {                                                                                        support remove().
              throw new UnsupportedOperationException(
                  "Alternating Diner Menu Iterator does not support remove()");      }
   }

378      Chapter 9


---

## PDF page 417

the iterator and composite patterns


              SOlUTion


Match each pattern with its description:

   Pattern              Description

      Strategy                          Clients treat collections
                                      of objects and individual
                                       objects uniformly

                                      Provides a way to traverse     Adapter
                                   a collection of objects
                                     without exposing the
                                             collection’s implementation
      Iterator
                                      Simplifies the interface of
                                   a group of classes

                                   Changes the interface of     Facade
                                  one or more classes

                                  Allows a group of objects to
                                be notified when some state     Composite
                                     changes

                                      Encapsulates interchangeable
                                     behaviors and uses delegation to     Observer
                                   decide which one to use


                                                         you are here 4      379


---

## PDF page 418

crossword puzzle solution

         Design Patterns Crossword Solution
                Wrap your brain around this composite crossword. Here’s our solution.


                            1                                   2                 J A  V A     .  U  T  I  L
                                          E
                                         3                          4                          5        6                      H A  S H M A  P                   I      I
                       7                                        8                C                          F  A  C  T O  R  Y M  E  T H O  D
            O                      N                    P     E
              9                                                                   10      W     L                             C         L         L     R
                                              11            12        A     L              C        C H A N  G  E        E    A
              13                14           I  T  E  R  A  T  I O N    A     K       A     M    T
         T     C     R     M        F     E        F        E    O
          R    T     R         P        E    H             N     R
                                                                15          E      I    A      O           C O M  P O  S  I  T  E
         S    O     Y      N           U              A
              16         S  I N  G  L  E  R  E  S  P O N  S  I  B  I  L  I  T  Y
                        I      N             E                   I
                   17           D  E  S  S  E  R  T                        O
                    T       S                        N


380      Chapter 9
