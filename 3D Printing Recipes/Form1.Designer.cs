namespace _3D_Printing_Recipes
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pages = new System.Windows.Forms.TabControl();
            this.recipes = new System.Windows.Forms.TabPage();
            this.pg1_lbl_recipeColor = new System.Windows.Forms.Label();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.btn_reloadRecipeList = new System.Windows.Forms.Button();
            this.pg1_lbl_material = new System.Windows.Forms.Label();
            this.pg1_listBox_materials = new System.Windows.Forms.ListBox();
            this.addRecipes = new System.Windows.Forms.TabPage();
            this.numericUpDown3 = new System.Windows.Forms.NumericUpDown();
            this.pg2_lbl_nozzleDiameter = new System.Windows.Forms.Label();
            this.pg2_lbl_temperature = new System.Windows.Forms.Label();
            this.numericUpDown2 = new System.Windows.Forms.NumericUpDown();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.label8 = new System.Windows.Forms.Label();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.addMaterial = new System.Windows.Forms.TabPage();
            this.label6 = new System.Windows.Forms.Label();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.pg3_lbl_materialName = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.pages.SuspendLayout();
            this.recipes.SuspendLayout();
            this.addRecipes.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            this.addMaterial.SuspendLayout();
            this.SuspendLayout();
            // 
            // pages
            // 
            this.pages.Controls.Add(this.recipes);
            this.pages.Controls.Add(this.addRecipes);
            this.pages.Controls.Add(this.addMaterial);
            this.pages.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pages.Dock = System.Windows.Forms.DockStyle.Top;
            this.pages.HotTrack = true;
            this.pages.Location = new System.Drawing.Point(0, 0);
            this.pages.Name = "pages";
            this.pages.SelectedIndex = 0;
            this.pages.Size = new System.Drawing.Size(384, 400);
            this.pages.TabIndex = 0;
            // 
            // recipes
            // 
            this.recipes.Controls.Add(this.pg1_lbl_recipeColor);
            this.recipes.Controls.Add(this.comboBox2);
            this.recipes.Controls.Add(this.btn_reloadRecipeList);
            this.recipes.Controls.Add(this.pg1_lbl_material);
            this.recipes.Controls.Add(this.pg1_listBox_materials);
            this.recipes.Location = new System.Drawing.Point(4, 24);
            this.recipes.Name = "recipes";
            this.recipes.Padding = new System.Windows.Forms.Padding(3);
            this.recipes.Size = new System.Drawing.Size(376, 372);
            this.recipes.TabIndex = 0;
            this.recipes.Text = "Current Recipes";
            this.recipes.UseVisualStyleBackColor = true;
            this.recipes.Click += new System.EventHandler(this.tabPage1_Click);
            // 
            // pg1_lbl_recipeColor
            // 
            this.pg1_lbl_recipeColor.AutoSize = true;
            this.pg1_lbl_recipeColor.Location = new System.Drawing.Point(25, 117);
            this.pg1_lbl_recipeColor.Name = "pg1_lbl_recipeColor";
            this.pg1_lbl_recipeColor.Size = new System.Drawing.Size(38, 15);
            this.pg1_lbl_recipeColor.TabIndex = 4;
            this.pg1_lbl_recipeColor.Text = "label9";
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Location = new System.Drawing.Point(94, 105);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(274, 23);
            this.comboBox2.TabIndex = 3;
            // 
            // btn_reloadRecipeList
            // 
            this.btn_reloadRecipeList.Location = new System.Drawing.Point(251, 76);
            this.btn_reloadRecipeList.Name = "btn_reloadRecipeList";
            this.btn_reloadRecipeList.Size = new System.Drawing.Size(117, 23);
            this.btn_reloadRecipeList.TabIndex = 2;
            this.btn_reloadRecipeList.Text = "Reload Recipe List";
            this.btn_reloadRecipeList.UseVisualStyleBackColor = true;
            // 
            // pg1_lbl_material
            // 
            this.pg1_lbl_material.AutoSize = true;
            this.pg1_lbl_material.Location = new System.Drawing.Point(8, 6);
            this.pg1_lbl_material.Name = "pg1_lbl_material";
            this.pg1_lbl_material.Size = new System.Drawing.Size(50, 15);
            this.pg1_lbl_material.TabIndex = 1;
            this.pg1_lbl_material.Text = "Material";
            // 
            // pg1_listBox_materials
            // 
            this.pg1_listBox_materials.FormattingEnabled = true;
            this.pg1_listBox_materials.ItemHeight = 15;
            this.pg1_listBox_materials.Location = new System.Drawing.Point(94, 6);
            this.pg1_listBox_materials.Name = "pg1_listBox_materials";
            this.pg1_listBox_materials.Size = new System.Drawing.Size(274, 64);
            this.pg1_listBox_materials.TabIndex = 0;
            this.pg1_listBox_materials.SelectedIndexChanged += new System.EventHandler(this.pg1_listBox_materials_SelectedIndexChanged);
            // 
            // addRecipes
            // 
            this.addRecipes.Controls.Add(this.numericUpDown3);
            this.addRecipes.Controls.Add(this.pg2_lbl_nozzleDiameter);
            this.addRecipes.Controls.Add(this.pg2_lbl_temperature);
            this.addRecipes.Controls.Add(this.numericUpDown2);
            this.addRecipes.Controls.Add(this.button2);
            this.addRecipes.Controls.Add(this.button1);
            this.addRecipes.Controls.Add(this.label8);
            this.addRecipes.Controls.Add(this.comboBox1);
            this.addRecipes.Controls.Add(this.label3);
            this.addRecipes.Controls.Add(this.textBox1);
            this.addRecipes.Controls.Add(this.label2);
            this.addRecipes.Controls.Add(this.numericUpDown1);
            this.addRecipes.Controls.Add(this.label1);
            this.addRecipes.Controls.Add(this.listBox1);
            this.addRecipes.Controls.Add(this.progressBar1);
            this.addRecipes.Location = new System.Drawing.Point(4, 24);
            this.addRecipes.Name = "addRecipes";
            this.addRecipes.Padding = new System.Windows.Forms.Padding(3);
            this.addRecipes.Size = new System.Drawing.Size(376, 372);
            this.addRecipes.TabIndex = 1;
            this.addRecipes.Text = "Add Recipe";
            this.addRecipes.UseVisualStyleBackColor = true;
            // 
            // numericUpDown3
            // 
            this.numericUpDown3.DecimalPlaces = 2;
            this.numericUpDown3.Increment = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            this.numericUpDown3.Location = new System.Drawing.Point(106, 162);
            this.numericUpDown3.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.numericUpDown3.Name = "numericUpDown3";
            this.numericUpDown3.Size = new System.Drawing.Size(253, 23);
            this.numericUpDown3.TabIndex = 107;
            this.numericUpDown3.Value = new decimal(new int[] {
            5,
            0,
            0,
            65536});
            // 
            // pg2_lbl_nozzleDiameter
            // 
            this.pg2_lbl_nozzleDiameter.AutoSize = true;
            this.pg2_lbl_nozzleDiameter.Location = new System.Drawing.Point(8, 164);
            this.pg2_lbl_nozzleDiameter.Name = "pg2_lbl_nozzleDiameter";
            this.pg2_lbl_nozzleDiameter.Size = new System.Drawing.Size(93, 15);
            this.pg2_lbl_nozzleDiameter.TabIndex = 106;
            this.pg2_lbl_nozzleDiameter.Text = "Nozzle Diameter";
            // 
            // pg2_lbl_temperature
            // 
            this.pg2_lbl_temperature.AutoSize = true;
            this.pg2_lbl_temperature.Location = new System.Drawing.Point(8, 106);
            this.pg2_lbl_temperature.Name = "pg2_lbl_temperature";
            this.pg2_lbl_temperature.Size = new System.Drawing.Size(92, 15);
            this.pg2_lbl_temperature.TabIndex = 105;
            this.pg2_lbl_temperature.Text = "Temperature (C)";
            // 
            // numericUpDown2
            // 
            this.numericUpDown2.Location = new System.Drawing.Point(106, 104);
            this.numericUpDown2.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDown2.Name = "numericUpDown2";
            this.numericUpDown2.Size = new System.Drawing.Size(253, 23);
            this.numericUpDown2.TabIndex = 104;
            this.numericUpDown2.Value = new decimal(new int[] {
            150,
            0,
            0,
            0});
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(221, 313);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(138, 23);
            this.button2.TabIndex = 103;
            this.button2.Text = "Add and Start New";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(8, 313);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(138, 23);
            this.button1.TabIndex = 102;
            this.button1.Text = "Add Recipe";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(8, 136);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(79, 15);
            this.label8.TabIndex = 101;
            this.label8.Text = "Quality Grade";
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "High",
            "Medium High",
            "Medium",
            "Medium Low",
            "Low"});
            this.comboBox1.Location = new System.Drawing.Point(92, 133);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(267, 23);
            this.comboBox1.TabIndex = 100;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(8, 46);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(36, 15);
            this.label3.TabIndex = 99;
            this.label3.Text = "Color";
            this.label3.Click += new System.EventHandler(this.label3_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(50, 46);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(309, 23);
            this.textBox1.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(8, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(43, 15);
            this.label2.TabIndex = 99;
            this.label2.Text = "Infill %";
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.Location = new System.Drawing.Point(64, 75);
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(295, 23);
            this.numericUpDown1.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(8, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(50, 15);
            this.label1.TabIndex = 99;
            this.label1.Text = "Material";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 15;
            this.listBox1.Location = new System.Drawing.Point(64, 6);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(295, 34);
            this.listBox1.TabIndex = 1;
            this.listBox1.Tag = "material";
            this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(8, 342);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(360, 30);
            this.progressBar1.TabIndex = 0;
            // 
            // addMaterial
            // 
            this.addMaterial.Controls.Add(this.label6);
            this.addMaterial.Controls.Add(this.textBox4);
            this.addMaterial.Controls.Add(this.label5);
            this.addMaterial.Controls.Add(this.textBox3);
            this.addMaterial.Controls.Add(this.pg3_lbl_materialName);
            this.addMaterial.Controls.Add(this.textBox2);
            this.addMaterial.Location = new System.Drawing.Point(4, 24);
            this.addMaterial.Name = "addMaterial";
            this.addMaterial.Padding = new System.Windows.Forms.Padding(3);
            this.addMaterial.Size = new System.Drawing.Size(376, 372);
            this.addMaterial.TabIndex = 2;
            this.addMaterial.Text = "Add Material";
            this.addMaterial.UseVisualStyleBackColor = true;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(8, 64);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(116, 15);
            this.label6.TabIndex = 105;
            this.label6.Text = "Cost per Gram (USD)";
            // 
            // textBox4
            // 
            this.textBox4.Location = new System.Drawing.Point(130, 61);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(229, 23);
            this.textBox4.TabIndex = 104;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(8, 35);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(47, 15);
            this.label5.TabIndex = 103;
            this.label5.Text = "Vendor:";
            this.label5.Click += new System.EventHandler(this.label5_Click);
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(102, 32);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(257, 23);
            this.textBox3.TabIndex = 102;
            // 
            // pg3_lbl_materialName
            // 
            this.pg3_lbl_materialName.AutoSize = true;
            this.pg3_lbl_materialName.Location = new System.Drawing.Point(8, 3);
            this.pg3_lbl_materialName.Name = "pg3_lbl_materialName";
            this.pg3_lbl_materialName.Size = new System.Drawing.Size(88, 15);
            this.pg3_lbl_materialName.TabIndex = 101;
            this.pg3_lbl_materialName.Text = "Material Name:";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(102, 3);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(257, 23);
            this.textBox2.TabIndex = 100;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(384, 461);
            this.Controls.Add(this.pages);
            this.Name = "Form1";
            this.Text = "Form1";
            this.pages.ResumeLayout(false);
            this.recipes.ResumeLayout(false);
            this.recipes.PerformLayout();
            this.addRecipes.ResumeLayout(false);
            this.addRecipes.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            this.addMaterial.ResumeLayout(false);
            this.addMaterial.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private TabControl pages;
        private TabPage recipes;
        private TabPage addRecipes;
        private ListBox listBox1;
        private ProgressBar progressBar1;
        private Label label1;
        private Label label3;
        private TextBox textBox1;
        private Label label2;
        private NumericUpDown numericUpDown1;
        private TabPage addMaterial;
        private Label label5;
        private TextBox textBox3;
        private Label pg3_lbl_materialName;
        private TextBox textBox2;
        private Label pg1_lbl_material;
        private ListBox pg1_listBox_materials;
        private Label label8;
        private ComboBox comboBox1;
        private Label label6;
        private TextBox textBox4;
        private Button btn_reloadRecipeList;
        private Button button2;
        private Button button1;
        private Label pg1_lbl_recipeColor;
        private ComboBox comboBox2;
        private NumericUpDown numericUpDown3;
        private Label pg2_lbl_nozzleDiameter;
        private Label pg2_lbl_temperature;
        private NumericUpDown numericUpDown2;
    }
}