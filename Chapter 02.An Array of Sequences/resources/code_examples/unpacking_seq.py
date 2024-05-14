# Unpacking with parallel assignment
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # unpacking
print(latitude, longitude)

## We can use the parallel assignment unpacking in swapping two variables with using a temp one.
latitude, longitude = longitude, latitude
print(latitude, longitude)

