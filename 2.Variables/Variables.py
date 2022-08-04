# variables are just containers for values.

# Creating a string variable. Both '' and "" work in Python. 
name = 'John';

print('Hello ' + name);

# We can always find out the type of the variable by printing it out.
print(type(name));

# We can combine variables together if they are of the same type.

first_name = 'Bob';
last_name = 'Johnson';
# Concatinating the two and adding a space.
full_name = first_name + ' ' + last_name;

print(full_name);

age = 21;

# Add 1.
age = age + 1;
# Add 1 again.
age += 1;

print(type(age));
print(age);

# Print a proper sentence by using the integer.
print(f"Your age is {age}");

# Floats
height = 250.5;

print(type(height));
print(f"Your height is {height}cm");

# Boolean - True or Flase.
human = True;

human = False;
print(type(human));
print(f"You are human: {human}");