# Program description

This is a Reddit bot that goes through the top 15 Hot posts of a subreddit and goes through the comments of each post to see 
if any comments mention a certain number of feet(the measurement). If there is such a comment, the bot will reply, to
the comment, with the conversion of feet to meters. This helps Reddit users that are from countries that use the metric 
system.
## Correct format for program
```
... # feet ...
... # ft ...
```

Here '#' means any number in decimal format without a comma


## Examples of valid input
User input #1
```
How many meters is 25 feet?
```

Program output #1
```
25  feet is  82.021  meters
```

User input #2
```
I think the deepest point of the Pacific Ocean is 29000 ft
```

Program output #2
```
29000  feet is  95144.36  meters
```

## Examples of invalid input

```
How many meters is twenty five feet?
I think the deepest point of the Pacific Ocean is 29,000 ft
```

In these cases the program does nothing
