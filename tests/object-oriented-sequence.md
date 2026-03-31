# Object-Oriented Programming language Concepts to be covered


- For each concept, create a file and write your exercise in that file. Make sure you cover it for both  `python` and `typescript` languages.
- Each script/file should have proper comments and instructions on how to run the code


## 1. Encapsulation
**The Concept:** Bundling data (attributes) and methods (functions) that operate on that data into a single unit (a class). Crucially, it involves **hiding the internal state** of an object from the outside world, usually by making attributes private and providing "getters" and "setters."



* **Exercise:** Create a `BankAccount` class. 
    * Make the `balance` attribute private (e.g., `_balance` or `__balance`).
    * Provide a `deposit()` and `withdraw()` method. 
    * **The Twist:** Add logic to `withdraw()` so it only works if the balance is sufficient. This prevents the user from manually setting a negative balance.

---

## 2. Abstraction
**The Concept:** Hiding complex implementation details and showing only the necessary features of an object. Think of a car: you know how to use the steering wheel and pedals (the interface), but you don't need to understand the internal combustion logic to drive it.

* **Exercise:** Create an abstract class `Document`.
    * Define an abstract method `open()`. 
    * Create two subclasses: `PDF` and `WordDocument`. 
    * Implement the `open()` method differently for each (e.g., "Opening PDF in Acrobat" vs "Opening Word in Office").
    * **The Goal:** The user should be able to call `.open()` on any Document without knowing which type it is.

---

## 3. Inheritance
**The Concept:** Allowing a new class (subclass/child) to inherit the attributes and methods of an existing class (superclass/parent). This promotes code reuse.



* **Exercise:** Build a "Smart Home" hierarchy.
    * **Parent:** `ElectronicDevice` with attributes like `brand` and `power_status`.
    * **Children:** `SmartLight` and `SmartThermostat`. 
    * Give the `SmartLight` a `change_color()` method and the `SmartThermostat` a `set_temperature()` method. 
    * **The Twist:** Both should inherit an `is_on()` method from the parent.

---

## 4. Polymorphism
**The Concept:** The ability of different objects to respond to the same method call in their own way. "Polymorphism" literally means "many shapes."

* **Exercise:** The "Animal Sound" test.
    * Create a list containing different objects: `Dog()`, `Cat()`, and `Duck()`.
    * Each class should have a method called `make_sound()`. 
    * **The Task:** Write a loop that iterates through the list and calls `animal.make_sound()` for every item. 
    * **Result:** You get a "Woof," "Meow," and "Quack" from the same line of code.

---

### Summary Checklist

| Concept | Keyword | Real-world Analogy |
| :--- | :--- | :--- |
| **Encapsulation** | *Protection* | A medicine capsule protecting the powder inside. |
| **Abstraction** | *Simplicity* | A TV remote (you press buttons, you don't rewire the TV). |
| **Inheritance** | *Reuse* | A child inheriting DNA from a parent. |
| **Polymorphism** | *Flexibility* | The "Play" button (works on a video, a song, or a podcast). |

---