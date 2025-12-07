/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.abstraccion.java;
// EJEMPLO DE ABSTRACCIÓN
// La abstracción nos permite definir comportamientos generales
// sin mostrar cómo se implementan exactamente.

abstract class Animal {
    public abstract void hacerSonido();
}

class Perro extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("El perro ladra");
    }
}

public class AbstraccionJava {
    public static void main(String[] args) {
        Animal miPerro = new Perro();
        miPerro.hacerSonido();
    }
}