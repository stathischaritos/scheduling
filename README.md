Intro
-----
N companies with a preference list P_i
want to meet with M investors without preference.
We have time T and each meeting takes T/(N*M)

example.

We have 5 investors [ I_1, I_2, I_3, I_4, I_5 ]
and 6 companies [
  ( C_1, P_1 ),
  ( C_2, P_2 ),
  ( C_3, P_3 ),
  ( C_4, P_4 ),
  ( C_5, P_5 ),
  ( C_6, P_6 )
]
Where
P_1 = [ I_2, I_1, I_4, I_3, I_5 ]
P_2 = [ I_1, I_4, I_2, I_3, I_5 ]
P_3 = [ I_5, I_2, I_1, I_3, I_4 ]
P_4 = [ I_2, I_1, I_3, I_5, I_4 ]
P_5 = [ I_1, I_3, I_4, I_2, I_5 ]
P_6 = [ I_4, I_2, I_5, I_3, I_1 ]

The output is like:

[ S1, S2, S3, S4, S5 ......]

Where S is a session of simultaneous meetings [ (C_1, I_2) , (C_2, I_1) ...]

The loss function is defined as:
cumulative Kendal tau distance between solution and company rankings. (or other ranking distance metric)
cumulative waiting time between meetings for all investors.
cumulative waiting time between meetings for all companies.
