| [Module Overview](./unittest_module.md) | [*What is Unit Testing*](./what_is_unit_testing.md) | [Black Box](./black_box.md) | [White Box](./white_box.md) | [Debrief](./debrief.md) |
|-----------------|----------------------|-----------|-----------|---------|
|                 |                      |           |           |         |

### What is Software Testing?

As you learned in Software Engineering I, there are many approaches for developing software (e.g. Waterfall and Agile). No matter which one you use, they all will generally have similar phases: Requirements, Design, Implementation, and Verification. _Software Testing_ occurs during the _Verification_ phase.

The goal of the Verification phase is to establish that the work done during the Implementation phase satisfies the Design and Requirements. In other words, "Does the code do the things we said we wanted it to do?" There are multiple ways of verifying software, but the one we are going to focus on is Software Testing (naturally).

Software Testing can be boiled down to trying to generate a fail state in the software with the ultimate goal of being unsuccessful in doing so.

By testing our software, we hope to identify instances where the behavior of the program deviates from the expected: a _failure_.

* **Failure** - a deviation from the expected behavior

  * These failures occur because there exists a "bug" in the code: a _fault_.

* **Fault**: - an instance of incorrect code that can lead to a failure

  * A fault is introduced to the program when a programmer makes a mistake: an _error_.

* **Error** - a mistake that introduces a fault (e.g. typo and conceptual misunderstanding)

So, in plain English, a test can help identify when the program does not behave as intended and therefore indicates a fault exists. Once we know a fault exists, we can track it down and fix it. That said, we may never know what error actually caused the fault in the first place, but that is ultimately irrelevant.

### Types of Testing

There are dozens of different ways of testing software, with more being developed and researched every day, but each can generally be put into one of two categories: Functional Testing or Non-functional Testing.

**Thought Experiment**

Take a moment and ponder the following questions before moving on:

* What types of things do you suppose would be verified using Functional Testing?
* What types of things do you suppose would be verified using Non-functional Testing?

Let's see if your predictions are correct!

#### Functional Testing

These types of tests are used to verify that the software meets the requirement specifications when it comes to functionality; does the software do the things it is expected to do?

**Examples:**

* Does clicking "save" actually save the changes to the hard drive?
* Does the search algorithm actually find the shortest path?
* Does the isItPrime function correctly identify prime numbers?
* Does the database correctly supply responses to the client?

#### Non-functional Testing

These types of tests are used to verify that the software performs at the required levels. This can literally mean performance, but also usability, reliability, and robustness.

**Examples**

* Does the webpage load in less than 2 seconds?
* Does the interface provide enough clues for easy navigation?
* Does the system successfully recover from a catastrophic failure?
* Does the service support 10,000+ active users at a time?

#### Ways of Testing

Both Functional and Non-functional Testing are very important to the successful deployment of a software system. Within each category of testing there are many different approaches. Below are just a few of the dozens of testing methods.

**Types of Functional Testing**

* Unit testing
* Integration testing
* Regression testing

**Types of Non-functional Testing**

* Performance testing
* Scalability testing
* Usability testing

For this class we will be focusing mostly on Functional Testing and, for this module, Unit Testing in particular.

#### So, What is Unit Testing Already!?

I have put this off long enough. It is time for the meat of the discussion! _Unit Testing_ is when individual _units_ of the software are _tested_...

Drat! You shouldn't use the word when defining it! Let's try again.

_Unit Testing_ is when the smallest component of a software system is verified to produce the expected behavior.

OK, that was _MUCH_ better! The smallest component is also called a _unit_ and we verify using _testing_, hence the name Unit Testing. 

A _unit_ will typically be a single method that takes a few inputs and has a single output. Below you will find an example of how we can use Python's unittest library to write automated tests. The two provided tests are attempting to verify that our implementation of `sum()` behaves correctly.

To run the tests simply click the **play** button in the top center. In the console you should see that we have two tests that are run and that they both pass with an "ok".

<iframe height="600px" width="100%" src="https://repl.it/@ericianni/whatisunittesting1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

**Leading Question Time**

* Seeing as both of our tests pass can we safely assume `sum()` is correct and we don't need any more tests?

Considering that there is a "Write your own test!" comment I am sure you answered correctly that we can't assume `sum()` is correct. I can tell you now that there is indeed a **fault** in the code that leads to a **failure** (see what I did there?). Without looking at the implementation of `sum()`, see if you can write a test that can expose the error. For more details on how to use _unittest_ please see the resource section below.

When you either find the error or grow bored with the hoops I am asking you to jump through find me on the next page for the answer.

[Black Box testing](./black_box.md)


### Resources

* [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
* [Python unittest tutorial](https://pymotw.com/2/unittest/)
