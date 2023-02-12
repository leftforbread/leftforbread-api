import { Component, OnInit } from '@angular/core';
import { RecipeService } from '../service/recipe/recipe.service';

@Component({
  selector: 'app-list-recipe-favorite',
  templateUrl: './list-recipe-favorite.component.html',
  styleUrls: ['./list-recipe-favorite.component.css']
})
export class ListRecipeFavoriteComponent implements OnInit {
  componentName: String;
  FavoriteRecipes: any = [];
  handleUpdateResponse: any;
  handleError: any;

  constructor(private recipeService: RecipeService) {
    this.componentName = "recipes";
 }
  // Angular Init method, retrieve all notifications from database
  ngOnInit(): void {
    this.recipeService.getFavoriteRecipes().subscribe(res => {
      console.log(res)
      this.FavoriteRecipes = res;
    });
  }
}
