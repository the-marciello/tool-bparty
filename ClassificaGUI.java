import java.util.*;

public class ClassificaGUI{
    private final Map<String, Integer> classifica;

    public ClassificaGUI(){
        classifica = new HashMap<>();
    }

    public void aggiungi(String squadra, int punteggio){
        if(classifica.containsKey(squadra)){
            for (String key : classifica.keySet()) {
                if(squadra.equalsIgnoreCase(key)){
                    int oldValue = classifica.get(key);
                    classifica.put(key, oldValue + punteggio);
                }
            }
        }else{
            classifica.put(squadra, punteggio);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Classifica:\n");
        for (Map.Entry<String, Integer> entry : classifica.entrySet()) {
            sb.append(entry.getKey()).append(": ").append(entry.getValue()).append("\n");
        }
        return sb.toString();
    }

        public static void main(String[] args) {
        ClassificaGUI c = new ClassificaGUI();

        c.aggiungi("squadra 1", 100);
        c.aggiungi("squadra 2", 100);
        c.aggiungi("squadra3", 100);
        c.aggiungi("squadra 4", 100);
        c.aggiungi("squadra 1", 100);
        c.aggiungi("squadra 1", 100);

        System.out.print(c);
    }
}