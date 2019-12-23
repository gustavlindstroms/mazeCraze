package sample;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main extends Application {
    private String row = "";
    private int rowCounter = 0;
    private String url = "C:/Users/gusta/OneDrive/Documents/Plenissalen/mazeCraze/maze.csv";
    private int size = 10;

    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void start(Stage primaryStage) {

        Group group = new Group();
        int numberOfRows = this.numberOfRows(url);
        this.readCsv(url, group, numberOfRows);
        Scene scene = new Scene(group, 330, 330);

        primaryStage.setScene(scene);
        primaryStage.show();
    }



    public void readCsv(String pathToCsv, Group gridPane, int rows) {
        try {
            Pane canvas = new Pane();
            canvas.setStyle("-fx-background-color: white");

            int xAxis = 0;
            int yAxis = 0;

            ArrayList<Rectangle> recArr = new ArrayList<Rectangle>();
            BufferedReader csvReader = new BufferedReader(new FileReader(pathToCsv));
            while ((row = csvReader.readLine()) != null) {

                rowCounter++;

                String[] printArray = row.split(",");

                for(int i = 0; i <printArray.length; i++){
                    Rectangle tmp = new Rectangle();
                    tmp.setWidth(size);
                    tmp.setHeight(size);
                    tmp.setX(xAxis);
                    tmp.setY(yAxis);
                    xAxis += size;
                    if (printArray[i].equals("1")){
                        tmp.setFill(Color.BLACK);
                    }
                    else{
                        tmp.setFill(Color.WHITE);
                    }
                    if(xAxis == (rows * size)){
                        yAxis += size;
                        xAxis = 0;
                    }
                    System.out.println(printArray[i]);
                    recArr.add(tmp);
                }
            }
            csvReader.close();
            gridPane.getChildren().addAll(canvas);
            System.out.println(rowCounter);
            for(int i = 0; i < recArr.size(); i++){
                canvas.getChildren().addAll(recArr.get(i));
            }

        } catch (Exception e) {
            e.printStackTrace();

        }

    }

    public int numberOfRows(String urlToCSV){
        try {
            Pane canvas = new Pane();
            canvas.setStyle("-fx-background-color: white");

            int rowTracker = 0;
            int xAxis = 0;
            int yAxis = 0;

            ArrayList<Rectangle> recArr = new ArrayList<Rectangle>();
            BufferedReader csvReader = new BufferedReader(new FileReader(urlToCSV));
            while ((csvReader.readLine()) != null) {
                rowTracker++;
            }
            csvReader.close();
            System.out.println(rowTracker);
            if(rowTracker != 0){
                return rowTracker;
            }
            else{
                int r = 0;
                return r;
            }


        } catch (Exception e) {
            e.printStackTrace();
            int r = 0;
            return r;

        }
    }
}