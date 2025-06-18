#!/bin/bash

read -p "Enter the number of atoms (nat): " nat
read -p "Enter the dimension (ndim): " ndim
read -p "Enter the number of vectors (nv): " nv
read -p "Choose the initialization method init_algo (1=Golden spiral, 2=Random, 3=Box-Muller): " init_algo
read -p "Choose the optimization method opt_algo (0=none, 1=forces, 2=dot_prod, 3=both): " opt_algo
read -p "Enter the number of steps (nstep_max): " nstep_max

filepos="atomic_positions_${nat}_${ndim}_${init_algo}_${opt_algo}.xyz"
fileout="output_equ_vect_${nat}_${ndim}_${init_algo}_${opt_algo}.xyz"

# Create the file input_variables.dat
echo "$nat"      >input_variables.dat
echo "$ndim"     >>input_variables.dat
echo "$nv"       >>input_variables.dat
echo "$init_algo">>input_variables.dat
echo "$opt_algo" >>input_variables.dat
echo "$nstep_max">>input_variables.dat
echo "$fileout"  >>input_variables.dat
echo "$filepos"  >>input_variables.dat
echo "dummy"     >>input_variables.dat
echo "dummy"     >>input_variables.dat
echo "dummy"     >>input_variables.dat

# Create the atomic positions file
echo "$nat" >"$filepos"
echo ""     >>"$filepos"
for ((j=1; j<=nat; j++)); do
  line="$j"
  for ((i=1; i<=ndim; i++)); do
    line="$line 0.0"
  done
  echo "$line" >>"$filepos"
done

# Run the program
./../../src/exe_main.out

# Rename angles.dat to angles_${nat}_${ndim}_${init_algo}_${opt_algo}.dat if it exists
if [ -f angles.dat ]; then
  mv angles.dat "angles_${nat}_${ndim}_${init_algo}_${opt_algo}.dat"
fi

