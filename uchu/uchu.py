import math

def oklch_to_rgb(oklch_str):
    """
    Convert an OKLCH color string (e.g. "oklch(62.39% 0.181 258.33)")
    to an sRGB hex color string (e.g. "#RRGGBB").

    The OKLCH components are:
      L: lightness in percent (converted to a 0..1 range)
      C: chroma (a float)
      H: hue in degrees
    """
    # Remove the 'oklch(' prefix and trailing ')'
    inner = oklch_str.strip()[6:-1]
    parts = inner.split()
    if len(parts) != 3:
        raise ValueError("Invalid OKLCH format")
    
    # Parse components; L is given as a percentage
    L = float(parts[0].replace('%', '')) / 100.0
    C = float(parts[1])
    H = float(parts[2])
    
    # Convert hue to radians and compute a and b
    H_rad = math.radians(H)
    a = math.cos(H_rad) * C
    b = math.sin(H_rad) * C

    # Convert from Oklab to LMS (see https://bottosson.github.io/posts/oklab/)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b

    # Cube the values
    l_ = l_ ** 3
    m_ = m_ ** 3
    s_ = s_ ** 3

    # Convert LMS to linear sRGB
    r_linear =  4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g_linear = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    b_linear = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_

    # Apply sRGB gamma correction
    def to_srgb(c):
        if c <= 0.0031308:
            return 12.92 * c
        else:
            return 1.055 * (c ** (1/2.4)) - 0.055

    r = to_srgb(r_linear)
    g = to_srgb(g_linear)
    b = to_srgb(b_linear)

    # Clamp the values between 0 and 1
    r = min(max(r, 0), 1)
    g = min(max(g, 0), 1)
    b = min(max(b, 0), 1)

    # Convert to 0-255 and then to a hex string
    r_int = int(round(r * 255))
    g_int = int(round(g * 255))
    b_int = int(round(b * 255))
    return '#{:02x}{:02x}{:02x}'.format(r_int, g_int, b_int)


class uchu:
    # Blue
    blue       = oklch_to_rgb("oklch(62.39% 0.181 258.33)")
    bluedark   = oklch_to_rgb("oklch(43.48% 0.17 260.2)")
    bluelight  = oklch_to_rgb("oklch(89.66% 0.046 260.67)")
    
    # General colors (non-standard names)
    yang       = oklch_to_rgb("oklch(99.4% 0 0)")
    yin         = oklch_to_rgb("oklch(14.38% 0.007 256.88)")
    
    # Gray
    gray       = oklch_to_rgb("oklch(84.68% 0.002 197.12)")
    graydark   = oklch_to_rgb("oklch(63.12% 0.004 219.55)")
    graylight  = oklch_to_rgb("oklch(95.57% 0.003 286.35)")
    
    # Green
    green       = oklch_to_rgb("oklch(79.33% 0.179 145.62)")
    greendark   = oklch_to_rgb("oklch(58.83% 0.158 145.05)")
    greenlight  = oklch_to_rgb("oklch(93.96% 0.05 148.74)")
    
    # Pink
    pink       = oklch_to_rgb("oklch(85.43% 0.09 354.1)")
    pinkdark   = oklch_to_rgb("oklch(64.11% 0.084 353.91)")
    pinklight  = oklch_to_rgb("oklch(95.8% 0.023 354.27)")
    
    # Purple
    purple       = oklch_to_rgb("oklch(58.47% 0.181 302.06)")
    purpledark   = oklch_to_rgb("oklch(39.46% 0.164 298.29)")
    purplelight  = oklch_to_rgb("oklch(89.1% 0.046 305.24)")
    
    # Orange
    orange       = oklch_to_rgb("oklch(78.75% 0.14163582809066333 54.32911089172009)")
    orangedark   = oklch_to_rgb("oklch(58.28% 0.128 52.2)")
    orangelight  = oklch_to_rgb("oklch(93.83% 0.037 56.93)")
    
    # Red
    red        = oklch_to_rgb("oklch(62.73% 0.209 12.37)")
    reddark    = oklch_to_rgb("oklch(45.8% 0.177 17.7)")
    redlight   = oklch_to_rgb("oklch(88.98% 0.052 3.28)")
    
    # Yellow
    yellow       = oklch_to_rgb("oklch(90.92% 0.125 92.56)")
    yellowdark   = oklch_to_rgb("oklch(69.14% 0.109 91.04)")
    yellowlight  = oklch_to_rgb("oklch(97.05% 0.039 91.2)")
    
    # Yin (separate from general)
    yinlight  = oklch_to_rgb("oklch(91.87% 0.003 264.54)")


if __name__ == '__main__':
    # Quick demo: print some of the colors
    print("Red base:", favcolors.red)
    print("Red dark:", favcolors.reddark)
    print("Red light:", favcolors.redlight)
    print("Blue base:", favcolors.blue)
    print("Green base:", favcolors.green)
    print("Yellow base:", favcolors.yellow)
    print("General yang:", favcolors.yang)
    print("General yin:", favcolors.yin)
    print("Yin light:", favcolors.yinlight)
