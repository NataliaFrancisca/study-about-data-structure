import java.util.ArrayList;

public class ListaTelefonica {
    public static void main(String[] args) {
        ArrayList<Telefone> listaTelefonica = new ArrayList<>();

        // LISTA ORDENADA PELO NOME
        listaTelefonica.add(new Telefone("Ana", 556060567));
        listaTelefonica.add(new Telefone("Bruno", 552020202));
        listaTelefonica.add(new Telefone("Camila", 553030303));
        listaTelefonica.add(new Telefone("Carlos", 557070678));
        listaTelefonica.add(new Telefone("Eduardo", 552222222));
        listaTelefonica.add(new Telefone("Fernanda", 558080789));
        listaTelefonica.add(new Telefone("Gustavo", 556060606));
        listaTelefonica.add(new Telefone("Isabela", 551111111));
        listaTelefonica.add(new Telefone("João", 555050456));
        listaTelefonica.add(new Telefone("Juliana", 557070707));
        listaTelefonica.add(new Telefone("Laura", 553333333));
        listaTelefonica.add(new Telefone("Lucas", 553030234));
        listaTelefonica.add(new Telefone("Marcel", 559090909));
        listaTelefonica.add(new Telefone("Mariana", 554040345));
        listaTelefonica.add(new Telefone("Mateus", 554040404));
        listaTelefonica.add(new Telefone("Natalia", 552020123));
        listaTelefonica.add(new Telefone("Patrícia", 551010101));
        listaTelefonica.add(new Telefone("Rafael", 558080808));
        listaTelefonica.add(new Telefone("Ricardo", 559090890));
        listaTelefonica.add(new Telefone("Sofia", 555050505));

        // PESQUISA SIMPLES
        String telefoneParaPesquisa = "Rafael";
        int numeroOperacoes = 0;

        for (int i = 0; i < listaTelefonica.size(); i++) {
            String nome = listaTelefonica.get(i).nome;

            if(nome.equals(telefoneParaPesquisa)){
                System.out.println("ACHAMOS NA LISTA SIMPLES :o " + nome);
                break;
            }

            numeroOperacoes++;
        }

        System.out.println("OPERAÇÕES: " + numeroOperacoes);

        // PESQUISA BINARIA
        int numeroOperacoesBinaria = 0;

        int inicioDaLista = 0;
        int finalDaLista = listaTelefonica.size() - 1;

        while(inicioDaLista <= finalDaLista){
            int meioDaLista = (finalDaLista + inicioDaLista) / 2;

            String atual = listaTelefonica.get(meioDaLista).nome;

            if(atual.compareTo(telefoneParaPesquisa) == 0){
                System.out.println("ACHAMOS NA LISTA BINARIA :o " + atual);
                break;
            }
         
            if(atual.compareTo(telefoneParaPesquisa) < 0){
                inicioDaLista = meioDaLista + 1;
            }

            if(atual.compareTo(telefoneParaPesquisa) > 0){
                finalDaLista = meioDaLista - 1;
            }
            
            numeroOperacoesBinaria++;
        }

        System.out.println("OPERAÇÕES BINÁRIA: " + numeroOperacoesBinaria);
    }
}
