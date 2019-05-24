# gradients based on http://bsou.io/posts/color-gradients-with-python

def hex_to_RGB(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def RGB_to_hex(RGB):
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    RGB = [int(x) for x in RGB]
    return "#"+"".join(["0{0:x}".format(v) if v < 16 else
                        "{0:x}".format(v) for v in RGB])

def color_dict(gradient):
    ''' Takes in a list of RGB sub-lists and returns dictionary of
      colors in RGB and hex form for use in a graphing function
      defined later on '''
    return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
            "r":[RGB[0] for RGB in gradient],
            "g":[RGB[1] for RGB in gradient],
            "b":[RGB[2] for RGB in gradient]}

def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    ''' returns a gradient list of (n) colors between
      two hex colors. start_hex and finish_hex
      should be the full six-digit color string,
      inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    RGB_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        RGB_list.append(curr_vector)

    return color_dict(RGB_list)


def polylinear_gradient(colors, n):
    ''' returns a list of colors forming linear gradients between
        all sequential pairs of colors. "n" specifies the total
        number of desired output colors '''
    # The number of colors per individual linear gradient
    n_out = int(float(n) / (len(colors) - 1))
    # returns dictionary defined by color_dict()
    gradient_dict = linear_gradient(colors[0], colors[1], n_out)

    if len(colors) > 1:
        for col in range(1, len(colors) - 1):
            next = linear_gradient(colors[col], colors[col+1], n_out)
            for k in ("hex", "r", "g", "b"):
                # Exclude first point to avoid duplicates
                gradient_dict[k] += next[k][1:]

    return gradient_dict

fact_cache = {}
def fact(n):
    ''' Memoized factorial function '''
    try:
        return fact_cache[n]
    except(KeyError):
        if n == 1 or n == 0:
            result = 1
        else:
            result = n*fact(n-1)
        fact_cache[n] = result
        return result


def bernstein(t,n,i):
    ''' Bernstein coefficient '''
    binom = fact(n)/float(fact(i)*fact(n - i))
    return binom*((1-t)**(n-i))*(t**i)


def bezier_gradient(colors, n_out=100):
    ''' Returns a "bezier gradient" dictionary
        using a given list of colors as control
        points. Dictionary also contains control
        colors/points. '''
    # RGB vectors for each color, use as control points
    RGB_list = [hex_to_RGB(color) for color in colors]
    n = len(RGB_list) - 1

    def bezier_interp(t):
        ''' Define an interpolation function
            for this specific curve'''
        # List of all summands
        summands = [
            map(lambda x: int(bernstein(t,n,i)*x), c)
            for i, c in enumerate(RGB_list)
        ]
        # Output color
        out = [0,0,0]
        # Add components of each summand together
        for vector in summands:
            for c in range(3):
                out[c] += vector[c]

        return out

    gradient = [
        bezier_interp(float(t)/(n_out-1))
        for t in range(n_out)
    ]
    # Return all points requested for gradient
    return color_dict(gradient)

fmt = '''
<expression label="{label}" exp="({x}, {y}, {z})" type="point"/>
<element type="point3d" label="{label}">
	<show object="true" label="false" ev="4"/>
	<objColor r="{r}" g="{g}" b="{b}" alpha="0"/>
	<layer val="0"/>
	<labelMode val="0"/>
	<animation step="1" speed="1" type="0" playing="false"/>
	<coords x="{x}" y="{y}" z="{z}" w="1"/>
	<pointSize val="5"/>
