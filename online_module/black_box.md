| [Module Overview](./unittest_module.md) | [What is Unit Testing](./what_is_unit_testing.md) | [*Black Box*](./black_box.md) | [White Box](./white_box.md) | [Debrief](./debrief.md) |
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

* **Advantages**
  * Quick to write
  * Can cover large portions of the input domain with very little code
  * Can potentially generate an input that no-one considered
* **Disadvantages**
  * Many random inputs could fall under the same "test case" so become redudent and a waste of resources
  * May not test the _tricky_ parts of the input domain like _edge cases_ (see boundary testing below)
  
#### Boundary Testing

This approach is based on the idea that errors are more likely to be introduced around the _boundaries_ of the input domain. 

Think about it for a moment. If the specification says the user needs to input a password that is between 8-16 (inclusive) characters long where is it most likely that the developer makes an error and introduces a fault?

**Thinking Cap Time**

Take a moment and think of a few password lenghts that would be useful to test with and one that wouldn't likely produce a failure.

Did you come up with testing with passwords of lengths 7, 8, 16, and 17 for being useful and something like 12 as not very helpful?

In case you wanted to see the reason for why this is the case, take a look at the following snippet of code:

```python
verify_pwd(pwd):
	if len(pwd) < 8 or len(pwd) >= 16:
		print("Passwords need to be between 8-16 characters long (inclusive)")
```

If we are being honest with ourselves, we have all made such mental errors when it comes to `<` and `<=`! These are the things our unit tests can help protect us from!


### Time to get our hands dirty!

Now that we have learned about a few approaches to black box testing, it is time to try your hand at writing some tests to identify failures in a piece of code.

Below you will find the specification for `mystery_func` and two sample tests. Your task is to write tests to expose the faults in the implementation. There are two faults in the code but **no peeking!**

#### Specification

This function takes two numbers (a and b). As long as the following conditions are met, the function returns True.
Conditions:

* a<b*b
* a*2>b
* if a<b, then a*3<b

**Hints**: 

* You need to test with both _good_ and _bad_ data. So make sure you are testing with values that should return `False` as well as `True`
* Remember to test the _edge cases_

<iframe height="600px" width="100%" src="https://repl.it/@ericianni/blackbox2?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

#### Solution

When you feel you have written enough tests or have found two failures take a moment and look at the `tests.py` file in the editor above. You will see that the two failures were generated by faults with how the code handles `a<b*b` and `a*2>b`. Again, without looking at `code.py`, think about what simple error the developer could have made to result in these faults?

#### Go ahead and peek!

You have waited long enough! It is time for you to finally look at the code you were testing. Please take a look at `code.py` in the editor above to see the implementation. Did you correctly identify that the issue was similar to the hypothetical password verify discussed in the boundary testing section? If not, that is 100% OK because the more you work with testing, the better you will become at predicting the faults that cause the failures.

### Black Box Testing Wrap-up

So those are the basics of black box testing. There is still much more to learn about such as _Partiition Testing_ and _Model Based Testing_. In a later module you will be learning more about both of these and implementing a simple _Partition Testing_ system.

For now though, we need to move onto the sibling of _Black Box_ testing: _White Box_ testing.

Continue onto [_White Box_ testing](./white_box.md)
