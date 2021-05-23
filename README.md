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
$ python3 vython.py main.vy
```
* The scripts' file extension must be ```.vy```

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
## Todo
- [ ] Add ```while``` loops
- [ ] Implement Famous Python Modules(eg. Pandas, Numpy, etc)
- [ ] Make A Website


## License
This Project is [MIT Licensed](https://github.com/cvython/Vython/blob/main/LICENSE)