</element>
'''
data = '''2	4	5	0	0	0	0
2	4	6	0	0	0	0
2	5	5	0	0	0	0
2	5	6	0	0	0	0
2	6	5	0	0	0	0
2	6	6	0	0	0	0
3	3	6	0	0	0	0
3	4	4	0	0	0	0
3	4	5	0	0	0	0
3	4	6	0	0	0	0
3	5	4	0	0	0	0
3	5	5	0	0	0	0
3	5	6	0	0	0	0
3	6	4	0	0	0	0
3	6	5	0	0	0	0
3	6	6	0	0	0	0
4	3	5	0	0	0	0
4	3	6	0	0	0	0
4	4	4	0	0	0	0
4	4	5	0	0	0	0
4	4	6	0	0	0	0
4	5	4	0	0	0	0
4	5	5	0	0	0	0
4	5	6	0	0	0	0
4	6	4	0	0	0	0
4	6	5	0	0	0	0
4	6	6	0	0	0	0
5	3	5	0	0	0	0
5	3	6	0	0	0	0
5	4	4	0	0	0	0
5	4	5	0	0	0	0
5	4	6	0	0	0	0
5	5	4	0	0	0	0
5	5	5	0	0	0	0
5	5	6	0	0	0	0
5	6	4	0	0	0	0
5	6	5	0	0	0	0
5	6	6	0	0	0	0
5	6	3	0	0	3	3
1	6	6	4	0	0	4
4	6	3	1	0	3	4
5	2	6	0	4	0	4
5	5	3	0	1	3	4
5	6	2	0	0	4	4
0	6	6	5	0	0	5
1	5	6	4	1	0	5
1	6	5	4	0	1	5
2	6	4	3	0	2	5
3	6	3	2	0	3	5
4	2	6	1	4	0	5
4	5	3	1	1	3	5
4	6	2	1	0	4	5
5	1	6	0	5	0	5
5	2	5	0	4	1	5
5	3	4	0	3	2	5
5	4	3	0	2	3	5
5	5	2	0	1	4	5
5	6	1	0	0	5	5
0	5	6	5	1	0	6
0	6	5	5	0	1	6
1	4	6	4	2	0	6
1	5	5	4	1	1	6
1	6	4	4	0	2	6
2	3	6	3	3	0	6
2	5	4	3	1	2	6
2	6	3	3	0	3	6
3	2	6	2	4	0	6
3	3	5	2	3	1	6
3	5	3	2	1	3	6
3	6	2	2	0	4	6
4	1	6	1	5	0	6
4	2	5	1	4	1	6
4	3	4	1	3	2	6
4	4	3	1	2	3	6
4	5	2	1	1	4	6
4	6	1	1	0	5	6
5	0	6	0	6	0	6
5	1	5	0	5	1	6
5	2	4	0	4	2	6
5	3	3	0	3	3	6
5	4	2	0	2	4	6
5	5	1	0	1	5	6
5	6	0	0	0	6	6
0	0	4	3	4	0	7
0	0	5	3	4	0	7
0	0	6	3	4	0	7
0	1	3	3	3	1	7
0	1	4	3	3	1	7
0	1	5	3	4	0	7
0	1	6	3	4	0	7
0	2	2	3	2	2	7
0	2	3	3	2	2	7
0	2	4	3	3	1	7
0	2	5	4	3	0	7
0	2	6	4	3	0	7
0	3	1	3	1	3	7
0	3	2	3	1	3	7
0	3	3	3	2	2	7
0	3	4	4	2	1	7
0	3	5	4	2	1	7
0	3	6	5	2	0	7
0	4	0	3	0	4	7
0	4	1	3	0	4	7
0	4	2	3	1	3	7
0	4	3	4	1	2	7
0	4	4	4	1	2	7
0	4	5	5	1	1	7
0	4	6	5	2	0	7
0	5	0	3	0	4	7
0	5	1	3	0	4	7
0	5	2	4	0	3	7
0	5	3	4	0	3	7
0	5	4	5	0	2	7
0	5	5	5	1	1	7
0	6	0	3	0	4	7
0	6	1	3	0	4	7
0	6	2	4	0	3	7
0	6	3	4	0	3	7
0	6	4	5	0	2	7
1	0	3	2	4	1	7
1	0	4	2	4	1	7
1	0	5	2	5	0	7
1	0	6	2	5	0	7
1	1	2	2	3	2	7
1	1	3	2	3	2	7
1	1	4	2	4	1	7
1	1	5	3	4	0	7
1	1	6	3	4	0	7
1	2	1	2	2	3	7
1	2	2	2	2	3	7
1	2	3	2	3	2	7
1	2	4	3	3	1	7
1	2	5	3	3	1	7
1	2	6	4	3	0	7
1	3	0	2	1	4	7
1	3	1	2	1	4	7
1	3	2	2	2	3	7
1	3	3	3	2	2	7
1	3	4	3	2	2	7
1	3	5	4	2	1	7
1	3	6	4	3	0	7
1	4	0	2	0	5	7
1	4	1	2	1	4	7
1	4	2	3	1	3	7
1	4	3	3	1	3	7
1	4	4	4	1	2	7
1	4	5	4	2	1	7
1	5	0	2	0	5	7
1	5	1	3	0	4	7
1	5	2	3	0	4	7
1	5	3	4	0	3	7
1	5	4	4	1	2	7
1	6	0	2	0	5	7
1	6	1	3	0	4	7
1	6	2	3	0	4	7
1	6	3	4	0	3	7
2	0	2	1	4	2	7
2	0	3	1	4	2	7
2	0	4	1	5	1	7
2	0	5	2	5	0	7
2	0	6	2	5	0	7
2	1	1	1	3	3	7
2	1	2	1	3	3	7
2	1	3	1	4	2	7
2	1	4	2	4	1	7
2	1	5	2	4	1	7
2	1	6	3	4	0	7
2	2	0	1	2	4	7
2	2	1	1	2	4	7
2	2	2	1	3	3	7
2	2	3	2	3	2	7
2	2	4	2	3	2	7
2	2	5	3	3	1	7
2	2	6	3	4	0	7
2	3	0	1	1	5	7
2	3	1	1	2	4	7
2	3	2	2	2	3	7
2	3	3	2	2	3	7
2	3	4	3	2	2	7
2	3	5	3	3	1	7
2	4	0	1	1	5	7
2	4	1	2	1	4	7
2	4	2	2	1	4	7
2	4	3	3	1	3	7
2	4	4	3	2	2	7
2	5	0	2	0	5	7
2	5	1	2	0	5	7
2	5	2	3	0	4	7
2	5	3	3	1	3	7
2	6	0	2	0	5	7
2	6	1	2	0	5	7
2	6	2	3	0	4	7
3	0	1	0	4	3	7
3	0	2	0	4	3	7
3	0	3	0	5	2	7
3	0	4	1	5	1	7
3	0	5	1	5	1	7
3	0	6	2	5	0	7
3	1	0	0	3	4	7
3	1	1	0	3	4	7
3	1	2	0	4	3	7
3	1	3	1	4	2	7
3	1	4	1	4	2	7
3	1	5	2	4	1	7
3	1	6	2	5	0	7
3	2	0	0	2	5	7
3	2	1	0	3	4	7
3	2	2	1	3	3	7
3	2	3	1	3	3	7
3	2	4	2	3	2	7
3	2	5	2	4	1	7
3	3	0	0	2	5	7
3	3	1	1	2	4	7
3	3	2	1	2	4	7
3	3	3	2	2	3	7
3	3	4	2	3	2	7
3	4	0	1	1	5	7
3	4	1	1	1	5	7
3	4	2	2	1	4	7
3	4	3	2	2	3	7
3	5	0	1	0	6	7
3	5	1	2	0	5	7
3	5	2	2	1	4	7
3	6	0	1	0	6	7
3	6	1	2	0	5	7
4	0	1	0	4	3	7
4	0	2	0	4	3	7
4	0	3	0	5	2	7
4	0	4	0	5	2	7
4	0	5	1	5	1	7
4	0	6	1	6	0	7
4	1	0	0	3	4	7
4	1	1	0	3	4	7
4	1	2	0	4	3	7
4	1	3	0	4	3	7
4	1	4	1	4	2	7
4	1	5	1	5	1	7
4	2	0	0	2	5	7
4	2	1	0	3	4	7
4	2	2	0	3	4	7
4	2	3	1	3	3	7
4	2	4	1	4	2	7
4	3	0	0	2	5	7
4	3	1	0	2	5	7
4	3	2	1	2	4	7
4	3	3	1	3	3	7
4	4	0	0	1	6	7
4	4	1	1	1	5	7
4	4	2	1	2	4	7
4	5	0	1	0	6	7
4	5	1	1	1	5	7
4	6	0	1	0	6	7
5	0	1	0	4	3	7
5	0	2	0	4	3	7
5	0	3	0	5	2	7
5	0	4	0	5	2	7
5	0	5	0	6	1	7
5	1	0	0	3	4	7
5	1	1	0	3	4	7
5	1	2	0	4	3	7
5	1	3	0	4	3	7
5	1	4	0	5	2	7
5	2	0	0	2	5	7
5	2	1	0	3	4	7
5	2	2	0	3	4	7
5	2	3	0	4	3	7
5	3	0	0	2	5	7
5	3	1	0	2	5	7
5	3	2	0	3	4	7
5	4	0	0	1	6	7
5	4	1	0	2	5	7
5	5	0	0	1	6	7
5	0	0	0	6	6	12
4	0	0	1	6	6	13
0	0	0	4	5	5	14
0	0	1	4	5	5	14
0	0	2	5	5	4	14
0	0	3	5	6	3	14
0	1	0	4	4	6	14
0	1	1	5	4	5	14
0	1	2	5	5	4	14
0	2	0	5	3	6	14
0	2	1	5	4	5	14
0	3	0	5	3	6	14
1	0	0	3	5	6	14
1	0	1	4	5	5	14
1	0	2	4	6	4	14
1	1	0	4	4	6	14
1	1	1	4	5	5	14
1	2	0	4	4	6	14
2	0	0	3	5	6	14
2	0	1	3	6	5	14
2	1	0	3	5	6	14
3	0	0	2	6	6	14
'''

col = linear_gradient('#00FF00', '#FF0000', 15)

for d in data.split('\n'):
    d = d.strip()
    if not d: continue 
    d = [int(x) for x in d.split('\t')]
    a, e, l, Q, W, E, f = d
    print(fmt.format(label=str(d), x=a, y=e, z=l, r=col['r'][f], g=col['g'][f], b=col['b'][f]))
    