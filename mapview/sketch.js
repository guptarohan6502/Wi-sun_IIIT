let table;
function preload() {
      table = loadTable("assets/data.csv", "csv", "header");
      Name_table = loadTable("assets/names.csv", "csv", "header");
      //   loc_table = loadTable("");
}

function setup() {
      createCanvas(1550, 740);
      console.log(width, height);
      background(220);

      freq_Table = new p5.Table();
      freq_Table.addColumn("Nodes");
      freq_Table.addColumn("freq");
      freq_Table.addColumn("Time");
      freq_Table.addColumn("x");
      freq_Table.addColumn("y");
      freq_Table.addColumn("radius");
      freq_Table.addColumn("F_color1");
      freq_Table.addColumn("F_color2");
      freq_Table.addColumn("F_color3");
      freq_Table.addColumn("T_color1");
      freq_Table.addColumn("T_color2");
      freq_Table.addColumn("T_color3");

      for (let r = 0; r < table.getRowCount(); r++) {
            Node_data = table.getRow(r);
            find_node1 = Name_table.findRow(Node_data.get("From"), "Node_id");
            find_node2 = Name_table.findRow(Node_data.get("To"), "Mac_add");
            node1_time = Node_data.get("Time");
            if (find_node1) {
                  pole_name = find_node1.get("Name");
                  Node_data.set("From", pole_name);
            }

            if (find_node2) {
                  pole_name = find_node2.get("Name");
                  Node_data.set("To", pole_name);
            }
      }
      console.log(table);
      for (let r = 0; r < table.getRowCount(); r++) {
            node_Row = table.getRow(r);
            console.log(node_Row)
            var nodes = node_Row.get("To");
            var timez = node_Row.get("Time")
            console.log(nodes,timez);
            //table.getString(r, "From");
            Nodes_location = Name_table.getRow(r);
            find_node = freq_Table.findRow(nodes, "Nodes");

            if (find_node) {
                  frequency = find_node.get("freq");
                  find_node.set("freq", frequency + 1);
                  console.log(find_node.get("freq"));
            } else {
                  let newRow = freq_Table.addRow();
                  newRow.setString("Nodes", nodes);
                  newRow.set("freq", 1);
                  newRow.set("Time",timez)
                  newRow.set("x", random(0, width - 50));
                  newRow.set("y", random(0, height - 50));
                  newRow.set("radius", 25);
                  newRow.set("T_color1", random(255));
                  newRow.set("T_color2", random(255));
                  newRow.set("T_color3", random(255));
                  newRow.set("F_color1", random(255));
                  newRow.set("F_color2", random(255));
                  newRow.set("F_color3", random(255));
            }

            var nodes = node_Row.get("From");
            var timez = node_Row.get("Time") //table.getString(r, "To");
            find_node = freq_Table.findRow(nodes, "Nodes");

            if (find_node) {
                  frequency = find_node.get("freq");
                  find_node.set("freq", frequency + 1);
                  console.log(find_node.get("freq"));
            } else {
                  let newRow = freq_Table.addRow();
                  From_node = freq_Table.findRow(node_Row.get("To"), "Nodes");
                  newRow.setString("Nodes", nodes);
                  newRow.set("freq", 1);
                  newRow.set("Time",timez)
                  newRow.set("x", random(0, width - 50));
                  newRow.set("y", random(0, height - 50));
                  newRow.set("radius", 25);
                  newRow.set("T_color1", From_node.getNum("F_color1"));
                  newRow.set("T_color2", From_node.getNum("F_color2"));
                  newRow.set("T_color3", From_node.getNum("F_color3"));
                  newRow.set("F_color1", random(255));
                  newRow.set("F_color2", random(255));
                  newRow.set("F_color3", random(255));
                  console.log(newRow, From_node);
            }
      }

      for (let r = 0; r < Name_table.getRowCount(); r++) {
            node_Row = Name_table.getRow(r);
            console.log(node_Row)
            var nodes = node_Row.get("Name");
            console.log(nodes);
            //table.getString(r, "From");
            Nodes_location = Name_table.getRow(r);
            find_node = freq_Table.findRow(nodes, "Nodes");

            if (find_node) {
                 continue
            } else {
                  let newRow = freq_Table.addRow();
                  newRow.setString("Nodes", nodes);
                  newRow.set("freq", 1);
                  newRow.set("x", random(0, width - 50));
                  newRow.set("y", random(0, height - 50));
                  newRow.set("radius", 25);
                  newRow.set("T_color1",128);
                  newRow.set("T_color2",128);
                  newRow.set("T_color3", 128);
                  newRow.set("F_color1", random(255));
                  newRow.set("F_color2",  random(255));
                  newRow.set("F_color3", random(255));
            }

           
      }
      console.log(freq_Table);

      for (let r = 0; r < freq_Table.getRowCount(); r++) {
            freq_table_node = freq_Table.getRow(r);
            Nodes_location = Name_table.findRow(
                  freq_table_node.get("Nodes"),
                  "Name"
            );
            const frequency = freq_Table.getNum(r, "freq");
            freq_Table.set(r, "radius", map(frequency, 1, 5, 50, 80));
            radius = freq_Table.get(r, "radius");
            if (Nodes_location) {
                  x_loc = Nodes_location.getNum("x"); //* 1000000;
                  y_loc = Nodes_location.getNum("y"); //* 1000000;
                  map_y_loc = x_loc; //map(y_loc, 78348000, 78351000, 0, height - 50);
                  map_x_loc = y_loc; //map(x_loc, 17444000, 17447000, 0, width - 50);
            } else {
                  map_x_loc = random(50, width - 50);
                  map_y_loc = random(50, height - 50);
                  freq_Table.set(r, "x", map_x_loc);
                  freq_Table.set(r, "y", map_y_loc);
            }

            // console.log(
            //       Nodes_location.get("Name"),
            //       x_loc,
            //       map_x_loc,
            //       y_loc,
            //       map(y_loc, 78348000, 78351000, 0, height - 50)
            // );
            freq_Table.set(r, "x", map_x_loc);
            freq_Table.set(r, "y", map_y_loc);

            for (var j = 0; j < r; j++) {
                  var other = freq_Table.getRow(j);
                  var circles = freq_Table.getRow(r);
                  var d = dist(
                        circles.get("x"),
                        circles.get("y"),
                        other.get("x"),
                        other.get("y")
                  );

                  // while (d < circles.get("radius") + other.get("radius")) {
                  //       console.log(circles.get("Nodes"));
                  //       change_y = circles.get("y");
                  //       change_y -= 1;
                  //       circles.set("y", change_y);
                  //       d = dist(
                  //             circles.get("x"),
                  //             circles.get("y"),
                  //             other.get("x"),
                  //             other.get("y")
                  //       );
                  // }
                  change_y = circles.get("y");
                  while (
                        2 * d <
                        circles.getNum("radius") + other.getNum("radius") + 20
                  ) {
                        //console.log(circles.get("Nodes"),other.get("Nodes"),d ,circles.get("radius") ,other.get("radius"));
                        change_y -= 1;

                        d = dist(
                              circles.get("x"),
                              change_y,
                              other.get("x"),
                              other.get("y")
                        );
                  }
                  if (change_y > 10 && change_y < height - 50) {
                        circles.set("y", change_y);
                  }
            }
      }

      console.log(freq_Table);
      textAlign(CENTER);
      for (let r = 0; r < table.getRowCount(); r++) {
            from_node = freq_Table.findRow(table.getString(r, "From"), "Nodes");
            to_node = freq_Table.findRow(table.getString(r, "To"), "Nodes");
            timez = table.getString(r, "Time")
            console.log(timez)

            line(
                  from_node.get("x"),
                  from_node.get("y"),
                  to_node.get("x"),
                  to_node.get("y")
            );
            fill(0);
            text(timez,  from_node.get("x"),from_node.get("y") + 50);
      }
      for (let r = 0; r < freq_Table.getRowCount(); r++) {
            wisun_node = freq_Table.getRow(r);
            const name = wisun_node.getString("Nodes");
             //freq_Table.getString(r, "Nodes");
            //console.log(name);
            const frequency = wisun_node.getNum("freq"); //freq_Table.getNum(r, "freq");
            const x = wisun_node.getNum("x"); //freq_Table.getNum(r, "x");
            const y = wisun_node.getNum("y"); //freq_Table.getNum(r, "y");
            radius = wisun_node.getNum("radius"); //freq_Table.get(r, "radius");

            console.log(x);

            console.log(radius);

            // r = random(255); // r is a random number between 0 - 255
            // g = random(100,200); // g is a random number betwen 100 - 200
            // b = random(100); // b is a random number between 0 - 100
            // a = random(200,255); // a is a random number between 200 - 255
            // fill(r, g, b, a);
            fill(
                  wisun_node.getNum("T_color1"),
                  wisun_node.getNum("T_color2"),
                  wisun_node.getNum("T_color3")
            );
            circle(x, y, radius);

            fill(0);
            text(name, x, y);
            
      }
      console.log(freq_Table);
}

