| [Module Overview](./unittest_module.md) | [What is Unit Testing](./what_is_unit_testing.md) | [Black Box](./black_box.md) | [White Box](./white_box.md) | [Debrief](./debrief.md) |
|-----------------|----------------------|-----------|-----------|---------|
|                 |                      |           |           |         |

### Providing Answers

Did you find the error without looking at the source for `sum()`? If you didn't that is just fine as we are just getting started on our testing journey. I have taken the liberty to craft a new test to expose a fault in `sum()`.


<iframe height="600px" width="100%" src="https://repl.it/@ericianni/blackbox1?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

This third test shows that `sum()` doesn't correctly add a floating point to an integer. Now that we have observed a failure we know that there is a fault in the code that has something to do with floating point numbers.

Notice how we were able to do all of this without ever looking at the source for `sum()`! We have just written our first _Black Box_ test!

### What is Black Box Testing?

Imagine there is a box sitting before you. It is solid black and you cannot see into it. Now imagine that you are told the box contains 20 lbs of gold! You are offered this box in exchange for your 2002 Dodge Neon. You know that if what you are being told is true, this box would be worth more than $18,000 while your car is worth less than half that. But how can you know that the box really has 20 lbs of gold in it?

The easy answer would be to open it up and look inside. But this mysterious figure will not allow that so you need to figure out another way to verify at least part of what is being promised.

One way to verify part of the claim is to weigh the box. If the box weighs <= 20 lbs you know that this person is a con-artist because it doesn't meet the weight expectations. 

This is an example of black-box testing outside of the world of software development. You were presented with an object and given a description. You were able verify at least part of that description without having any actual knowledge of the contents of the box. 

**Definition Time**

_Black Box Testing_ is when you write tests based purely on the description provided for the software (a.k.a. the specification).

### Advantages of Black Box Testing

* Focuses on the input domain for the software
  * Allows targeted testing of possible inputs
* There is no need for the actual code
  * Non-developers can write tests
  * Tests can be written _before_ the actual code
  * Allows for unbiased tests by separating the tester from the developer
* Can catch logic errors that other types of testing cannot
* Can be used at all levels of testing: unit testing, integration testing, and so on

### Disadvantages of Black Box Testing

* It isn't possible to test every possible input, so tests may miss logic branches/program paths untested (more on this in ([White Box](./white_box.md))
* There is no way to know why the failure occurs, just that it indicates a fault
* Poorly written specifications can lead to inaccurate tests

### Black Box Testing Approaches

As mentioned above, black box testing is any type of testing that is based purely on the specification. This is a very broad definition with many different ways of approaching the task. Let's take a look at some!

#### Random Testing

This approach randomly selects inputs from the specified input domain and sends them into the black box. 

Can you think of at least one advantage and at least one disadvantage?

Check your guesses below:

* Advantages
  * Quick to write
  * Can cover large portions of the input domain with very little code
  * Can potentially generate an input that no-one considered
* Disadvantages
  * Many random inputs could fall under the same "test case" so become redudent and a waste of resources
  * May not test the _tricky_ parts of the input domain like _edge cases_ (see boundary testing below)
  
#### Boundary Testing

This approach is based on the idea that errors are more likely to be introduced around the _boundaries_ of the input domain. 

### Time to get our hands dirty!


