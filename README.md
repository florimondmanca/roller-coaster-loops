# Roller coaster loops

Compute the shape of roller coaster loops.

## Requirements

This program should work on Python 2.7.x and 3.x.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```
python main.py [C1, C2, ...]
```

## Example

```
python main.py 2 3 4 5
```

![](loops.png)

## Derivation

> The derivation of equations is based on [1]. Scipy's default non-linear ODE solver is used instead of Euler's method.

The loop shape is computed so that the centripetal force `a_c` stays constant along the track segment:

```python
a_c = C * g  # (1)
```

where `C` is a non-dimensional parameter.

We then derive the expression of the radius `r` along the track section.

The centripetal acceleration is commonly express as:

```python
a_c = v ** 2 / r  # (2)
```

Using (1) and (2) we get:

```python
r = v ** 2 / (G * g)  # (3)
```

But the conservation of energy gives us:

```python
v ** 2 = v_0 ** 2 - 2 * g * y
```

And so:

```python
r = 1 / C * (v_0 ** 2 / g - 2 * y)
```

The relationship between `r` the curvilinear abscissa `s` is:

```python
∂Θ/∂s = 1/r
```

Besides, `s` can be related to the abscissa `x` and the height `y` of a given point of the track section using:

```python
∂x/∂s = cos(Θ)
∂y/∂s = sin(Θ)
```

This allows us to write the final system of non-linear ODEs:

```python
∂Θ/∂s = C / (v_0 ** 2 / g - 2 * y)
∂x/∂s = cos(Θ)
∂y/∂s = sin(Θ)
```

This system can be rewritten as

```python
dZ/ds = f(s, Z)
```

where `Z = (Θ x y)` and:

```python
f(s, Z) = (C / (v_0 ** 2 / g - 2 * Z[2]), cos(Z[0]), sin(Z[1]))
```

We use this expression to integrate the system of ODEs using [`scipy.integrate.ode`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html). The final results are dislayed using `matplotlib`.

## Bibliography

[1]: Art of Engineering, [The Real Physics Of A Roller Coaster](https://www.youtube.com/watch?v=4q2W5SJc5j4), published 2019-05-09.
