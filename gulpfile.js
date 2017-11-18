// Importando módulo gulp e plugins
var gulp = require('gulp'),
    cssnano = require('gulp-cssnano'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    runSequence = require('run-sequence');

// Task para minificar arquivos css e juntá-los em um único arquivo
// utilizando o cssnano e o concat
gulp.task('minify-css', function() {
    return gulp.src('static/css/**/*.css')
        .pipe(concat('main.min.css'))
        .pipe(cssnano())
        .pipe(gulp.dest('static/css'));
});

// Task para minificar arquivos js e juntá-los em um único arquivo
// utilizando o uglify e o concat
gulp.task('minify-js', function() {
  return gulp.src('static/js/**/*.js')
    .pipe(concat('main.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('static/js'));
});

// Task default, que executa as tasks de minify
gulp.task('default', function(callback) {
    runSequence('minify-css',
                'minify-js',
                callback);
});
