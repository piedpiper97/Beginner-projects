import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class Convertor extends JFrame implements ActionListener{

    // Separate dropdowns for each panel
    JComboBox<String> lengthDropDown;
    JComboBox<String> weightDropDown;
    JComboBox<String> tempDropDown;
    
    JTextField lengthQuery = new JTextField(10);
    JTextField weightQuery = new JTextField(10);
    JTextField tempQuery = new JTextField(10);
    JTextField currencyQuery = new JTextField(10);
    JLabel lengthAnswer = new JLabel();
    JLabel weightAnswer = new JLabel();
    JLabel tempAnswer = new JLabel();
    JTabbedPane tabs;


    public Convertor(){

        setSize(800, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //create tab pane with seperate panels
        tabs = new JTabbedPane();
        JPanel length = createLengthPanel();
        JPanel weight = createWeightPanel();
        JPanel temperature = createTemperaturePanel();
        //add tabs
        tabs.addTab("Length", length);
        tabs.addTab("weight", weight);
        tabs.addTab("temperature", temperature);
        //add tabbedPane to window
        add(tabs);



    }

    private JPanel createLengthPanel(){
        JPanel length = new JPanel();
        length.setLayout(new GridLayout(0, 1));
        //mini panel to store drop down menu in a flow layout
        JPanel choices = new JPanel();
        choices.setLayout(new FlowLayout());
        //types of conversions to be chosen form drop down menu
            String[] conversions = {"meters to km", "inches to cm", "feet to meters"};
            lengthDropDown = new JComboBox <String>(conversions);
            choices.add(new JLabel("Choose type of conversion"));
            choices.add(lengthDropDown);
            //add mini panel to main panel
            length.add(choices);
        //add remaining labels and textfields to get input
                JPanel input = new JPanel();
                input.setLayout(new FlowLayout());
                input.add(new JLabel("Enter length to convert") );
                input.add(lengthQuery);
                length.add(input);
        JButton convert = new JButton("CONVERT");
        convert.addActionListener(this);
        convert.setBackground(Color.CYAN);
        length.add(convert);
        length.add(lengthAnswer );
        
        
        
      

        return length;
    }
    private JPanel createWeightPanel(){
         JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(0, 1));
        //mini panel to store drop down menu in a flow layout
        JPanel choices = new JPanel();
        choices.setLayout(new FlowLayout());
        //types of conversions to be chosen form drop down menu
            String[] conversions = {"ounces to grams", "pounds to kilograms"};
            weightDropDown = new JComboBox <String>(conversions);
            choices.add(new JLabel("Choose type of conversion"));
            choices.add(weightDropDown);
            //add mini panel to main panel
            panel.add(choices);
        //add remaining labels and textfields to get input
                JPanel input = new JPanel();
                input.setLayout(new FlowLayout());
                input.add(new JLabel("Enter weight to convert") );
                input.add(weightQuery);
                panel.add(input);
        JButton convert = new JButton("CONVERT");
        convert.addActionListener(this);
        convert.setBackground(Color.CYAN);
        panel.add(convert);
        panel.add(weightAnswer );
        return panel;
      
    }
    private JPanel createTemperaturePanel(){
         JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(0, 1));
        //mini panel to store drop down menu in a flow layout
        JPanel choices = new JPanel();
        choices.setLayout(new FlowLayout());
        //types of conversions to be chosen form drop down menu
            String[] conversions = {"kelvin to celcius", "fahreheit to celcius", "kelvin to fahrenheight"};
            tempDropDown = new JComboBox <String>(conversions);
            choices.add(new JLabel("Choose type of conversion"));
            choices.add(tempDropDown);
            //add mini panel to main panel
            panel.add(choices);
        //add remaining labels and textfields to get input
                JPanel input = new JPanel();
                input.setLayout(new FlowLayout());
                input.add(new JLabel("Enter temperature to convert") );
                input.add(tempQuery);
                panel.add(input);
        JButton convert = new JButton("CONVERT");
        convert.addActionListener(this);
        convert.setBackground(Color.CYAN);
        panel.add(convert);
        panel.add(tempAnswer );
        return panel;
    }
    


    //actionlistener
    public void actionPerformed(ActionEvent e){
        int selectedTab = tabs.getSelectedIndex();
        String selected;
        double multiplier = 1.0;
        String query;
        double value;
        double result;
        String formattedResult;
        
        // Determine which tab is active and get the appropriate dropdown selection
        if (selectedTab == 0) {  // Length tab
            selected = (String) lengthDropDown.getSelectedItem();
            query = lengthQuery.getText();
            
            if (selected.equals("meters to km")) multiplier = 0.001;
            else if (selected.equals("inches to cm")) multiplier = 2.54;
            else if (selected.equals("feet to meters")) multiplier = 0.3048;
            
            try {
                value = Double.parseDouble(query);
                result = value * multiplier;
                formattedResult = String.format("%.2f", result);
                lengthAnswer.setText(formattedResult);
            } catch (NumberFormatException ex) {
                lengthAnswer.setText("Error. Please enter a valid number.");
            }
        }
        else if (selectedTab == 1) {  // Weight tab
            selected = (String) weightDropDown.getSelectedItem();
            query = weightQuery.getText();
            
            if (selected.equals("ounces to grams")) multiplier = 28.35;
            else if (selected.equals("pounds to kilograms")) multiplier = 0.454;
            
            try {
                value = Double.parseDouble(query);
                result = value * multiplier;
                formattedResult = String.format("%.2f", result);
                weightAnswer.setText(formattedResult);
            } catch (NumberFormatException ex) {
                weightAnswer.setText("Error. Please enter a valid number.");
            }
        }
        else if (selectedTab == 2) {  // Temperature tab
            selected = (String) tempDropDown.getSelectedItem();
            query = tempQuery.getText();
            
            try {
                value = Double.parseDouble(query);
                if (selected.equals("kelvin to celcius")) result = value - 273.15;
                else if (selected.equals("fahreheit to celcius")) result = (value - 32) * 5.0 / 9.0;
                else if (selected.equals("kelvin to fahrenheight")) result = (value - 273.15) * 9.0 / 5.0 + 32;
                else result = value;
                
                formattedResult = String.format("%.2f", result);
                tempAnswer.setText(formattedResult);
            } catch (NumberFormatException ex) {
                tempAnswer.setText("Error. Please enter a valid number.");
            }
        }
    }     

    public static void main(String[] args){
        Convertor convertor = new Convertor();
        convertor.setVisible(true);
    }
    
}
