package com.caddickbrown.algorithmic

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log.d
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.widget.TextView
import kotlinx.android.synthetic.main.fragment_first.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.fragment_first)
        setSupportActionBar(findViewById(R.id.toolbar))

        GoToAddProduct.setOnClickListener {
            startActivity(Intent(this,AddProductActivity::class.java))
        }

        val preferences = getSharedPreferences("Database", Context.MODE_PRIVATE)
        val savedname = preferences.getString("SavedProductName","No Value")
        d("daniel", "saved message is: $savedname")

        LastSavedProduct.text = savedname
    }

}