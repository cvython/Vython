# **Vython** 

## Download & Setup
* Clone the repo from Github:
```
git clone https://github.com/cvython/Vython.git
```
* Enter Into Its Derectory
```
cd Vython
```
* You're All Set!


## Running A Script
```
$ python3 vython.py main.vo
```
* ~~The scripts' file extension must be~~```.vo```
* The scripts' file extension can be anything from ```.txt``` to ```.vo```! Though it is recommended to use the file extension ```.vo```.

## Usage
* Print:
```
show("Hello World")
```
* Take Input:
```
age = enter("Age: ") 
```
* Print Text And Variable:
```
show("Age = "+age) 
```
* If Statements:
```
if a > 18
{
    show("Adult")
}else
{
    show("Child")
}
```
* If Statement With 'and':
```
if a > 18 and a < 50
{
    show("Adult, But Not Old")
}
```
* If Statement With 'or':
```
if a > 18 || a > 16
{
    show("Can Drive")
}
```
* Check If Variable A Particular *Type*:
```
if canbe(a, "int")
{
    show("Variable is an integer")
}
```
* Supported Variable Forms:
    * Integer ➡ int()
    * Float ➡ float()
    * String ➡ str()
    * List ➡ list[]
        * Select Cell From List:
        ```
        a = [0, 1, 2, 3, 4, 5]
        ## Show The First Cell
        show(a[0])
        ```
* Supported Arethmetic Opperations:
    * Addition ➡ '+'
    * Subtraction ➡ '-'
    * Division ➡ '/'
    * Multiplication ➡ '*'
    * Remainder ➡ '%'

## Credits
* [Vedant K](https://github.com/dopevog)
* [Pranav Baburaj](https://github.com/pranavbaburaj)
* [Harry](https://github.com/fineans)

## License
This Project is [MIT Licensed](https://github.com/cvython/Vython/blob/vython/LICENSE)

