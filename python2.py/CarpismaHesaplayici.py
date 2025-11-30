import math

def neutron_final_energy(A, theta_deg):
    """
    A: hedef çekirdeğin kütle numarası
    theta_deg: saçılma açısı (derece)
    returns: son nötron enerjisi (MeV)
    """
    E0 = 1.0  # MeV
    theta = math.radians(theta_deg)

    E_ratio = (A**2 + 1 + 2*A*math.cos(theta)) / (A + 1)**2
    E_final = E0 * E_ratio
    return E_final

# Örnek kullanım
A = float(input("Hedef çekirdeğin kütle numarası A: "))
theta = float(input("Saçılma açısı θ (derece): "))

E_final = neutron_final_energy(A, theta)
print(f"Nötronun son enerjisi: {E_final:.6f} MeV")
