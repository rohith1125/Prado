<h1 align="center"><code>Prado</code></h1>
<h6 align="center">A BF-derivative esoteric programming language.</h6>

---
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

Where _n_ is the amount of `+`s or `-`s, and multiple `x`s or `y`s are given the power of their length. For example:

```
>++++[>>++++++++<<-]>++[>---<-]>
```
Becomes:

<pre>
x+4(x<sup>2</sup>+8y<sup>2</sup>-1)x+2(x-3y-1)x
</pre>

Optional: `x` or `y` directly followed by a numeral indicates an exponent.

### `Hello World!` in Prado

In BF, the following program outputs "`Hello World!`":
```
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

<pre>
[Q1]: 8(x+9y-1) x
=y+10(x+3y-1) x-1
=y+2(x+3y-1) x+1
=xy
=3
=y+4(x2+8y2-1) x2
=y2+2(x+4y-1) x
=y+2(x-4y-1) x
=3
=y+2(x-3y-1) x
=y+2(x-4y-1) x
=x+1
</pre>

### Interpreter (WIP)
Prado needs a Python interpreter to scan a `.pdn` file and convert it to BF. This is currently a work in progress, saved as the `Prado.py` file in this Repo.
