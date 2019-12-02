| [Module Overview](./unittest_module.md) | [What is Unit Testing](./what_is_unit_testing.md) | [Black Box](./black_box.md) | [White Box](./white_box.md) | [*Debrief*](./debrief.md) |
|-----------------|----------------------|-----------|-----------|---------|
|                 |                      |           |           |         |

### Bringing it all together

Congratulations! That was quite a lot of information to pack into a single module, but we made it through. Let's go over some key points. 

#### Unit Testing

* Unit testing is just a small part of the entire testing process, but it is crucial and something you will most likely have to do in your day-to-day
* A unit test can be done manually, but is usually part of an automated testing suite
* Unit tests can be used in other testing phases (see _regression testing_ below)

#### Black Box Testing

* Based purely on the specifications of the software
* Can implemented by non-technical individuals
* Can't identify what fault caused the failure

#### White Box Testing

* Based purely on the code as written
* Must be implemented by someone familiar with the code
* Can be used to compare test suites' effectiveness

### Additional Musings

**Regression Testing**

Regression testing is a form of testing where you run your test suite regularly as you make changes to the code to ensure you haven't broken any functionality. If we are all honest with ourselves, we know we have spent hours tinkering on a project only to discover it no longer works and we are unsure where the fault is!

**Continuous Integration**

This is an automated process of verifying/testing a developer's code changes before merging it with the central repository. In this way it is similar to regression testing in that strives to prevent faults from being introduced to the codebase that all other developers rely on.

### Video Resources

#### PyCharm Testing Demo


#### Module Material in Video Form!

* All this theoretical knowledge is nice and all, but I am sure you want to see it in action. Please take the time to watch this succinct video demonstration of using some of what we learned in PyCharm, which will be the IDE we use for this course.

  * **Link to a recorded demonstration where I walk the students through how to write tests in PyCharm and use the code coverage analysis tools**
  
* If you are more of a visual learner and would prefer to see some of these concepts covered again, please view these video discussions.

  * **Link to a recorded lecture of me going over black box testing using slides and replit**
  * **Link to a recorded lecture of me going over white box testing using slides and digital white board**
  
  
### Assignments and Quizzes

* Please view this week's assignment (**link to assignment page**) where you will be running through PyCharm's testing functions using the PyCharm Course provided. This is an activity so is based on completion and the instructions walk you through every step of the way.

* You also have a quiz for this week covering the material here (**link to the quiz page**). It is graded for accuracy, but you will have two attempts with the highest score counting.

### Moving Forward

Next week we will be tackling Partition Testing, which is a form of black box testing. We will use some automated software to help us identify tests that need writing, so we aren't just thrashing about wildly.
  
