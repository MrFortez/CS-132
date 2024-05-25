// Name: Brandon Fortes
// Description: Java version of Room Adventure
// Improvements: 
//  0: Added Room 4, with a few bedroom themed items and a... flamethrower...
//  1: Added a "Use" action, which makes something happen based on the item you use.
//  2: Added a Locking mechanic, preventing you from entering a room until you use a certain item
//      to unlock it.
//  3: Added a win condition, that being using the flamethrower to uncover the exit in Room 2, then
//      going through that exit.


import java.util.Scanner;


public class RoomAdventure {

    private static Room currentRoom;
    private static String[] inventory = {null, null, null, null, null};
    private static String status;

    final private static String DEFAULT_STATUS = "Sorry, I don't understand. Try [verb] [noun]. Valid verbs are go, look, take, and use";
    
    public static void main(String[] args){
        setupGame();

        while (true){
            // Print info about game.
            System.out.println(currentRoom);
            System.out.println("Inventory: ");
            for (int i=0; i < inventory.length; i++){
                System.out.print(inventory[i] + " ");
            }
            System.out.println("\nWhat would you like to do? ");

            // take input
            Scanner s = new Scanner(System.in);
            String input = s.nextLine(); // wait here for input

            // process input
            String[] words = input.split(" ");

            if (words.length != 2){
                status = DEFAULT_STATUS;
            }

            String verb = words[0];
            String noun = words[1];

            switch (verb){
                case "go":
                    handleGo(noun);
                    break;
                case "look":
                    handleLook(noun);
                    break;
                case "take":
                    handleTake(noun);
                    break;
                case "use":
                    handleUse(noun);
                    break;
                default: status = DEFAULT_STATUS;
            }

            if (currentRoom.getName().equals("exitRoom")) {
                System.out.println("You crawled through the unfired-fireplace and managed to escape. You Win!");
                break;
            }

            System.out.println(status);
        }
    }

    private static void handleGo(String noun){
        String[] exitDirections = currentRoom.getExitDirections();
        Room[] exitDestinations = currentRoom.getExitDestinations();
        status = "I don't see that exit.";
        for (int i = 0; i < exitDirections.length; i++){
            if (noun.equals(exitDirections[i])) {
                if (exitDestinations[i].getIsLocked()) {
                    if (exitDestinations[i].getName().equals("exitRoom")) {
                        status = "unless you want to crawl through that active fire, you're not gonna be going north for now.";
                    } else {
                        status = "That room is locked! You need to use a key to unlock it.";
                    }
                } else {
                    currentRoom = exitDestinations[i];
                    status = "Changed Room.";
                }
            }
        }
    }

    private static void handleLook(String noun){
        String[] items = currentRoom.getItems();
        String[] itemDescriptions = currentRoom.getItemDescriptions();
        status = "I don't see that item.";
        for (int i = 0; i < items.length; i++){
            if (noun.equals(items[i])){
                status = itemDescriptions[i];
            }
        }
    }

    private static void handleTake(String noun){
        String[] grabbables = currentRoom.getGrabbables();
        status = "I can't grab that.";
        for (int i=0; i < grabbables.length; i++){
            if (noun.equals(grabbables[i])){
                for (int j = 0; j < inventory.length; j++){
                    if (inventory[j] == null){
                        inventory[j] = noun;
                        status = "Added it to the inventory";
                        break;
                    }
                }
            }
        }
    }

    private static void handleUse(String noun) {
        switch(noun) {
            case "book":
                status = "You would use the book but then you realized that you never learned how to read. Worse yet it is The Great Gatsby, that stupid pile of trash that is nothing but rich people problems the book and could easily be replaced by any other book to be a staple in high school english classes but just isnt for some reason. Why do people still like this trash";
                break;
            case "pillow":
                status = "You squeeze the pillow. It feels very good :)";
                break;
            case "satsuma":
                status = "You take a bite out of the satsuma. It taste acidic but also very good.";
                break;
            case "key":
                for (Room room : currentRoom.getExitDestinations()) {
                    if (room.getIsLocked() && !room.getName().equals("exitRoom")) {
                        status = "You used the key and unlocked the room!";
                        room.setIsLocked(false);
                        break;
                    } else {
                        status = "There's no rooms to unlock in this area";
                    }
                }
                break;
            case "flamethrower":
                for (Room room : currentRoom.getExitDestinations()) {
                    if (room.getName().equals("exitRoom")) {
                        status = "You use the flamethrower to throw flames onto the fireplace. For some bizarre reason, this causes it to fizzle out, revealing a secret passage!";
                        room.setIsLocked(false);
                        break;
                    } else {
                        status = "Despite your immense desire to burn everything to the ground, nothing in this room looks flammable.";
                    }
                }
                break;
        }
    }

