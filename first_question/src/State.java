public class State {
    public int[] field;
    public String path;
    public int depth;

    public State(int[] field, String path, int depth) {
        this.field = field;
        this.path = path;
        this.depth = depth;
    }
}

