<h1 align="center"><code>Prado</code></h1>
<p align="center">A BF-derivative esoteric programming language.</p>

---
### Intro
Prado (dedicated to [Isabel Lifu](https://github.com/Isabel-Lifu-211207-XPrado)) is an esolang that translates to [BF](https://en.wikipedia.org/wiki/Brainfuck) to be interpreted.

Until Prado is added to Linguist, the `JavaScript` percentage in this Repo represents `Prado`.

### Interpreter (WIP)
`Prado.py` is a WIP Python interpreter for `Windows 10` that translates between Prado, BF and text.

### Dependencies
The interpreter requires the following `Python 3` modules:
```
python -m pip install brainfuck
python -m pip install brainfuck_interpreter
```
(Yes, both are required.)

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

### Contributing

One of the biggest contributions you can give is creating your own Repo containing Prado code, so it can be added to Linguist. Please either Fork this Repo, or make your own code with the interpreter. Thanks!