    public static void setupGame(){
        Room room1 = new Room("Room 1");
        Room room2 = new Room("Room 2");
        Room room3 = new Room("Room 3");
        Room room4 = new Room("Room 4");

        // Exit Room, used for victory sequence
        Room exitRoom = new Room("exitRoom");
        exitRoom.setIsLocked(true);


        // Setup Room 1
        String[] room1ExitDirections = {"east", "south"};
        Room[] room1ExitDestinations = {room2, room3};

        String[] room1Items = {"chair", "stool", "TV"};
        String[] room1ItemDescriptions = {
            "It is a chair.", 
            "It's like a chair. There is a key on it.",
            "It is a 4k 72 inch flatscreen tv with surround sound systems, 3D visuals, special effects, the capability to make you meals, the ability to make you a gazillion dollars, the ability to serve as a father figure to your family, the ability to ......"
        };  

        String[] room1Grabbables = {"key"};

        room1.setExitDirections(room1ExitDirections);
        room1.setExitDestinations(room1ExitDestinations);
        room1.setItems(room1Items);
        room1.setItemDescriptions(room1ItemDescriptions);
        room1.setGrabbables(room1Grabbables);


        // Setup Room 2
        String[] room2ExitDirections = {"west", "south", "north"};
        Room[] room2ExitDestinations = {room1, room4, exitRoom};

        String[] room2Items = {"rug", "fireplace", "recliner"};
        String[] room2ItemDescriptions = {
            "It's like a chair but flat. There is a satsuma on it.", 
            "It's hot. If only there was a way to make it even hotter and even more fiery",
            "It's a comfy recliner. You pat it on the head for being epic"
        };

        String[] room2Grabbables = {"satsuma"};

        room2.setExitDirections(room2ExitDirections);
        room2.setExitDestinations(room2ExitDestinations);
        room2.setItems(room2Items);
        room2.setItemDescriptions(room2ItemDescriptions);
        room2.setGrabbables(room2Grabbables);


        // Setup Room 3
        String[] room3ExitDirections = {"north", "east"};
        Room[] room3ExitDestinations = {room1, room4};

        String[] room3Items = {"statue", "bookshelf"};
        String[] room3ItemDescriptions = {
            "It's the lady of the mist. A full sized replica.", 
            "There is one book on it."
        };

        String[] room3Grabbables = {"book"};

        room3.setExitDirections(room3ExitDirections);
        room3.setExitDestinations(room3ExitDestinations);
        room3.setItems(room3Items);
        room3.setItemDescriptions(room3ItemDescriptions);
        room3.setGrabbables(room3Grabbables);


        // Setup Room 4
        String[] room4ExitDirections = {"north", "west"};
        Room[] room4ExitDestinations = {room2, room3};

        String[] room4Items = {"bed", "couch", "nightstand"};
        String[] room4ItemDescriptions = {
            "Its a queen sized bed with purple blankets. It has drapes on the side and some very comfy and very grabbable pillows", 
            "A flower patterned couch, its cushions are pretty soft",
            "A wooden nightstand next to the bed. There is a flamethrower on it... for some reason."
        };

        String[] room4Grabbables = {"pillow", "flamethrower"};

        room4.setExitDirections(room4ExitDirections);
        room4.setExitDestinations(room4ExitDestinations);
        room4.setItems(room4Items);
        room4.setItemDescriptions(room4ItemDescriptions);
        room4.setGrabbables(room4Grabbables);





        //note that room 1 (the one with the key in it) cant be locked
        int lockedRoom = (int) Math.random() * 3;

        switch(lockedRoom) {
            case 0:
                room2.setIsLocked(true);
                break;
            case 1:
                room3.setIsLocked(true);
                break;
            case 2:
                room4.setIsLocked(true);
                break;
        }
        currentRoom = room1;
    }
}

class Room{

    private String name;
    private String[] exitDirections;
    private Room[] exitDestinations;
    private String[] items;
    private String[] itemDescriptions;
    private String[] grabbables;
    private boolean isLocked;

    public Room(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setExitDirections(String[] exitDirections) {
        this.exitDirections = exitDirections;
    }

    public String[] getExitDirections()  {
        return exitDirections;
    }

    public void setExitDestinations(Room[] exitDestinations)  {
        this.exitDestinations = exitDestinations;
    }

    public Room[] getExitDestinations() {
        return exitDestinations;
    }

    public void setItems(String[] items) {
        this.items = items;
    }

    public String[] getItems() {
        return items;
    }

    public void setItemDescriptions(String[] itemDescriptions) {
        this.itemDescriptions = itemDescriptions;
    }

    public String[] getItemDescriptions() {
        return itemDescriptions;
    }

    public void setGrabbables(String[] grabbables) {
        this.grabbables = grabbables;
    }

    public String[] getGrabbables() {
        return grabbables;
    }

    public void setIsLocked(boolean islocked) {
        this.isLocked = islocked;
    }

    public boolean getIsLocked() {
        return isLocked;
    }

    public String toString() {
        String result = "\n";
        result += "Location: " + name;

        // add items to the output
        result += "\nYou See: ";
        for (int i = 0; i < items.length; i++){
            result += items[i] + " ";
        }

        // add exits to the output
        result += "\nExits: ";
        for (int i = 0; i < exitDirections.length; i++){
            result += exitDirections[i] + " ";
        }

        return result;
    }

}