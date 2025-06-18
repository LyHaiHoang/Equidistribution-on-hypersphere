#!/bin/bash

read -p "Enter the number of atoms (nat): " nat
read -p "Enter the dimension (ndim): " ndim
read -p "Enter the number of vectors (nv): " nv

# Loop over initialization methods
for init_algo in 1 2 3; do
  # Loop over optimization methods
  for opt_algo in 0 1 2 3; do
    
    echo "Running with init_algo=$init_algo and opt_algo=$opt_algo"

    filepos="atomic_positions_${nat}_${ndim}_${init_algo}_${opt_algo}.xyz"
    fileout="output_equ_vect_${nat}_${ndim}_${init_algo}_${opt_algo}.xyz"

    # Create input_variables.dat
    echo "$nat"      >input_variables.dat
    echo "$ndim"     >>input_variables.dat
    echo "$nv"       >>input_variables.dat
    echo "$init_algo">>input_variables.dat
    echo "$opt_algo" >>input_variables.dat
    echo "300"      >>input_variables.dat   # You can set nstep_max fixed or ask user once
    echo "$fileout"  >>input_variables.dat
    echo "$filepos"  >>input_variables.dat
    echo "dummy"     >>input_variables.dat
    echo "dummy"     >>input_variables.dat
    echo "dummy"     >>input_variables.dat

    # Create atomic positions file
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

    # Rename angles.dat if it exists
    if [ -f angles.dat ]; then
      mv angles.dat "angles_${nat}_${ndim}_${init_algo}_${opt_algo}.dat"
    fi

  done
done

