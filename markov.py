def generate_pn_sequence(initial_values):
  """Generates a pseudo-random code sequence using the m-sequence generator.
  Args:
    initial_values: A list of two initial values.
  Returns:
    A list of pseudo-random code sequence.
  """
  pn_sequence = []
  a1 = initial_values[0]
  a2 = initial_values[1]
  while True:
    shifted_a1 = a1 >> 1
    shifted_a2 = a2 >> 1
    next_bit = a1 ^ shifted_a2
    pn_sequence.append(next_bit)
    a1 = shifted_a1
    a2 = shifted_a2
    if a1 == 0 and a2 == 0:
      break
  return pn_sequence
# Compute the PN sequences PN1 and PN2 for initial values of 001 and 101, respectively.
pn1 = generate_pn_sequence([0, 0, 1])
pn2 = generate_pn_sequence([1, 0, 1])
# Print the PN sequences.
print("PN1:", pn1)
print("PN2:", pn2)

#output
PN1:[0]
PN2:[1]
