import sys
import getopt

if __name__ == "__main__":
    argv = sys.argv[1:]
    tempCelsius = None
    tempKelvin = None

    try:
        options, args = getopt.getopt(argv, "t:")
    except Exception as e:
        print(f"Error message! {e}")

    for arg, value in options:
        if arg in ["-t"]:
            tempCelsius = value
            
    tempKelvin = float(274.15) + float(tempCelsius)
               
    print("Input temperature (Celsius):", tempCelsius)
    print("Temp. in (Kelvin):",  tempKelvin)

    # 0 Grad = 273,15 K
    