function draw() {
      fill(255);
      rect(100, 690, 100, 40, 20);
      fill(0);
      textSize(14);
      text("Main Gate", 150, 715);
      // //circle(0,0,100)
      // //background(220);
      // //rect(10, 20, 30, 40);
      // for (let r = 0; r < table.getRowCount(); r++) {
      //       Node_data = table.getRow(r);
      //       find_node1 = Name_table.findRow(Node_data.get("From"), "Node_id");
      //       find_node2 = Name_table.findRow(Node_data.get("To"), "Mac_add");
      //       if (find_node1) {
      //             pole_name = find_node1.get("Name");
      //             Node_data.set("From", pole_name);
      //       }
      //       if (find_node2) {
      //             pole_name = find_node2.get("Name");
      //             Node_data.set("To", pole_name);
      //       }
      // }
      // for (let r = 0; r < table.getRowCount(); r++) {
      //       from_node = freq_Table.findRow(table.getString(r, "From"), "Nodes");
      //       to_node = freq_Table.findRow(table.getString(r, "To"), "Nodes");
      //       line(
      //             from_node.get("x"),
      //             from_node.get("y"),
      //             to_node.get("x"),
      //             to_node.get("y")
      //       );
      // }
      // for (let r = 0; r < freq_Table.getRowCount(); r++) {
      //       const name = freq_Table.getString(r, "Nodes");
      //       //console.log(name);
      //       const frequency = freq_Table.getNum(r, "freq");
      //       const x = freq_Table.getNum(r, "x");
      //       const y = freq_Table.getNum(r, "y");
      //       radius = freq_Table.get(r, "radius");
      //       color_fill = freq_Table.get(r, "color1");
      //       console.log(x);
      //       console.log(radius);
      //       // r = random(255); // r is a random number between 0 - 255
      //       // g = random(100,200); // g is a random number betwen 100 - 200
      //       // b = random(100); // b is a random number between 0 - 100
      //       // a = random(200,255); // a is a random number between 200 - 255
      //       // fill(r, g, b, a);
      //       //fill(random(255), random(255), random(255));
      //       fill(
      //             freq_Table.get(r, "color1"),
      //             freq_Table.get(r, "color2"),
      //             freq_Table.get(r, "color3")
      //       );
      //       noStroke();
      //       circle(x, y, radius);
      //       fill(0);
      //       text(name, x, y);
      // }
}
