

public class GameCharacter {

    // Constants
    private final int MAXLIVES = 5;

    // Instance Variables
    private String name = "";
    private int lives = 0;
    private String[] inventory = new String[5];



    // Base Constructor
    public GameCharacter() {
        setName("Sam Sung");
        setLives(MAXLIVES);
        for (int i = 0; i < inventory.length; i++) {
            inventory[i] = null;
        }
    }

    // Constructor with parameters for name and lives
    public GameCharacter(String name, int lives) {
        setName(name);
        setLives(lives);        
        for (int i = 0; i < inventory.length; i++) {
            inventory[i] = null;
        }
    }

    // name getter
    public String getName() {
        return name;
    }

    // name setter 
    public void setName(String val) {
        name = val;
    }

    // lives getter
    public int getLives() {
        return lives;
    }

    // lives setter, clamping it between zero and the max lives
    public void setLives(int val) {
        if (val >= MAXLIVES) {
            lives = MAXLIVES;
        }
        else if (val <= 0) {
            lives = 0;
        }
        else {
            lives = val;
        }
    }

    // inventory getter
    public String[] getInventory() {
        return inventory;
    }

    // inventory setter
    public void setInventory(String[] val) {
        inventory = val;
    }

    // returns whether or not the character has more than zero lives
    public boolean isAlive() {
        return lives > 0;
    }

    // checks the character's inventory for certain key words
    public boolean hasWeapon() {
        for (String item : inventory) {
            if (item != null) {
                if (item.equals("knife") || item.equals("gun")) {
                    return true;
                }
            }
        }
        
        return false;
    }

    // returns the size of the character's inventory
    public int sizeOfInventory() {
        int size = 0;
        for (String item : inventory) {
            if (item != null) {
                size++;
            }
        }
        return size;
    }

    // sets lives to the max lives value
    public void heal() {
        setLives(MAXLIVES);
    }

    // decreases lives by one if the character isnt dead
    public void damage() {
        if (isAlive()) {
            setLives(lives - 1);
        }
    }

    // adds an item to the inventory if there is an open spot available (aka a null value)
    public void pickUp(String newItem) {
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] == null) {
                inventory[i] = newItem;
                break;
            }
        }
    }

    // removes the specified item from the inventory if it is present
    public void drop(String droppedItem) {
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] != null) {
                if (inventory[i].equals(droppedItem)) {
                    inventory[i] = null;
                }
            }
        }
    }

    // to string method
    public String toString() {
        String str = String.format("Name: %s \nLives: %d \nInventory: ", name, lives);
        for (String item : inventory) {
            if (item != null) {
                str += item + ", ";
            }
        }
        return str + "\n";
    }
}
