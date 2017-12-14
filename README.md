# Unit-converter
This project aims at creating a convenient (energy) unit converter application that physical scientists will find easy to use

## Introduction
When scientists are dealing with atoms and molecules, they don't use "Macro" units like, *lb* or *oz*, they use "Micro" units such as the celebrated **eV**(electron volt). Why? Because that way they don't have to worry about all the "nasty" pre-factor constants, and don't have to convert back and forth from *kg*, *s* all the time, which makes life much simpler. It might also just be more "intuitive" to scientists and when young researchers enter into the fields they just adopt the convention. 

Nonetheless, even when all the units are conveniently boiled down to be measured with the concept of **energy** in mind, the difference between spectral experimentalists (who often use *cm* inverse) and electronic structure physicists (who mostly use *eV* apparently) in terms of preference of units are not so straightforward. Therefore it will be helpful to young researchers (like myself) to give a brief summary of the relations of all these units, and useful if some tiny "converter" utility is developed to make everybody's life happy and productive.

## Technical details
First of all, so far (till Dec-13-17 EST) only one converter is built, with *Python*, specifically targets for energy
converting. Because as I am concerned, other units such as length, time, are trivial. The energy units are a little more
complex and more heavily used in the realm of atomic and molecular sciences. Of course, other converters can be
constructed, but one may be enough for this time.

There is [excellent online converter](http://halas.rice.edu/conversions) already existed online for free. But sadly they
don't have termal units (i.e. kT), so this code can be used a complementary tool to that and download for offline usage
of course.

*Python2.7* is used in the code, so if your interpreter is version 3+, then it might run into some trouble. But
converting it to *Python3* should be pretty simple since there are just small different (like *print* syntax) involved
here and *Python* has its intrinsic utility to do the conversion on-the-fly.

If you find any bugs or additional requests to a better version. Please kindly let me know.

## Usage
Just run the *Python* source code `unit-converter.py` and input the unit you want to convert from, the amount, and the
unit you want to convert to, it should give you the number up to a certain decimal points.

## Disclaimer
You are free to fork, download, distribute this code or modify to your own. But the author is not claiming any
responsibility to any potential damage brought by the use of this tool, the user should discern by him or her self
alone.
