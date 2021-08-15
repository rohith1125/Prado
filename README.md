<p align="center">
  <img src="Logo.png" align="center" width="25%">
</p>
<h1 align="center">Prado</h1>
<p align="center">A BF-derivative esoteric programming language.</p>

---
### Intro
Prado (dedicated to [Isabel Lifu](https://github.com/Isabel-Lifu-211207-XPrado)) is an esolang that translates to [BF](https://en.wikipedia.org/wiki/Brainfuck) to be interpreted. Prado files have the `.pdn` extension.

Until Prado is added to Linguist, the `JavaScript` percentage in this Repo represents `Prado`, whose Linguist colour will be `#d0a92c` (gold).

### Interpreter
`Prado.py` is a Python 3 interpreter for `Windows 10` that translates between Prado, BF and text.

The text-to-BF (and therefore text-to-Prado) functionality is thanks to [this `Stack Exchange` post](https://codereview.stackexchange.com/questions/179492/text-to-brainfuck-translator). Long texts may take a while to encode and decode, but it should get there eventually. Probably.

Please note that text-to-BF and text-to-Prado are not optimised. Maybe Prado should be added to [Code Golf](https://code.golf)!

Also, please remove comments from BF/Prado code before running. The interpreter currently fails to convert invalid BF/Prado characters. This will likely not be addressed.

If you encounter any problems with the interpreter, please create an [Issue](https://github.com/TurnipGuy30/Prado/issues/new).

### Dependencies
The interpreter requires the following `Python 3` modules:
```
python -m pip install brainfuck
python -m pip install brainfuck_interpreter
```

### Key
BF | Prado
--- | ---
`>` | x
`<` | y
`+` | _n_
`-` | -_n_
`.` | =
`,` | z
`[` | (
`]` | )

Where _n_ is the amount of `+`s or `-`s, and multiple `x`s or `y`s are given the power of their length. `x` or `y` directly followed by a numeral indicates an exponent. For example:
```brainfuck
>++++[>>++++++++<<-]>++[>---<-]>
```
Becomes:
```
x+4(x2+8y2-1)x+2(x-3y-1)x
```
If you don't understand, try out the text-to-Prado translator.

### `Hello world!` in Prado
In BF, the following program outputs "`Hello world!`":
```brainfuck
++++++++[>+++++++++<-]>.
<++++++++++[>+++<-]>-.
<++[>+++<-]>+.
.
+++.
<++++[>>++++++++<<-]>>.
<<++[>++++<-]>.
<++[>----<-]>.
+++.
<++[>---<-]>.
<++[>----<-]>.
>+.
```
This can be translated into Prado as:
```
8(x+9y-1)x
=y+10(x+3y-1)x-1
=y+2(x+3y-1)x+1
=xy
=3
=y+4(x2+8y2-1)x2
=y2+2(x+4y-1)x
=y+2(x-4y-1)x
=3
=y+2(x-3y-1)x
=y+2(x-4y-1)x
=x+1
=xy
```
More examples like this can be found in [the `/examples` directory](https://github.com/TurnipGuy30/Prado/tree/main/examples).

### Contributing
One of the biggest contributions you can give is creating your own Repository containing Prado code, so it can be added to Linguist. Please either Fork this Repository, or make your own code with the interpreter. Thanks!
