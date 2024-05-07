import math

m_small = 47 / 1000  # kg
m_large = 67 / 1000  # kg
rho = 1.038  # g/cm^3 -> kg/L
c = 3.7  # J/g K -> kJ/kg K
k = 5.4 * 10 ** -3  # W/cm K -> kW/m K
T_w = 100  # C
T_y = 70  # C
T_0_fridge = 4  # C
T_0_room = 20  # C


def calculate_cook_time(mass, original_temp, t_minutes=None):
    global T_0
    if original_temp == 4:
        T_0 = T_0_fridge
    elif original_temp == 20:
        T_0 = T_0_room

    t_seconds = ((mass ** (2 / 3)) * c * (rho ** (1 / 3))) / (
            k * (math.pi ** 2) * ((4 / 3) ** (2 / 3)) * math.log(0.76 * ((T_0 - T_w) / (T_y - T_w))))

    assert isinstance(t_minutes, object)
    return t_seconds, t_minutes


# Calculate cook times for large and small eggs from fridge and room temperature
t_large_fridge_seconds, t_large_fridge_minutes = calculate_cook_time(m_large, 4)
t_large_room_seconds, t_large_room_minutes = calculate_cook_time(m_large, 20)
t_small_fridge_seconds, t_small_fridge_minutes = calculate_cook_time(m_small, 4)
t_small_room_seconds, t_small_room_minutes = calculate_cook_time(m_small, 20)

print(f"Large egg from fridge cook time = {t_large_fridge_seconds:.1f} s = {t_large_fridge_minutes:.1f} min")
print(f"Large egg from room temperature cook time = {t_large_room_seconds:.1f} s = {t_large_room_minutes:.1f} min")
print(f"Small egg from fridge cook time = {t_small_fridge_seconds:.1f} s = {t_small_fridge_minutes:.1f} min")
print(f"Small egg from room temperature cook time = {t_small_room_seconds:.1f} s = {t_small_room_minutes:.1f} min")
