package main;

import modelo.Apartamento;
import modelo.Casa;
import modelo.Terreno;
import util.InterfaceUsuario;

import modelo.Financiamento;

import  java.util.ArrayList;

import java.util.List;

public class Main {

    public static void main(String[] args) {


        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        List<Financiamento> ListaDeFinaciamento = new ArrayList<Financiamento>();

        double taxaJuros = interfaceUsuario.PedirTaxaDeJuros();
        int PrazoFinanciamentoemAnos = interfaceUsuario.PedirPrazoFinanciamento();
        double ValorImovel = interfaceUsuario.PedirvalorImovel();


        ListaDeFinaciamento.add(new modelo.Terreno(460.000,  480, taxaJuros,250 ));

        ListaDeFinaciamento.add(new modelo.Casa(500.000,  520, taxaJuros, 100.000, 700.0));
        ListaDeFinaciamento.add(new modelo.Casa(520.000,  540, taxaJuros ,100.000, 700.0));

        ListaDeFinaciamento.add(new modelo.Apartamento(600.000,620, taxaJuros,  10, 20  ));
        ListaDeFinaciamento.add(new modelo.Apartamento(620.000,640, taxaJuros,11, 21 ));


        }
            }



