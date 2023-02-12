import { Component, OnInit } from '@angular/core';
import { RecipeService } from '../service/recipe/recipe.service';

@Component({
  selector: 'app-list-recipe-suggested',
  templateUrl: './list-recipe-suggested.component.html',
  styleUrls: ['./list-recipe-suggested.component.css']
})
export class ListRecipeSuggestedComponent implements OnInit {
  componentName: String;
  SuggestedRecipes: any = [];
  handleUpdateResponse: any;
  handleError: any;

  constructor(private recipeService: RecipeService) {
    this.componentName = "recipes";
 }
  // Angular Init method, retrieve all notifications from database
  ngOnInit(): void {
    this.recipeService.getSuggestedRecipes({
      "ingredients": "[\"chicken\",\"spinach\",\"fettucini\"]"
    }).subscribe(res => {
      console.log(res.hits)
      this.SuggestedRecipes = res.hits;
    });
  }
}
